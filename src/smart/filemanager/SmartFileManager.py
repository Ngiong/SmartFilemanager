import os
import platform
from tkinter import simpledialog

import pandas as pd
from io import StringIO
from smart.preprocessor import DocumentPreprocessor
from smart.clustering import DocumentCluster
from smart.summarizer import DocumentsSummarizer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


class SmartFileManager(object):
    PATH = '';

    def __init__(self, path, use_gui = False):
        self.PATH = path
        self.titles = []
        self.document_content = []
        self.use_gui = use_gui
        os.chdir(self.PATH)

    def listFiles(self):
        files = os.listdir(self.PATH)
        for file in files:
            if(os.path.isfile(file)):
                self.titles.append(file)
                self.document_content.append(self.getDocument(file))
            print(file)

    def getDocument(self, filename):
        ext = os.path.splitext(filename)[1]
        if (ext == '.pdf'):
            result = self.pdfPathToTxt(filename)
        else:
            file_open = open(filename, 'r')
            result = file_open.read()
        return result

    def makeDirectory(self, dirname):
        os.mkdir(dirname)

    def moveDocument(self, filename, dirname):
        if not os.path.isdir(dirname): os.mkdir(dirname)

        if platform.system() == 'Windows':
            os.rename(filename, dirname+'\\'+filename)
        else :
            os.rename(filename, dirname + '/' + filename)

    def pdfPathToTxt(self, path):
        rsrcmgr = PDFResourceManager()
        sio = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        fp = open(path, 'rb')
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
        fp.close()
        text = sio.getvalue()
        device.close()
        sio.close()
        return text

    ###
    # TODO: handle empty document / empty directory
    ###
    def manage(self, num_cluster):
        print('Load File...')
        self.listFiles()
        print(self.titles)

        # get the list of stemmed word
        print('Preprocessing...')
        list_of_stemmed_document = []
        stemmed_documents = dict()
        item_i = 0
        for item in self.document_content :
            preprocessor = DocumentPreprocessor(item)
            print('  Preprocessing '
                  + self.titles[item_i])
            word_stemmed = preprocessor.convert_lowercase().tokenize().eliminate_stopwatch().stem().to_string()
            list_of_stemmed_document.append(word_stemmed)
            stemmed_documents[self.titles[item_i]] = word_stemmed
            item_i += 1

        # vectorize
        print('Vectorizing...')
        tfidf_matrix = DocumentPreprocessor(list_of_stemmed_document).vectorize()

        # clustering
        print('Clustering...')
        clusters = DocumentCluster(tfidf_matrix).cluster(num_cluster).labels_.tolist()

        # mapping cluster and document
        print('Cluster-Document mapping...')
        documents = {'title' : self.titles, 'content' : self.document_content, 'cluster' : clusters}
        frame = pd.DataFrame(documents, index=[clusters], columns=['title', 'cluster'])

        print("Result of clustering : ")
        for i in range(num_cluster):
            gui_text = ''
            print("Cluster %d titles:\n" % i)
            gui_text += "Cluster %d titles:\n\n" % i

            # Get contents for summarization
            cluster_contents = []
            for title in frame.ix[i]['title'].values.tolist():
                cluster_contents.append(stemmed_documents[title])
                print(' %s,' % title)
                gui_text += ' %s\n' % title
            print('\n')
            gui_text += '\n'

            # Summarization
            docs_summarizer = DocumentsSummarizer(cluster_contents)
            document_keywords = docs_summarizer.getSummarization()
            print('Some Suggestion Candidates: ', document_keywords[:7])
            gui_text += 'Some Suggestion Candidates: ' + str(document_keywords[:7]) + '\n'

            if self.use_gui:
                cluster_name = simpledialog.askstring('Please enter the name for the folder', gui_text)
            else:
                cluster_name = input("Please enter the name for the folder : ")

            # Move document to subfolder
            for title in frame.ix[i]['title'].values.tolist():
                self.moveDocument(title, cluster_name)

