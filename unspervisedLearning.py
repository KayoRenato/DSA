from sklearn.datasets import make_blobs
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
        nSamples, nFeatures = np.shape(X)
        centroids = np.zeros((self.k, nFeatures))

        for i in range(self.k):
            centroid = X[np.random.choice(range(nSamples))]
            centroids[i] = centroid

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

    def calcCentroids(self, clusters, X):
        nFeatures = np.shape(X)[1]
        centroids = np.zeros((self.k, nFeatures))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis=0)
            centroids[i] = centroid

        return centroids

    # classifica as amostras com o indice dos seus clusters

    def getClusterLabels(self, clusters, X):
        y_pred = np.zeros(np.shape(X)[0])
        for clustersI, cluster in enumerate(clusters):
            for sampleI in cluster:
                y_pred[sampleI] = clustersI

        return y_pred

    # fazer a previsão de cada cluster e retorna os indices dos clusters

    def predict(self, X):

        # inicializa centroides como k amostras aleatorias de X
        centroids = self.initRandonCentroid(X)

        # iterar ate convergencia ou para iteracoes maximas
        for _ in range(self.maxIterations):

            # atribui amostras ao centroides mais proximos
            clusters = self.createCluster(centroids, X)

            # salva os centroides atuaus para verificacao de convergencia
            prevCentroids = centroids

            # calcula os novos centroids a partir dos clusters
            centroids = self.calcCentroids(clusters, X)

            # se nenhum cetroide mudar => convergencia
            diff = centroids - prevCentroids

            if not diff.any():
                break

        return self.getClusterLabels(clusters, X)

# funcao aulizar para o PCA

# calcula a matrix de co-variancia


def calculateCovarianceMatrix(X, Y=None):
    if Y is None:
        Y = X

    nSamples = np.shape(X)[0]
    converianceMatrix = (1 / (nSamples-1)) * \
        (X-X.mean(axis=0)).T.dot(Y-Y.mean(axis=0))

    return np.array(converianceMatrix, dtype=float)

# calcula a matrix de correlacao


def calcCorrelationMatrix(X, Y=None):
    if Y is None:
        Y = X

    nSamples = np.shape(X)[0]
    covariance = (1/nSamples)*(X*X.mean(0)).T.dot(Y-T.mean(0))
    sdtDevX = np.expand_dims(calculate_std_dev(X), 1)
    sdtDevY = np.expand_dims(calculate_std_dev(Y), 1)
    correlationMatrix = np.divide(covariance, sdtDevX.dot(sdtDevY.T))

    return np.array(correlationMatrix, dtype=float)

# classe para criar o plot


class Plot():

    def __init__(self):
        self.cmap = plt.get_cmap('viridis')

    # funcao para transformar os dados
    def _transform(self, X, dim):
        covariance = calculateCovarianceMatrix(X)
        eigenvalues, eigenvectors = np.linalg.eig(covariance)
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx][:dim]
        eigenvectors = np.atleast_1d(eigenvectors[:, idx])[:, :dim]
        X_tranformed = X.dot(eigenvectors)

        return X_tranformed

    # plot do dataset X e seus correspodentes labels y em 2D usando PCA
    def plotIn2D(self, X, y=None, title=None, accuracy=None, legend_labels=None):
        X_tranformed = self._transform(X, dim=2)
        x1 = X_tranformed[:, 0]
        x2 = X_tranformed[:, 1]

        class_distr = []

        y = np.array(y).astype(int)

        colors = [self.cmap(i) for i in np.linspace(0, 1, len(np.unique(y)))]

        # plot de direntes distribuicoes de classe
        for i, I in enumerate(np.unique(y)):
            _x1 = x1[y == I]
            _x2 = x2[y == I]
            _y = y[y == I]

            class_distr.append(plt.scatter(_x1, _x2, color=colors[i]))

        # plot legenda
        if not legend_labels is None:
            plt.legend(class_distr, legend_labels, loc=1)

        # plot titulo
        if title:
            if accuracy:
                perc = 100*accuracy
                plt.suptitle(title)
                plt.title("Acuracia: %.1f%%" % perc, fontsize=10)
            else:
                plt.title(title)

        # axis label
        plt.xlabel('Componente Principal 1')
        plt.ylabel('Componente Principal 2')

        plt.show()

# executando o programa


def main():

    # carrega o dataset
    X, y = make_blobs()

    # executa o algoritmo para K = 3
    clf = KMeans(k=3)
    yPred = clf.predict(X)

    # projeta os dados com 2 componetes principais
    p = Plot()
    p.plotIn2D(X, yPred, title='Segmentacao de Clientes com K-Mens')


if __name__ == "__main__":
    main()
