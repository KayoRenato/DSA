import math
import numpy as np
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Normalizar dados


def normalizeDada(X, axis=-1, order=2):
    I2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    I2[I2 == 0] = 1
    return X / np.expand_dims(I2, axis)


def calcDistEucl(x1, x2):
    dist = 0
    for i in range(len(x1)):
        dist += pow((x1[i]-x2[i]), 2)

    return math.sqrt(dist)


class KMeans():
    def __init__(self, k=3, maxIterations=500):
        self.k = k
        self.maxIterations = maxIterations

    def initRandonCentroid(self, X):
        nSamples, nFeatures = np.shape(x)
        centroids = np.zeros((self.k, nFeatures))

        for i in range(self.k):
            centroid = X[np.random.choice(range(nSamples))]
            centroid[i] = centroid

        return centroids

    # retorna o indice mais proximo do centroide da amostra

    def closestCentroid(self, sample, centroids):
        closestI = 0
        closestDist = float('inf')
        for i, centroid in enumerate(centroids):
            distance = calcDistEucl(sample, centroid)
            if distance < closestDist:
                closestI = i
                closestDist = distance

        return closestI

    # assosia as amostras de dados aos centroides mais proximos para criar os clusters
    def createCluster(self, centroids, X):
        n_samples = np.shape(X)[0]
        clusters = [[] for _ in range(self.k)]
        for sampleI, sample in enumerate(X):
            centroidI = self.closestCentroid(sample, centroids)
            clusters[centroidI].append(sampleI)

        return clusters

    def calcCentroids(self.k, clusters, X):
        nFeatures = np.shape(X)[1]
        centroids = np.zeros((self.k, nFeatures))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis=0)
            centroids[i] = centroid

        return centroids
