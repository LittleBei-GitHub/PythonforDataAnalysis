# coding=utf-8

import numpy as np

if __name__ == '__main__':

    data = np.array([[0.9526, -0.246, -0.8856],
                    [0.5639, 0.2379, 0.9104]])
    print(data)
    print(data*10)
    print(data+data)

    print('获取数组的行列数：')
    print(data.shape)
    print(np.shape(data))

    print('获取数组的元素数据类型：')
    print(data.dtype)

    print('创建数组：')
    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1) # np.array 会为数组推断出一个合适的数据类型
    print(arr1)
    print(arr1.dtype)

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)
    print(arr2.dtype)

    print('创建全0数组：')
    print(np.zeros(10))
    print(np.zeros((3, 6)))

    print('创建全1数组：')
    print(np.ones(4))
    print(np.ones((3, 3)))

    print('创建单位矩阵：')
    print(np.eye(2))

    print('创建一个没有具体值的数组：')
    print(np.empty((2,3)))

    print('创建等差数组：')
    print(np.arange(10))
    print(type(np.arange(10)))

    print('ndarray 的数据类型：')
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    arr2 = np.array([1, 2, 3], dtype=np.int32)
    print(arr1)
    print(arr2)

    print('转换ndarray元素的数据类型：')
    # 使用astype()方法
    print(arr1.astype(np.int32))
    numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
    print(numeric_strings)
    print(numeric_strings.astype(np.float64))

    int_arr = np.arange(10)
    calibers = np.array([.22, .270, .357, .380], dtype=np.float64)
    print(int_arr)
    print(int_arr.astype(calibers.dtype))

    print('数组与标量之间的运算：')
    arr = np.array([[1., 2., 3.],
                    [4., 5., 6.]])
    # 大小相等等的数组之间的任何算术运算都会应用到元素级
    print(arr)
    print(arr*arr)
    print(arr-arr)

    # 数组与标量之间的算术运算也会将那个标量值传播到各个元素
    print(1/arr)
    print(arr*0.5)

    print('基本的索引和切片：')
    arr = np.arange(10)
    print(arr)
    print(arr[5])
    print(arr[5:8])
    arr[5:8] = 12
    print(arr)