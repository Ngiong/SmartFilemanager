from src.smart.preprocessor import DocumentTokenizer


class DocumentTokenizerTest(object):
    def testTokenizer(self):
        str = 'Tulisan ini masih terkait dengan tulisan saya sebelumnya tentang penggunaan library Python Sastrawi ' \
              'dalam proses steeming Bahasa Indonesia . Pada tulisan ini saya akan menjelaskan tentang proses Stopword ' \
              'Removal tentu saja dengan menggunakan Python Sastrawi.'
        docTokenizer = DocumentTokenizer(str)
        print(docTokenizer.getTokens())

    def runTest(self):
        self.testTokenizer()

dtTest = DocumentTokenizerTest()
dtTest.runTest()