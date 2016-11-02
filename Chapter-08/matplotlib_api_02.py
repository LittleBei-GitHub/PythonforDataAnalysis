# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    ## 颜色、标记和线型
    fig = plt.figure()

    # 绘制绿色曲线
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(np.arange(30), np.arange(30) + 3 * np.random.randn(30), 'g--')
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(np.arange(30), np.arange(30) + 3 * np.random.randn(30), linestyle='--', color='g')

    # 添加标记
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(np.random.randn(30).cumsum(), 'ko--')
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
    plt.show()