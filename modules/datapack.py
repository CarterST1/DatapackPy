import PIL

class DataPack:
    def __init__(self, version: tuple[int, int, int]) -> None:
        self.game_version = version
        self.icon = None
