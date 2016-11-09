# coding=utf-8

import numpy as np

if __name__ == '__main__':
    ## 广播
    arr = np.arange(5)
    print(arr)
    print(arr*4)

    # 减去列的平均值
    arr = np.random.randn(4, 3)
    print(arr.mean(0))
    demeaned = arr - arr.mean(0)
    print(demeaned)
    print(demeaned.mean(0))

    row_means = arr.mean(1)
    print(row_means)
    demeaned = arr - row_means.reshape((4, 1))
    print(demeaned)
    print(demeaned.mean(1))

    ## 沿其他轴广播
    arr = np.random.randn(3, 4, 5)
    depth_means = arr.mean(2)
    demeaned = arr - depth_means[:, :, np.newaxis]
    print(demeaned.mean(2))

    ## 通过官博设置数组的值
    arr = np.zeros((4, 3))
    arr[:] = 5
    print(arr)
    col = np.array([1.28, -0.42, 0.44, 1.6])
    print(col[:, np.newaxis])
    arr[:] = col[:, np.newaxis]
    print(arr)
    arr[:2] = [[-1.37], [0.509]]
    print(arr)