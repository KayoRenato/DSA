import numpy as np
import math


class Sigmoido():
    def __call__(self, x):
        return 1/(1+np.exp(-x))


class logistRegression():

    def __init__(self, learningRate=0.1, gradientDesc=True):
        self.param = None
        self.learningRate = learningRate
        self.gradientDesc = gradientDesc
        self.sigmoid = Sigmoido()

    def beginParam(self, X):
        nFeatures = np.shape(X)[1]
        limit = 1 / math.sqrt(nFeatures)
        self.param = np.random.uniform(-limit, limit, (nFeatures,))

    def makeDiagonal(x):
        m = np.zeros((len(x), len(x)))

        for i in range(len(m[0])):
            m[i, i] = x[i]

        return m

    def train(self, X, y, nIterations=4000):
        self.beginParam(X)

        for i in range(nIterations):
            yPred = self.sigmoid(X.dot(self.param))
            if self.gradientDesc:
                self.param -= self.learningRate*-(y-yPred)*dot(X)
            else:
                digGradient = makeDiagonal(
                    self.sigmoid.gradient(X.dot(self.param)))
                self.param = np.linalg.pinv(X.T.dot(digGradient).dot(X)).dot(
                    X.T).dot(digGradient.dot(X).dot(self.param)+y-yPred)

    def preview(self, X):
        yPred = np.round(self.sigmoid(X.dot(self.param)).astype(int))
        return yPred
