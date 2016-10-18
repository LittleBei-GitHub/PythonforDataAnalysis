# coding=utf-8

import numpy as np
# 随机数生成
if __name__ == '__main__':
    print('标准正态分布：')
    samples = np.random.normal(size=(4, 4))
    print(samples)

    print('均匀分布：')
    print(np.random.rand(10))
    print(np.random.uniform())

    print('随机漫步：')
    position = 0
    walk = [position]
    steps = 100
    for i in xrange(steps):
        step = 1 if np.random.randint(0, 2) else -1
        position += step
        walk.append(position)
    print(walk)

    draws = np.random.randint(0, 2, size=100)  # size表示生成的随机序列的大小
    print(draws)
    steps = np.where(draws>0, 1, -1)
    walk = steps.cumsum()
    print(walk)
    print(walk.min())
    print(walk.max())

    print('一次模拟多个随机漫步：')
    draws = np.random.randint(0, 2, size=(5, 100))
    print(draws)
    steps = np.where(draws>0, 1, -1)
    walks = steps.cumsum(1) # 以列的方式进行累加
    print(walks)
    print(walks.min())
    print(walks.max())