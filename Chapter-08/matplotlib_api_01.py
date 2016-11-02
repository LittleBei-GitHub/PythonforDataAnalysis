# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    ## Figure 和 Subplot
    # matplotlib的图像都位于Fig
    fig = plt.figure()
    # 不能通过空figure绘图，必须用add_subplot创建一个或多个subplot
    ax1 = fig.add_subplot(2, 2, 1)   # 选中4个subplot中的第一个，编号是从1开始
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)

    # 会在最后一个subplot上绘制
    plt.plot(np.random.randn(50).cumsum(), 'k--')

    # 在各自的subplot里面绘制
    _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
    ax2 = ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))

    # 创建subplot更为简便的方式
    fig, axes = plt.subplots(2, 2)
    for i in range(2):
        for j in range(2):
            axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
    # 去除各个subplot之间的空隙
    plt.subplots_adjust(wspace=0, hspace=0)

    ## 颜色、标记和线型
    ax = fig.add_subplot(111)
    ax.plot(np.arange(30), np.arange(30)+3*np.random.randn(30), 'g--')
    plt.show()