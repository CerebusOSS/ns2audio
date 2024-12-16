from pathlib import Path

from neo.rawio import BlackrockRawIO
import scipy.io.wavfile as wavfile
import scipy.signal
import typer


def main(filepath: str, chidx: int = 1, start_time: float = 0.0, duration: float | None = None):
    filepath = Path(filepath)
    if not filepath.is_absolute():
        filepath = Path(__file__).parent / filepath
    io = BlackrockRawIO(filepath)
    io.parse_header()

    fs = 30_000
    
    i_start = int(start_time * fs)
    i_stop = (i_start + int(duration * fs)) if duration is not None else None

    raw_sigs = io.get_analogsignal_chunk(
        block_index=0, seg_index=0,
        i_start=i_start,
        i_stop=i_stop,
        channel_indexes=None
    )
    float_sigs = io.rescale_signal_raw_to_float(raw_sigs, dtype="float64")

    coefs = scipy.signal.butter(
        8,
        Wn=(250, 2_500),
        btype="bandpass",
        fs=30_000,
        output="sos",
    )
    filt_sigs = scipy.signal.sosfilt(coefs, float_sigs, axis=0)
    
    outpath = filepath.parents[1] / "out" / (filepath.stem + ".wav")
    outpath.parent.mkdir(exist_ok=True)
    wavfile.write(outpath, 30_000, filt_sigs[:, chidx-1] * 0.01)


if __name__ == "__main__":
    typer.run(main)
