# coding=utf-8

import numpy as np

if __name__ == '__main__':
    print('通用函数：快速的元素级数组函数')
    arr = np.arange(10)
    print(arr)
    print(np.sqrt(arr))
    print(np.exp(arr))

    x = np.random.randn(8)
    y = np.random.randn(8)
    print(x)
    print(y)
    print(np.maximum(x, y))  # 元素级最大值

    arr = np.random.randn(7) *5
    print(arr)
    arrModf = np.modf(arr)
    print(arrModf)
    print(arrModf[0])
    print(arrModf[1])