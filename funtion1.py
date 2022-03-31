import math


def mean(array):
    return sum(array) / len(array)


def findB(value1, value2):
    sigmaTop = 0
    sigmaBot = 0
    for j in range(0, len(value1)):
        sigmaTop += (value1[j] - mean(value1)) * (value2[j] - mean(value2))
        sigmaBot += math.pow(value1[j] - mean(value1), 2)
    b = sigmaTop / sigmaBot
    return b


def findA(value1, value2, b):
    a = mean(value2) - b * mean(value1)
    return a
