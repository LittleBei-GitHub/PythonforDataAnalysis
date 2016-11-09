# coding=utf-8

import numpy as np

if __name__ == '__main__':
    ### Numpy 数据类型体系
    ints = np.ones(10, dtype=np.int)
    floats = np.ones(10, dtype=np.float32)
    print(np.issubdtype(ints.dtype, np.integer))
    print(np.issubdtype(floats.dtype, np.float))

    # 查看某个dtype的mro方法
    print(np.float64.mro())

    ### 高级数组操作
    ## 数组重塑
    arr = np.arange(8)
    print(arr)
    print(arr.reshape((2, 4)))
    print(arr.reshape((2, 4)).reshape((4, 2)))

    # 作为参数形状的其中一维可以是-1，它表示维度的大小由数据本身推断而来
    arr = np.arange(15)
    print(arr.reshape((5, -1)))

    # 数组的shape属性是一个元组，所以它可以被传入reshape
    other_arr = np.ones((3, 5))
    print(other_arr.shape)
    print(arr.reshape(other_arr.shape))

    # 扁平化
    arr = np.arange(15).reshape((5, 3))
    print(arr)
    print(arr.ravel())
    print(arr.flatten())  # flatten与ravel类似，只不过flatten返回数据的副本

    ## C和Fortran顺序(行优先和列优先)
    arr = np.arange(12).reshape((3, 4))
    print(arr)
    print(arr.ravel())
    print(arr.ravel('F'))
    arr = arr.ravel()
    print(arr)
    print(arr.reshape((4, 3), order='C'))
    print(arr.reshape((4, 3), order='F'))

    ## 数组的合并和拆分
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])

    print(np.concatenate([arr1, arr2], axis=0))
    print(np.concatenate([arr1, arr2], axis=1))

    print(np.vstack((arr1, arr2)))
    print(np.hstack((arr1, arr2)))

    arr = np.random.randn(5, 2)
    print(arr)
    first, second, third = np.split(arr, [1, 3])
    print(first)
    print(second)
    print(third)

    ## 堆叠辅助类
    arr = np.arange(6)
    arr1 = arr.reshape((3, 2))
    arr2 = np.random.randn(3, 2)
    print(arr1)
    print(arr2)
    print(np.r_[arr1, arr2])
    print(np.c_[np.r_[arr1, arr2], arr])

    # 将切片翻译为数组
    print(np.c_[1:6, -10:-5])

    ## 元素的重复操作
    # repeat
    arr = np.arange(3)
    print(arr.repeat(3))
    print(arr.repeat([2, 3, 4]))

    arr = np.random.randn(2, 2)
    print(arr.repeat(2, axis=0))
    print(arr.repeat([2, 3], axis=0))
    print(arr.repeat([2, 3], axis=1))

    # tile
    print(np.tile(arr, 2))
    print(np.tile(arr, (1, 2)))
    print(np.tile(arr, (2, 1)))
    print(np.tile(arr, (3, 2)))

    ## 花式索引的等价函数
    arr = np.arange(10)*100
    inds = [7, 1, 2, 6]
    print(arr)
    print(arr[inds])
    print(arr.take(inds))
    arr.put(inds, 42)
    print(arr)
    arr.put(inds, [40, 41, 42, 43])
    print(arr)

    inds = [2, 0, 2, 1]
    arr  =np.random.randn(2, 4)
    print(arr)
    print(arr.take(inds, axis=1))