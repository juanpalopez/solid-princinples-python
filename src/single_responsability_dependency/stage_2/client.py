from book import Book
from printer import StandardOutputPrinter, StandardOutputHtmlPrinter


class Client:
    def client(self):
        book = Book()
        currentPage = book.getCurrentPage()

        # printerStandard = StandardOutputPrinter()
        printerHtml = StandardOutputHtmlPrinter()

        # printerStandard.printPage(currentPage)
        printerHtml.printPage(currentPage)


if __name__ == "__main__":
    client = Client()
    client.client()
