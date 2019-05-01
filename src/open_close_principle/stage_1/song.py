class Song:
    def __init__(self, totalLength: int, sentLength: int):
        self.totalLength = totalLength
        self.sentLength = sentLength

    def getSentLengthPercentage(self) -> float:
        return self.sentLength * 100 / self.totalLength
