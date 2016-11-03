# coding=utf-8

from datetime import datetime
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 图形的绘制
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
    circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
    pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)

    # 将块对象添加到subplot中
    ax.add_patch(rect)
    ax.add_patch(circ)
    ax.add_patch(pgon)

    plt.show()


    ## 将图标保存到文件
    plt.savefig('./data/figpath.svg')

    # savefig并非一定要写入磁盘，也可以写入任何文件型的对象
    buffer = StringIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()