import numpy as np

class Array:

    def __init__(self):
        self.array = np.array([])

    def addToArray2x3(self, a11, a12, a13, a21, a22, a23):
        self.array = np.array([(a11, a12, a13),
                               (a21, a22, a23)])

    def getArray(self):
        return self.array

    def arrayOfZeros(self, size):
        self.array = np.zeros(size)

    def arrayOfEye(self, size):
        self.array = np.eye(size)

    def maxValue(self):
        return self.array.max()

    def sumValues(self):
        return self.array.sum()

    def meanValues(self):
        return self.array.mean()

    def stdOfValues(self):
        return self.array.std()