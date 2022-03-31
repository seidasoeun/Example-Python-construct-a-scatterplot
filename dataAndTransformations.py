from data.data import data
from tabulate import tabulate
from _class.num import *
import numpy as np
import math

# create list of data (x, y, logx, logy, 1/x, 1/y)
n5 = Num()
x = np.array([i[0] for i in data])
y = np.array([i[1] for i in data])

logx = []
logy = []
x1 = []
y1 = []
for i in range(len(x)):
    logx.append(round(math.log(x[i], 10), 4))
    logy.append(round(math.log(y[i], 10), 4))
    x1.append(round(1 / x[i], 4))
    y1.append(round(1 / y[i], 4))

# define
# (a,b, e1, none) for label (x, y)
# (a_log, bx, e2, _x)   for label (logx, y)
# (a_logy, b_logx, e3, _log) for label (logx, logy)
# (a1, b1, e4)     for label (1/x, 1/y)

# create dta table (x, y, logx, logy, 1/x, 1/y)
data = list(zip(x, y, logx, logy, x1, y1))
data_table = tabulate(data, headers=["x", "y", "logx", "logy", "1/x", "1/y"])

# find a, b
b = findB(x, y)
a = findA(x, y, b)

bx = findB(logx, y)
a_log = findA(logx, y, bx)

b_logx = findB(logx, logy)
a_logy = findA(logx, logy, b_logx)

b1 = findB(x1, y1)
a1 = findA(x1, y1, b1)

# or we can use library numpy for find a and b
# b, a = np.poly1d(np.polyfit(x, y, deg=1))
# bx, a_log = np.poly1d(np.polyfit(logx, y, deg=1))
# b_logx, a_logy = np.poly1d(np.polyfit(logx, logy, deg=1))
# b1, a1 = np.poly1d(np.polyfit(x1, y1, deg=1))

# equations
e1 = f'y = {round(a, 4)}{"+" if b > 0 else ""}{round(b, 4)} * x'
e2 = f'y = {round(a_log, 4)}{"+" if bx > 0 else ""}{round(bx, 4)} * log(x)'
e3 = f'log(y) = {round(a_logy, 4)}{"+" if b_logx > 0 else ""}{round(b_logx, 4)} * log(x)'
e4 = f'1/y = {round(a1, 4)}{"+" if b1 > 0 else ""}{round(b1, 4)} * 1/x'

# predict values
n = len(data)
predict_value = n5.quadratic(a, b, x)
predict_value_x = n5.quadratic(a_log, bx, logx)
predict_value_log = n5.quadratic(a_logy, b_logx, logx)
predict_value1 = n5.quadratic(a1, b1, x1)
data_predictions = list(zip(predict_value, predict_value_x, predict_value_log, predict_value1))
data_table_predictions = tabulate(data_predictions, headers=["Predict Value(x,y)", "Predict Value(logx,y)",
                                                             "Predict Value(logx,logy)", "Predict Value(1/x,1/y"])

# SSResid (Residual sum of squares)
SSResid = n5.SSResid(y, predict_value)
SSResid_x = n5.SSResid(y, predict_value_x)
SSResid_log = n5.SSResid(logy, predict_value_log)
SSResid1 = n5.SSResid(y1, predict_value1)

# SSTo (Total sum of squares)
SSTo = n5.SSTo(y)
SSTo_x = n5.SSTo(y)
SSTo_log = n5.SSTo(logy)
SSTo1 = n5.SSTo(y1)

# r_square (r^2)
r_square = round((1 - (SSResid / SSTo)) * 100, 2)
r_square_x = round((1 - (SSResid_x / SSTo_x)) * 100, 2)
r_square_log = round((1 - (SSResid_log / SSTo_log)) * 100, 2)
r_square1 = round((1 - (SSResid1 / SSTo1)) * 100, 2)

# se
se = round(math.sqrt(SSResid / (n - 2)), 4)
se_x = round(math.sqrt(SSResid_x / (n - 2)), 4)
se_log = round(math.sqrt(SSResid_log / (n - 2)), 4)
se1 = round(math.sqrt(SSResid1 / (n - 2)), 4)

# Use the least-squares regression line to make predictions where x = 25m
log_y_hat = a_logy + (b_logx * math.log(25, 10))  # logy = a + b * logx
y_predict = round(pow(10, log_y_hat), 4)  # y = 10 ^ logy
