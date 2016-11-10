# coding=utf-8

from pandas import Series
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

    ## 间接排序
    # argsort
    values = np.array([5, 0, 1, 3, 2])
    indexer = values.argsort()
    print(indexer)
    print(values[indexer])

    arr = np.random.randn(3, 5)
    arr[0] = values
    print(arr[:, arr[0].argsort()])

    # lexsort
    first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])
    last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
    sorter = np.lexsort((first_name, last_name))
    print(sorter)
    print(zip(last_name[sorter], first_name[sorter]))

    ## 其他排序算法
    values = np.array(['2:first', '2:second', '1:first', '1:second', '1:third'])
    key = np.array([2, 2, 1, 1, 1])
    indexer = key.argsort(kind='mergesort')
    print(indexer)
    print(values.take(indexer))

    ## 在有序数组中查找元素
    arr = np.array([0, 1, 7, 12, 15])
    print(arr.searchsorted(9))
    print(arr.searchsorted([0, 8, 11, 16]))

    arr = np.array([0, 0, 0, 1, 1, 1, 1])
    print(arr.searchsorted([0, 1]))
    print(arr.searchsorted([0, 1], side='right'))

    data = np.floor(np.random.uniform(0, 10000, size=50))
    bins = np.array([0, 100, 1000, 5000, 10000])
    print(data)
    labels = bins.searchsorted(data)
    print(labels)

    print(Series(data).groupby(labels).mean())

    print(np.digitize(data, bins))