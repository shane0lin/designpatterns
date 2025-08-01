from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

class WordDocument(Document):
    def open(self):
        print("Opening Word document.")

class ExcelDocument(Document):
    def open(self):
        print("Opening Excel document.")

class PDFDocument(Document):
    def open(self):
        print("Opening PDF document.")

class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

class WordDocumentCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()

class ExcelDocumentCreator(DocumentCreator):
    def create_document(self):
        return ExcelDocument()

class PDFDocumentCreator(DocumentCreator):
    def create_document(self):
        return PDFDocument()


if __name__ == "__main__":
    creator = WordDocumentCreator()
    doc = creator.create_document()
    doc.open()

    creator = ExcelDocumentCreator()
    doc = creator.create_document()
    doc.open()

    creator = PDFDocumentCreator()
    doc = creator.create_document()
    doc.open()