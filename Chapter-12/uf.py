# coding=utf-8

import numpy as np

if __name__ == '__main__':
    ### ufunc高级应用
    ## ufunc实例方法
    arr = np.arange(10)
    print(np.add.reduce(arr))
    print(arr.sum())

    arr = np.random.randn(5, 5)
    print(arr[:])
    print(arr[::2])
    print(np.logical_and.reduce(arr, axis=0))

    #
    arr = np.arange(15).reshape((3, 5))
    print(np.add.accumulate(arr, axis=1))

    # 计算两个数组的叉积
    arr = np.arange(3).repeat([1, 2, 2])
    print(np.multiply.outer(arr, np.arange(5)))

    ## 自定义ufunc
    def add_elements(x, y):
        return x+y
    add_them = np.frompyfunc(add_elements, 2, 1)
    print(add_them(np.arange(8), np.arange(8)))