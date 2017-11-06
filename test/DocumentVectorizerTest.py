from src.smart.preprocessor.DocumentVectorizer import DocumentVectorizer

class DocumentVectorizerTest(object):
    def test_vectorizer(self):
        document = ['bangsa indonesia banyak yang kerja di luar indonesia ', 'orang indonesia luar biasa']
        vectorizer = DocumentVectorizer(document)
        out = vectorizer.vectorize()
        print(out)
        print(out.shape)

    def run_test(self):
        self.test_vectorizer()

vectorizerTest = DocumentVectorizerTest()
vectorizerTest.run_test()
