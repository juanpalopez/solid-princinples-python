from measurable import Measurable


class Song(Measurable):
     def __init__(self, totalLength: int, sentLength: int):
        self.totalLength = totalLength
        self.sentLength = sentLength

    def getTotalLengthPercentage(self) -> int:
        return self.totalLength
    
    def getSentLengthPercentage(self) -> int:
        return self.sentLength
    
