from smart.filemanager import SmartFileManager

class SmartFileManagerTest(object):
    TESTING_PATH = '/home/varian97/Desktop/testing/'
    TESTING_PATH_2 = 'C://Users//Ngiong//Desktop//testing'
    TESTING_PATH_3 = 'E://IF/Semester_7/NLP/test'
    TESTING_PDF_READ = 'E://IF/Semester_7/NLP/test/IF2130-12-2014-Exception.pdf'
    TESTING_FILE_READ = 'ConstituencyParsing.txt'
    TESTING_DIRNAME = 'hello_from_the_other_side'

    def testListFiles(self):
        sfm = SmartFileManager(self.TESTING_PATH_3)
        sfm.listFiles()

    def testGetDocument(self):
        sfm = SmartFileManager(self.TESTING_PATH_3)
        sfm.getDocument(self.TESTING_FILE_READ)

    def testMakeDirectory(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.makeDirectory(self.TESTING_DIRNAME)

    def testMoveDocument(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        sfm.moveDocument(self.TESTING_FILE_READ, self.TESTING_DIRNAME)

    def test_manage(self):
        sfm = SmartFileManager(self.TESTING_PATH_3)
        sfm.manage(2)

    def test_pdfPathToText(self):
        sfm = SmartFileManager(self.TESTING_PATH)
        print (sfm.pdfPathToTxt(self.TESTING_PDF_READ))

    def runTest(self):
        # self.testListFiles()
        # self.testGetDocument()
        self.test_manage()
        # self.testMakeDirectory()
        # self.testMoveDocument()
        #self.test_pdfPathToText()
        return 0

sfmTest = SmartFileManagerTest()
sfmTest.runTest()