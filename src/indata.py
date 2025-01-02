def fgetl(file: str) -> list[str]:
    with open(file, "r") as f:
        return f.readlines()

class indata:
    def __init__(self, file: str) -> None:
        self.raw: list[str]  = fgetl(file)
        self.file: str       = file
        self.construct()

    def construct(self) -> None:
        self.data: dict[str] = {}
        recipe_name: str = ""
        for ln in self.raw:
            if not ln.startswith("    "):
                recipe_name: str = ln.rstrip(":").rstrip(":\n")
                self.data[recipe_name] = {}
            if ln.startswith("    ") and not recipe_name.lstrip(" ") == "":
                self.data[recipe_name][ln.lstrip("    ").split(" ")[0].rstrip(":")] = \
                    " ".join(ln.lstrip("    ").split(" ")[1:]).rstrip("\n")
