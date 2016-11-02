# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 刻度、标签和图例
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(np.random.randn(1000).cumsum())
    ax.set_xticks([0, 250, 500, 750, 1000])
    ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
    ax.set_title('my first matplotlib plot')
    ax.set_xlabel('stages')

    # 添加图例
    ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')
    ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two')
    ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
    ax.legend(loc='best')
    plt.show()