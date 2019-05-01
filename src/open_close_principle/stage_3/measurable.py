from abc import ABC, abstractmethod


class Measurable(ABC):

    @abstractmethod
    def getTotalLength(self):
        raise NotImplementedError

    @abstractmethod
    def getSentLength(self):
        raise NotImplementedError

    def getSentLengthPercentage(self) -> float:
        return self.getSentLength() * 100 / self.getTotalLength()
