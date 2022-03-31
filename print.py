from plot import *

# show data table
print(data_table)
print("\n")

# show predict value in data table
print(data_table_predictions)
print("\n")

# show equations
print(e1)  # label x, y
print(e2)  # label logx, y
print(e3)  # label logx, logy
print(e4, "\n")  # label 1/x, 1/y

# show r^2
print(f'r^2(x,y) = {r_square}%')
print(f'r^2(logx,y) = {r_square_x}%')
print(f'r^2(logx,logy) = {r_square_log}%')
print(f'r^2(1/x,1/y) = {r_square1}% \n')

# show se
print(f'se(x,y) = {se}')
print(f'se(logx,y) = {se_x}')
print(f'se(logx,logy) = {se_log}')
print(f'se(1/x,1/y) = {se1}\n')

# predict value where x = 25
print("Predict value (x = 25) : ", y_predict)

# show scatter plot
plt.show()
