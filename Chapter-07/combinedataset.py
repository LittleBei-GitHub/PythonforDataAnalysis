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

    ## 轴向连接
    arr = np.arange(12).reshape((3, 4))
    print(arr)
    print(np.concatenate([arr, arr], axis=1))
    print(np.concatenate([arr, arr], axis=0))

    # Series
    s1 = Series([0, 1], index=['a', 'b'])
    s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
    s3 = Series([5, 6], index=['f', 'g'])
    print(pd.concat([s1, s2, s3])) # 默认情况，cancat是在axis=0上工作的

    print(pd.concat([s1, s2, s3], axis=1)) # 当axis=1时，返回DataFrame
    s4 = pd.concat([s1*5, s3])
    print(s4)
    print(pd.concat([s1, s4]))
    print(pd.concat([s1, s4], axis=1))
    print(pd.concat([s1, s4], axis=1, join='inner'))
    print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))

    result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three']) # 当axis=0时，keys为分块的索引
    print(result)
    print(result.unstack())

    print(pd.concat([s1, s2, s3], axis=1))
    print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])) # 当axis=1时， keys是DataFrame的头

    # DataFrame
    df1 = DataFrame(np.arange(6).reshape(3, 2),
                    index=['a', 'b', 'c'],
                    columns=['one', 'two'])
    df2 = DataFrame(5+np.arange(4).reshape(2, 2),
                    index=['a', 'c'],
                    columns=['three', 'four'])
    print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
    print(pd.concat({'level1': df1, 'level2': df2}, axis=1))

    print(pd.concat({'level1': df1, 'level2': df2}, axis=1, names=['upper', 'lower'])) # 用于管理层次化索引创建方式的参数

    df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
    df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
    print(df1)
    print(df2)
    print(pd.concat([df1, df2]))
    print(pd.concat([df1, df2], ignore_index=True))

    ## 合并重叠数据(用参数对象中的数据为调用者对象中的缺失数据打补丁)
    a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
               index=['f', 'e', 'd', 'c', 'b','a'])
    b = Series(np.arange(len(a)), dtype=np.float64,
               index=['f', 'e', 'd', 'c', 'b', 'a'])
    print(b[:-2].combine_first(a[2:]))

    df1 = DataFrame({'a': [1, np.nan, 5, np.nan],
                     'b': [np.nan, 2, np.nan, 6],
                     'c': range(2, 18, 4)})
    df2 = DataFrame({'a': [5, 4, np.nan, 3, 7],
                     'b': [np.nan, 3, 4, 6, 8]})
    print(df1)
    print(df2)
    print(df1.combine_first(df2))
    print(df2.combine_first(df1))