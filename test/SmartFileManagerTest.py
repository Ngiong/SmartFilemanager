from smart.filemanager import SmartFileManager

class SmartFileManagerTest(object):
    TESTING_PATH = '/home/varian97/Desktop/testing/'
    TESTING_FILE_READ = 'ConstituencyParsing.txt'
    TESTING_DIRNAME = 'hello_from_the_other_side'

    def testListFiles(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.listFiles()

    def testGetDocument(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.getDocument(self.TESTING_FILE_READ)

    def testMakeDirectory(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.makeDirectory(self.TESTING_DIRNAME)

    def testMoveDocument(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.moveDocument(self.TESTING_FILE_READ, self.TESTING_DIRNAME)

    def test_manage(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.manage()

    def runTest(self):
        #self.testListFiles()
        #self.testGetDocument()
        self.test_manage()
        #self.testMakeDirectory()
        #self.testMoveDocument()
        return 0

sfmTest = SmartFileManagerTest()
sfmTest.runTest()