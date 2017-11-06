from src.smart.preprocessor import DocumentStemmer

class DocumentStemmerTest(object):
    def test_stemmer (self):
        document = "Bangsa Indonesia sedang bersedih karena kehilangan salah satu musisi terbaiknya." \
                   "Karena begitu sedihnya, Indonesia dihibur oleh negara tetangga."
        stemmer = DocumentStemmer(document)
        result = stemmer.stem()
        print(result)

    def run_test(self):
        self.test_stemmer()

doc_stemmer_test = DocumentStemmerTest()
doc_stemmer_test.run_test()