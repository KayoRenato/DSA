from sklearn.datasets import load_iris
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
                self.param -= self.learningRate * -(y-yPred).dot(X)
            else:
                digGradient = makeDiagonal(
                    self.sigmoid.gradient(X.dot(self.param)))
                self.param = np.linalg.pinv(X.T.dot(digGradient).dot(X)).dot(
                    X.T).dot(digGradient.dot(X).dot(self.param)+y-yPred)

    def preview(self, X):
        yPred = np.round(self.sigmoid(X.dot(self.param))).astype(int)
        return yPred


def normalizeData(X, axis=-1, order=2):
    I2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    I2[I2 == 0] = 1
    return X / np.expand_dims(I2, axis)


def randomData(X, y, seed=None):
    if seed:
        np.random.seed(seed)
        idx = np.arange(X.shape[0])
        np.random.shuffle(idx)
        return X[idx], y[idx]


def calcAccuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred, axis=0)/len(y_true)
    return accuracy


def trainTestSplit(X, y, testSize=0.5, shuffle=True, seed=None):
    if shuffle:
        X, y = randomData(X, y, seed)

    split_i = len(y)-int(len(y)//(1/testSize))
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test


def main():
    # carregar dados
    data = load_iris()

    # normalizar dados
    X = normalizeData(data.data[data.target != 0])

    # carregar dados de saida
    y = data.target[data.target != 0]
    y[y == 1] = 0
    y[y == 2] = 1

    # dividir os dados em treino e test
    X_train, X_test, y_train, y_test = trainTestSplit(
        X, y, testSize=0.33, seed=1)

    # definir modelo
    model = logistRegression(gradientDesc=True)

    # treinar modelo
    model.train(X_train, y_train)

    y_pred = model.preview(X_test)

    accu = calcAccuracy(y_test, y_pred)

    print(f'Acuracia do Modelo:{accu:.3f}\n')


if __name__ == "__main__":
    main()
