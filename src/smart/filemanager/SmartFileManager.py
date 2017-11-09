import os
import platform

class SmartFileManager(object):
    PATH = '';

    def __init__(self, path):
        self.PATH = path
        os.chdir(self.PATH)

    def listFiles(self):
        files = os.listdir(self.PATH)
        for file in files:
            print(file)

    def getDocument(self, filename):
        file_open = open(filename, 'r')
        print(file_open.read())

    def makeDirectory(self, dirname):
        os.mkdir(dirname)

    def moveDocument(self, filename, dirname):
        if not os.path.isdir(dirname): os.mkdir(dirname)

        if platform.system() == 'Windows':
            os.rename(filename, dirname+'\\'+filename)
        else :
            os.rename(filename, dirname + '/' + filename)
