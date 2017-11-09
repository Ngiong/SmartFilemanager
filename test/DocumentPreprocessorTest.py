from smart.preprocessor import DocumentPreprocessor

class DocumentPreprocessorTest(object):
    def test_prepocessor(self):
        document = 'Anak menjerit-jerit, asap panas membara, lahar dan debu menjadi makanan'
        preprocessor = DocumentPreprocessor(document)
        result = preprocessor.convert_lowercase().tokenize().eliminate_stopwatch().stem().to_string()
        print(result)

    def run_test(self):
        self.test_prepocessor()

test = DocumentPreprocessorTest()
test.run_test()