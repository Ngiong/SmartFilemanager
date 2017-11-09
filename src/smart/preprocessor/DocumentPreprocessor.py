from smart.preprocessor import *

class DocumentPreprocessor(object):
    def __init__(self, document_str):
        self.document = document_str

    def convert_lowercase(self):
        self.document = self.document.lower()
        return self

    def tokenize(self):
        docTokenizer = DocumentTokenizer(self.document)
        self.document = docTokenizer.getTokens()
        return self

    def eliminate_stopwatch(self):
        swEliminator = SWEliminator(self.document)
        self.document = swEliminator.getSWEliminatedTokens()
        return self

    def stem(self):
        doc_stemmer = DocumentStemmer(self.document)
        self.document = doc_stemmer.stem()
        return self

    def vectorize(self):
        return 0