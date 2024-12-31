import os

# Toolset.
TOOLS: dict[str] = {
    "tex"   : "tex",
    "latex" : "latex",
    "man"   : "/usr/bin/install -c",
    "roff"  : "groff"
}

TOOL_NOT_FOUND_ERROR: str = """-rtfm: ERROR. Tool doesn't match up with
any tool in the tooling list. The tooling list is as such:"""

class Tool:
    def __init__(
            self,
            tooling_list: dict[str],
            tool: str,
            saved_tool: str) -> None:
        self.tooling_list: dict[str] = tooling_list
        self.saved_tool: str = saved_tool

        for file in os.listdir("."):
            if file == self.saved_tool:
                os.remove(file)
        
        if not tool in self.tooling_list.keys() and tool != "":
            print(TOOL_NOT_FOUND_ERROR)
        
            for real_tool in self.tooling_list.keys():
                print(real_tool)
            self.tool: str = ""
            return
        self.tool: str = self.tooling_list[tool]

    def save(self) -> None:
        with open(self.saved_tool, "a") as tool_cfg:
            tool_cfg.write(f"{self.tool}\n")
            tool_cfg.close()

    def get(self) -> None:
        with open(self.saved_tool, "r") as tool_cfg:
            return tool_cfg.readlines()[-1].rstrip("\n")

# EXPORT
__all__: list[str] = [TOOLS, Tool]
