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
            tool: str) -> None:
        self.tooling_list: dict[str] = tooling_list
        if not tool in self.tooling_list.keys() and tool != "":
            print(TOOL_NOT_FOUND_ERROR)
            for real_tool in self.tooling_list.keys():
                print(real_tool)
            self.tool: str = ""
            return
        self.tool: str = self.tooling_list[tool]

    def save(self, file: str) -> None:
        self.saved_tool: str = file
        with open(file, "w") as tool_cfg:
            tool_cfg.write(self.tool)
            tool_cfg.close()

    def get(self) -> None:
        with open(self.saved_tool, "r") as tool_cfg:
            return tool_cfg.read()

# EXPORT
__all__: list[str] = [TOOLS, Tool]
