# [STYLE]
# Global variable: [var]
# Local variable: _[var]

from indata import indata
from tool import Tool, TOOLS
import os

tooling: any = Tool(TOOLS, "roff") # Assume roff as it is 
                                   # the most popular.

def mantool_match(_mantool: str) -> str:
    _mantool_valid: bool = False
    for _toolk in TOOLS.keys():
        if _toolk == _mantool:
            return TOOLS[_toolk]
    if not _mantool_valid:
        print("-rtfm: ERROR! Maybe you should read the fucking manual!?")
    return "NULL"

def recipe_match(
        _indata: dict[str],
        _proc: dict[str],
        _inst: str) -> None:
    _main: str       = _indata[_proc][_inst]
    _main_split: str = _main.split(" ")
    match _inst:
        case "cmd":
            os.system(_main) 
        case "tool":
            tooling.tooling_list[_main_split[0]] = " ".join(_main_split[1:])
        case "build":
            _cmd: str = f"{tooling.tool} {_main}"
            os.system(_cmd)
            print(f"-rtfm: build returned {os.system(_cmd)}")
        case "use":
            if (mantool_match(_main) != "NULL"):
                tooling.tool = TOOLS[_main]
        case _:
            print("-rtfm: ERROR. Read the fucking manual.")

def interpret(_indata: dict[str]) -> None:
    for _proc in _indata:
        for _inst in _indata[_proc]:
            recipe_match(_indata, _proc, _inst)
