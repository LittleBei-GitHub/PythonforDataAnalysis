# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 合并数据集
    # 数据库风格的DataFrame合并
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'c'],
                     'data2': range(3)})
    print(df1)
    print(df2)
    print(pd.merge(df1, df2)) # 未指定要连接的列名，默认使用重叠的列明
    print(pd.merge(df1, df2, on='key')) # 指定连接的列名
    print(pd.merge(df1, df2, how='outer'))

    # 合并两个列名不同的对象
    df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1:': range(7)})
    df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                     'data2': range(3)})
    print(pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='outer'))

    # 多对多的合并(笛卡尔积)
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                     'data1': range(6)})
    df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                     'data2': range(5)})
    print(df1)
    print(df2)
    print(pd.merge(df1, df2, on='key', how='left'))
    print(pd.merge(df1, df2, on='key', how='inner'))

    # 根据多个键进行合并
    left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                      'key2': ['one', 'two', 'one'],
                      'lval': [1, 2, 3]})
    right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                       'key2': ['one', 'one', 'one', 'two'],
                       'rval': [4, 5, 6, 7]})
    print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

    # 对重复列名的处理
    print(pd.merge(left, right, on='key1'))
    print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))

    ## 索引上的合并
    left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                       'value': range(6)})
    right1 = DataFrame({'group_val': [3.5, 7],}, index=['a', 'b'])
    print(left1)
    print(right1)
    print(pd.merge(left1, right1, left_on='key', right_index=True))

    # 层次化索引的连接
    lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                       'key2': [2000, 2001, 2002, 2001, 2002],
                       'data': np.arange(5)})
    righth = DataFrame(np.arange(12).reshape((6, 2)),
                       index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                              [2001, 2000, 2000, 2002, 2001, 2002]],
                       columns=['event1', 'event2'])
    print(lefth)
    print(righth)
    print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
    print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))

    # 同时使用合并双方的索引
    left2 = DataFrame([[1, 2], [3, 4], [5, 6]],
                      index=['a', 'b', 'e'],
                      columns=['Ohio', 'Nevada'])
    right2 = DataFrame([[7, 8], [9, 10], [11, 12], [13, 14]],
                       index=['b', 'c', 'd', 'e'],
                       columns=['Missouri', 'Alabama'])
    print(left2)
    print(right2)
    print(pd.merge(left2, right2, left_index=True, right_index=True,  how='outer'))

    ## DataFrame的join方法(实现快速的索引连接)
    print(left2.join(right2, how='outer'))
    print(left1.join(right1, on='key'))

    # 实现多个DataFrame的连接
    another = DataFrame([[7, 8], [9, 10], [11, 12], [16, 17]],
                        index=['a', 'c', 'e', 'f'],
                        columns=['New York', 'Oregon'])
    print(left2.join([right2, another]))
    print(left2.join([right2, another], how='outer'))