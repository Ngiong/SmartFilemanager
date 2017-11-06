from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class DocumentStemmer(object):
    def __init__(self, document):
        self.document = document

    def stem(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        self.document = stemmer.stem(self.document)
        return self.document