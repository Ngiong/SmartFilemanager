from sklearn.feature_extraction.text import TfidfVectorizer

class DocumentVectorizer(object):
    def __init__(self, document):
        self.document = document

    def vectorize(self):
        vectorizer = TfidfVectorizer(use_idf=False)
        self.document = vectorizer.fit_transform(self.document)
        return self.document

