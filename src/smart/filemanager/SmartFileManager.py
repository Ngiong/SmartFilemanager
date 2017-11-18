import os
import platform
import pandas as pd
from smart.preprocessor import DocumentPreprocessor
from smart.clustering import DocumentCluster
from smart.summarizer import DocumentsSummarizer


class SmartFileManager(object):
    PATH = '';

    def __init__(self, path):
        self.PATH = path
        self.titles = []
        self.document_content = []
        os.chdir(self.PATH)

    def listFiles(self):
        files = os.listdir(self.PATH)
        for file in files:
            if(os.path.isfile(file)):
                self.titles.append(file)
                self.document_content.append(self.getDocument(file))
            print(file)

    def getDocument(self, filename):
        file_open = open(filename, 'r')
        result = file_open.read()
        print(result)
        return result

    def makeDirectory(self, dirname):
        os.mkdir(dirname)

    def moveDocument(self, filename, dirname):
        if not os.path.isdir(dirname): os.mkdir(dirname)

        if platform.system() == 'Windows':
            os.rename(filename, dirname+'\\'+filename)
        else :
            os.rename(filename, dirname + '/' + filename)

    ###
    # TODO: handle empty document / empty directory
    ###
    def manage(self, num_cluster):
        self.listFiles()
        print(self.titles)

        # get the list of stemmed word
        list_of_stemmed_document = []
        stemmed_documents = dict()
        item_i = 0
        for item in self.document_content :
            preprocessor = DocumentPreprocessor(item)
            word_stemmed = preprocessor.convert_lowercase().tokenize().eliminate_stopwatch().stem().to_string()
            list_of_stemmed_document.append(word_stemmed)
            stemmed_documents[self.titles[item_i]] = word_stemmed
            item_i += 1

        # vectorize
        tfidf_matrix = DocumentPreprocessor(list_of_stemmed_document).vectorize()

        # clustering
        clusters = DocumentCluster(tfidf_matrix).cluster(num_cluster).labels_.tolist()

        # mapping cluster and document
        documents = {'title' : self.titles, 'content' : self.document_content, 'cluster' : clusters}
        frame = pd.DataFrame(documents, index=[clusters], columns=['title', 'cluster'])

        print("Result of clustering : ")
        for i in range(num_cluster):
            print("Cluster %d titles:\n" % i)

            # Get contents for summarization
            cluster_contents = []
            for title in frame.ix[i]['title'].values.tolist():
                cluster_contents.append(stemmed_documents[title])
                print(' %s,' % title)
            print('\n')

            # Summarization
            docs_summarizer = DocumentsSummarizer(cluster_contents)
            document_keywords = docs_summarizer.getSummarization()
            print('Some Suggestion Candidates: ', document_keywords)
            cluster_name = input("Please enter the name for the folder : ")

            # Move document to subfolder
            for title in frame.ix[i]['title'].values.tolist():
                self.moveDocument(title, cluster_name)

