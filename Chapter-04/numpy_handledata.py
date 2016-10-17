# coding=utf-8

import numpy as np

# 使用数组进行数据处理
if __name__ == '__main__':
    points = np.arange(-5, 5, 0.1)
    print(points)
    xs, ys = np.meshgrid(points, points)
    print(xs)
    print(ys)
    z = np.sqrt(xs**2 + ys**2)
    print(z)

    arr = np.arange(5)
    print(arr)
    z = np.sqrt(arr**2 + arr**2)
    print(z)

    print('将条件逻辑表述为数组运算：')
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    result = np.where(cond, xarr, yarr)
    print(result)
    # 将数组中大于0的赋值为2， 小于0的赋值为-2
    arr = np.random.randn(4, 4)
    print(arr)
    result = np.where(arr>0, 2, -2)
    print(result)
    # 只将数组中大于0的赋值为2，小于0的不用管
    result = np.where(arr>0, 2, arr)
    print(result)

    print('数学和统计方法：')
    arr = np.random.randn(5,4)
    print(arr)
    print(np.mean(arr))
    print(arr.mean())
    print(np.sum(arr))
    print(arr.sum())

    print(np.mean(arr, axis=1))
    print(arr.mean(axis=1))
    print(arr.mean(1))
    print(np.sum(arr, axis=0))
    print(arr.sum(axis=0))
    print(arr.sum(0))

    arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(arr.cumsum(0)) # 累加
    print(arr.cumprod(1)) # 累积