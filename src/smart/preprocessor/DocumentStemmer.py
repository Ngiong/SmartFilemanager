from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class DocumentStemmer(object):
    def __init__(self, token):
        self.token = token

    def stem(self):
        result = []
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        for item in self.token:
            result.append(stemmer.stem(item))

        return result