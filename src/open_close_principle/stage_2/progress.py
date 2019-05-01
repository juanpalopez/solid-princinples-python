from file import File
from song import Song
from measurable import Measurable


class Progress:
    def getSentLengthPercentage(measurable: Measurable) -> float:
        return measurable.getSentLength() * 100 / measurable.getTotalLength()
