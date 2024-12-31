#!/usr/bin/python3

from os import listdir
pwd = listdir(".")

from sys import argv
argc = len(argv)

from indata import indata
from interpreter import interpret

NOCFG_ERROR_MSG: str = """-rtfm: rtfm.cfg doesn't exist!
Please create an rtfm.cfg an configure rtfm to continue.
Type -h or --help for more information on rtfm."""
NOCFG_ERROR_CODE = 1

HELP_FLAGS: list[str] = ["-h", "--help"]
HELP_MSG: str = """-- RTFM: Read The Fucking Manual --
DESCRIPTION: RTFM is a program made to generate 
             manuals, hence the name of 
             \"Read The fucking Manual\".
USAGE: rtfm <flags>
FLAGS:
    -h, --help: Print this message"""

def cfg_exists() -> bool:
    cfg: bool = False
    for file in pwd:
        if file == f"rtfm.cfg":
            cfg = True
    return cfg
        
def build_man() -> int:
    if not cfg_exists():
        print(NOCFG_ERROR_MSG)
        return NOCFG_ERROR_CODE
    PORT_IN: any = indata(f"rtfm.cfg")
    interpret(PORT_IN.data)
    return 0

def main() -> None:
    if argc >= 1:
        build_man()
        return
    if argv[1] in HELP_FLAGS:
        print(HELP_MSG)
        return
        
if __name__ == "__main__":
    main()
