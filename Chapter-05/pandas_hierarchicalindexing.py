# coding=utf-8

from pandas import DataFrame, Series
import numpy as np
import pandas as pd

if __name__ == '__main__':
    ## 层次化索引
    # Series
    data = Series(np.random.randn(10),
                  index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    print(data)
    print(data.index)
    print(data['b'])
    print(data['b':'c'])
    print(data.ix[['b', 'c']])

    print(data[:, 2]) # 从内层取值

    print(data.unstack()) # 将Series类型的层次化数据S转换成DataFrame类型的数据
    print (data.unstack().stack())

    # DataFrame
    frame = DataFrame()
    frame = DataFrame(np.arange(12).reshape((4, 3)),
                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                      columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
    print(frame)
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print(frame)
    print(frame['Ohio'])

    print(frame.swaplevel(0, 1))
    print(frame.sortlevel(1))
    print(frame.swaplevel(0, 1).sortlevel(0))

    ## 根据级别汇总统计
    print(frame.sum(level='key2'))
    print(frame.sum(level='color', axis=1))

    frame = DataFrame({'a':range(7),
                       'b':range(7, 0, -1),
                       'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                       'd':[0, 1, 2, 0, 1, 2, 3]})
    print(frame)
    frame2 = frame.set_index(['c', 'd'])
    print(frame2)
    frame3 = frame.set_index(['c', 'd'], drop=False)
    print(frame3)

    print(frame2.reset_index())