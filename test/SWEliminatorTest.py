from smart.preprocessor import SWEliminator


class SWEliminatorTest(object):
    def testEliminateStopwords(self):
        tokens = ['tulisan', 'ini', 'masih', 'terkait', 'dengan', 'tulisan', 'saya', 'sebelumnya', 'tentang', 'penggunaan',
                  'library', 'python', 'sastrawi', 'dalam', 'proses', 'steeming', 'bahasa', 'indonesia', '.', 'pada',
                  'tulisan', 'ini', 'saya', 'akan', 'menjelaskan', 'tentang', 'proses', 'stopword', 'removal', 'tentu',
                  'saja', 'dengan', 'menggunakan', 'python', 'sastrawi', '.']
        swEliminator = SWEliminator(tokens)
        print(swEliminator.getSWEliminatedTokens())

    def runTest(self):
        self.testEliminateStopwords()

sweTest = SWEliminatorTest()
sweTest.runTest()