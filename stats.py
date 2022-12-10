class Stats:
    def __init__(self, bulls: int, cows: int) -> None:
        self.bulls = bulls
        self.cows = cows

    def __str__(self) -> str:
        return f"bulls: {self.bulls}, cows: {self.cows}"