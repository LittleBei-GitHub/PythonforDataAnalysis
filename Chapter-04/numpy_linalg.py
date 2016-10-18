# coding=utf-8

import numpy as np
import numpy.linalg as lg

# 线性代数
if __name__ == '__main__':
    print('矩阵乘法：')
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1, 7], [8, 9]])
    print(x)
    print(y)
    z = x.dot(y)
    m = np.dot(x, y)
    print(z)
    print(m)

    X = np.random.randn(5, 5)
    print(X)
    mat = X.T.dot(X)
    print(mat)
    mat_inv = np.linalg.inv(mat)
    print(mat_inv)
    print(mat.dot(mat_inv))
    q, r = np.linalg.qr(mat)
    print(r)