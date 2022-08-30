import numpy as np

class Calculator:

    @staticmethod
    def mulOfSameArrays(array1, array2):
        if len(array2) == 0:
            return np.sum(array1)
        index = 0
        sum = 0
        while index < len(array1):
            sum += array1[index] * array2[index]
            index += 1
        return sum
