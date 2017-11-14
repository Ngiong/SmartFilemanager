from gui import MainWindow


class GUITest(object):
    def testGui(self):
        main_window = MainWindow()
        main_window.start()

    def runTest(self):
        self.testGui()


gui_test = GUITest()
gui_test.runTest()