class DocumentTokenizer(object):
    PUNCTUATIONS = ['.', ',', '?', '!']
    def __init__(self, document_str):
        self.str = document_str

    def getTokens(self):
        for punct in self.PUNCTUATIONS:
            self.str = self.str.replace(punct, ' ' + punct +' ')
        return self.str.split()