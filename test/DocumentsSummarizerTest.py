from smart.summarizer import DocumentsSummarizer


class DocumentsSummarizerTest(object):
    def testSummarization(self):
        documents = ['This blog is a gentle introduction to text summarization and can serve as a practical summary of the current landscape. It describes how we, a team of three students in the RaRe Incubator programme, have experimented with existing algorithms and Python tools in this domain.',
                     'We compare modern extractive methods like LexRank, LSA, Luhn and Gensim’s existing TextRank summarization module on the Opinosis dataset of 51 article-summary pairs. We also had a try with an abstractive technique using Tensorflow’s Text Summarization algorithm, but didn’t obtain good results due to its extremely high hardware demands (7000 GPU hours, ~$30k cloud credits).',
                     'With push notifications and article digests gaining more and more traction, the task of generating intelligent and accurate summaries for long pieces of text has become a popular research as well as industry problem.',
                     'There are two fundamental approaches to text summarization: extractive and abstractive. The former extracts words and word phrases from the original text to create a summary. The latter learns an internal language representation to generate more human-like summaries, paraphrasing the intent of the original text.',
                     'gensim.summarization module implements TextRank, an unsupervised algorithm based on weighted-graphs from a paper by Mihalcea et al. It was added by another incubator student Olavur Mortensen – see his previous post on this blog. It is built on top of the popular PageRank algorithm that Google used for ranking webpages. TextRank works as follows:']
        docs_summarizer = DocumentsSummarizer(documents)
        print('Keywords:', docs_summarizer.getSummarization())

    def runTest(self):
        self.testSummarization()


dsTest = DocumentsSummarizerTest()
dsTest.runTest()