from sklearn.cluster import KMeans

class DocumentCluster(object):
    def __init__(self, word_vector):
        self.word_vector = word_vector

    def cluster(self, n_cluster):
        km = KMeans(n_clusters=n_cluster)
        km.fit(self.word_vector)
        return km