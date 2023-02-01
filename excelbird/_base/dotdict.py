class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return super().__getattr__(key)


class Style(DotDict):

    def help(self) -> None:
        print(*self.keys(), sep="\n")
