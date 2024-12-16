Just a silly little script to convert Blackrock ns5 or ns6 files to audio.

## Prerequisites

* Install dependencies. I use `uv`.

## Usage

As long as you have a Python environment with the required dependencies installed then it's just a matter of calling the `ns2audio.py` script with arguments.

I use `uv` so I typically run it with `uv run ns2audio path/to/my.ns5

```
 Usage: ns2audio.py [OPTIONS] FILEPATH                                                                                                                                                           
                                                                                                                                                                                                 
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────
│ *    filepath      TEXT  [default: None] [required]                                           
╰───────────────────────────────────────────────────────────────────────────────────────────────
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────
│ --chidx             INTEGER  [default: 1]                                                     
│ --start-time        FLOAT    [default: 0.0]                                                   
│ --duration          FLOAT    [default: None]                                                  
│ --help                       Show this message and exit.     
╰───────────────────────────────────────────────────────────────────────────────────────────────
```

* `chidx` -- 1-based index to the channel that will be converted. You can provide more than 1 integer by editing the script if you want stereo audio files.
* `start-time` -- in seconds since the beginning of the file

Tested in Python 3.12 on MacOS ARM.
