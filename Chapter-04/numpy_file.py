# coding=utf-8

import numpy as np

# 用于数组的文件输入输出
if __name__ == '__main__':
    print('讲数组以二进制格式保存到磁盘：')
    # 使用np.save()保存数组
    arr = np.arange(10)
    print(arr)
    np.save('data/some_array.npy', arr)
    print(np.load('data/some_array.npy'))

    # 使用np.savez()保存数组
    np.savez('data/array_archive.npz', a=arr, b=arr)
    # 会返回一个类似字典的对象
    arch = np.load('data/array_archive.npz')
    print(arch)
    print(arch['a'])
    print(arch['b'])

    print('存取文本文件：')
    arr = np.loadtxt('data/array_ex.txt', delimiter=',')
    print(arr)