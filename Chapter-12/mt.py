# coding=utf-8

import numpy as np

if __name__ == '__main__':
    ## NumPy的matrix类
    X = np.random.randn(4, 4)
    print(X)
    Xm = np.matrix(X)
    ym = Xm[:, 0]
    print(ym.T*Xm*ym)

    # 矩阵的逆
    print(Xm.I * Xm)