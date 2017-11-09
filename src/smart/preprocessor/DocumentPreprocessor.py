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
        eliminated_word = swEliminator.getSWEliminatedTokens()
        self.document = ''
        for word in eliminated_word:
            self.document += word + ' '
        self.document = self.document[:len(self.document)-1]
        return self

    def stem(self):
        doc_stemmer = DocumentStemmer(self.document)
        self.document = doc_stemmer.stem()
        return self

    def vectorize(self):
        vectorizer = DocumentVectorizer(self.document)
        out = vectorizer.vectorize()
        return out

    def to_string(self):
        return self.document