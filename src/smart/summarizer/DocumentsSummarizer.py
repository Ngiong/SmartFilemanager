from gensim.summarization import keywords


class DocumentsSummarizer(object):
    def __init__(self, documents):
        self.documents = documents

    def getSummarization(self):
        concatenated_document = ' '.join(self.documents)
        return keywords(concatenated_document, split=True)