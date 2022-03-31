import numpy as np
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


class Num:
    def __init__(self):
        self.ls = None

    def init(self, ls=None):
        self.ls = ls

    def mean(self, data=None):
        lst = data if data else self.ls
        n = len(lst)
        s = sum(lst)
        return s / n if n > 0 else float('nan')

    def median(self, data=None):
        lst = sorted(data) if data else sorted(self.ls)
        n = len(lst)
        mid = (n) // 2
        return lst[mid] if n % 2 else (lst[mid - 1] + lst[mid]) / 2

    def deviation_from_mean(self, data=None):
        lst = sorted(data) if data else sorted(self.ls)
        m = self.mean(lst)
        return [x - m for x in lst]

    def sample_variant(self, data=None):
        lst = data if data else self.ls
        m = self.mean(lst)
        return sum([(x - m) ** 2 for x in lst]) / (len(lst) - 1)

    def standard_deviation(self, data=None):
        lst = data if data else self.ls
        m = self.mean(lst)
        return (sum([(x - m) ** 2 for x in lst]) / (len(lst) - 1))(0.5)

    def iqr(self, data=None):
        lst = sorted(data) if data else sorted(self.ls)
        n = len(lst)
        lower, upper = (lst[0:n // 2], lst[n // 2 + 1:]) if n % 2 else (lst[0:n // 2], lst[n // 2:])
        q1 = self.median(lower)
        q3 = self.median(upper)
        return q3 - q1

    def zscore(self, data=None):
        lst = data if data else self.ls
        m = self.mean(lst)
        s = self.standard_deviation(lst)
        return [((u - m) / s) for u in lst]

    def r(self, x, y):
        n = len(x)
        zx = self.zscore(x)
        zy = self.zscore(y)
        return (round((sum([zx[i] * zy[i] for i in range(0, n)]) / (n - 1)), 4))

    def least_square_line(self, x, y):
        sum_x = sum(x)
        sum_y = sum(y)
        # sum_x2 = sum([i**2 for i in x])
        sum_xy = sum([x[i] * y[i] for i in range(len(x))])
        mean_x = self.mean(x)
        mean_y = self.mean(y)
        n = len(x)
        b1 = sum_xy - (sum_x * sum_y) / n
        b = round(b1, 4)
        a = round(mean_y - b * mean_x, 2)
        st = '+' + str(b) + 'x' if b > 0 else b + 'x'
        return [a, b, f'y = {a}{st}']

    def linear(self, a, b, x):
        return [round(a + (b * i), 2) for i in x]

    def quadratic(self, a, b1, x):
        return [round(a + (b1 * i), 4) for i in x]

    def residual(self, y, y_hat):
        return [round((y[i] - y_hat[i]), 2) for i in range(len(y))]

    def SSResid(self, y, y_hat):
        return sum([(y[i] - y_hat[i]) ** 2 for i in range(len(y))])

    def SSTo(self, y):
        y_mean = self.mean(list(y))
        return sum([(y[i] - y_mean) ** 2 for i in range(len(y))])

    def r_square(self, y, y_hat):
        # SSResid sum((y-y_hat)^2)
        SSResid = sum([(y[i] - y_hat[i]) ** 2 for i in range(len(y))])
        # SSTo sum((y-y_mean)^2)
        y_mean = self.mean(list(y))
        SSTo = sum([(y[i] - y_mean) ** 2 for i in range(len(y))])
        return round((1 - (SSResid / SSTo)) * 100, 2)
