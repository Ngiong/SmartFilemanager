from src.smart.preprocessor import DocumentStemmer
from src.smart.preprocessor import DocumentTokenizer

class DocumentStemmerTest(object):
    def test_stemmer (self):
        document = "Bangsa Indonesia sedang bersedih karena kehilangan salah satu musisi terbaiknya." \
                   "Karena begitu sedihnya, Indonesia dihibur oleh negara tetangga."
        tokenizer = DocumentTokenizer(document)
        stemmer = DocumentStemmer(tokenizer.getTokens())
        result = stemmer.stem()
        print(result)

    def run_test(self):
        self.test_stemmer()

doc_stemmer_test = DocumentStemmerTest()
doc_stemmer_test.run_test()