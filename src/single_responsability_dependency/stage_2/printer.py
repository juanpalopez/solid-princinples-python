from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def printPage(self, page: str) -> None:
        raise NotImplementedError


class StandardOutputPrinter(Printer):
    def printPage(self, page: str) -> None:
        print(page)


class StandardOutputHtmlPrinter(Printer):
    def printPage(self, page: str) -> None:
        print("<div>{}<div>".format(page))
