class DocumentPreprocessor(object):
    def __init__(self, document_str):
        self.document = document_str

    def eliminate_stopwatch(self):

        return self

    def convert_lowercase(self):
        self.document = self.document.lower()
        return self

    def tokenize(self):

        return self

    def vectorize(self):
        return 0