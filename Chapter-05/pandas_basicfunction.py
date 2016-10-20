# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# 基本功能
if __name__ == '__main__':
    ## 重新索引
    # Series重新索引
    print('Series重新索引:')
    obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    print(obj)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)
    obj3 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0.0)
    print(obj3)

    print('重新索引时的插值处理：')
    obj4 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
    print(obj4)
    obj4 = obj4.reindex(range(6), method='ffill')
    print(obj4)
    obj4 = obj4.reindex(range(6), method='bfill')
    print(obj4)

    # DataFrame重新索引
    print('DataFrame重新索引:')
    print('重新索引行：')
    frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'd', 'c'], columns=['Ohio', 'Texas', 'California'])
    print(frame)
    frame2 = frame.reindex(['a', 'b', 'c', 'd'])
    print(frame2)

    print('重新索引列：')
    frame3 = frame.reindex(columns=['Texas', 'Utah', 'California', 'Ohio'])
    print(frame3)

    print('重新索引行列：')
    frame4 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=['Texas', 'Utah', 'California', 'Ohio'])
    print(frame4)
    # frame5 = frame.reindex(index=[0, 1, 2, 3], columns=['Texas', 'Utah', 'California', 'Ohio'], method='ffill')

    ## 丢弃指定轴上的项
    # Series丢弃指定轴上的项
    print('Series丢弃指定轴上的项:')
    obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
    new_obj = obj.drop('c')
    print(new_obj)
    print(obj.drop(['d', 'c']))

    # DataFrame丢弃指定轴上的项
    print('DataFrame丢弃指定轴上的项:')
    data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    print(data)

    print('丢弃行：')
    print(data.drop('Ohio'))
    print(data.drop(['Colorado', 'Ohio']))

    print('丢弃列：')
    print(data.drop('one', axis=1))
    print(data.drop(['two', 'four'], axis=1))

    ## 索引、选取和过滤
    # Series索引、选取和过滤
    print('Series索引、选取和过滤:')
    obj = Series(np.arange(4), index=['a', 'b', 'c', 'd'])
    print(obj)
    print(obj['a'])
    print(obj[['a', 'b']])

    print(obj[1])
    print(obj[[1, 3]])

    print(obj[2:4])

    print(obj[obj<2])

    print(obj['b':'c']) # 与普通的python切片运算不同，其末端是包含的