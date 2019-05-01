from abc import ABC, abstractmethod


class Measurable(ABC):

    @abstractmethod
    def getTotalLength(self):
        raise NotImplementedError

    @abstractmethod
    def getSentLength(self):
        raise NotImplementedError
