from dataAndTransformations import *
import matplotlib.pyplot as plt

# subplot(columns, rows, position)

# define size of figure(10, 10) it's mean 1000px * 1000px
plt.figure(figsize=(10, 10))

# plot label (x,y)
ax1 = plt.subplot(2, 2, 1)
ax1.scatter(x, y, c='green', marker='o', alpha=1, label="x,y")
ax1.legend()
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# plot label (logx, y)
ax2 = plt.subplot(2, 2, 2)
ax2.scatter(logx, y, c='dodgerblue', marker='o', alpha=1, label="logx,y")
ax2.legend()
ax2.set_xlabel('logx')
ax2.set_ylabel('y')

# plot label (logx, logy)
ax3 = plt.subplot(2, 2, 3)
ax3.scatter(logx, logy, c='yellow', marker='o', alpha=1, label="logx,logy")
ax3.legend()
ax3.set_xlabel('logx')
ax3.set_ylabel('logy')

# plot label (1/x, 1/y)
ax4 = plt.subplot(2, 2, 4)
ax4.scatter(x1, y1, c='blue', marker='o', alpha=1, label="1/x,1/y")
ax4.legend()
ax4.set_xlabel('1/x')
ax4.set_ylabel('1/y')
# plt.show()
