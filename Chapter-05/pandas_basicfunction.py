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

    # DataFrame索引、选取和过滤
    print('DataFrame索引、选取和过滤:')
    data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    print(data)
    print(data['two'])
    print(data[['two', 'one']])
    print(data[:2]) # 通过切片的方式访问
    print(data[data['three']>5]) # 通过布尔索引的方式访问
    print(data<5)
    data[data<5] = 0
    print(data)

    print(data.ix['Ohio']) # 访问行
    print(data.ix[0])

    print(data.ix['Colorado', ['two', 'three']]) # 访问行、列
    print(data.ix[['Colorado', 'Utah'], ['two', 'three']])
    print(data.ix[['Colorado', 'Utah'], [1, 2]])
    print(data.ix[:'Utah', 'two'])
    print(data.ix[data.three>5, :3])

    ## 算术运算和数据对齐
    # Series算术运算和数据对齐
    s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
    s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
    print(s1+s2)

    # DataFrame算术运算和数据对齐
    df1 = DataFrame(np.arange(9).reshape((3, 3)),
                    columns=['b', 'c', 'd'],
                    index=['Ohio', 'Texas', 'Colorado'])
    df2 = DataFrame(np.arange(12).reshape((4, 3)),
                    columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print(df1)
    print(df2)
    print(df1+df2)

    # 在算术方法中填充值
    df1 = DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))
    df2 = DataFrame(np.arange(20).reshape((4, 5)), columns=list('abcde'))
    print(df1)
    print(df2)
    print(df1+df2)
    print(df1.add(df2, fill_value = 0))
    print(df1.reindex(columns=df2.columns, fill_value=0))

    ##DataFrame和Series之间的运算
    print('numpy上的广播：')
    arr = np.arange(12).reshape((3, 4))
    print(arr)
    print(arr[0])
    print(arr-arr[0]) # 这就是广播

    print('Series和DataFrame的广播：')
    frame = DataFrame(np.arange(12).reshape((4, 3)),
                    columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    series = frame.ix[0]
    print(frame)
    print(series)
    print(frame-series) # 匹配列在行上广播，算术运算会将Series的索引匹配到DataFrame的列

    series2 = Series(range(3), index=['b', 'e', 'f'])
    print(frame+series2) # 如果某个索引值在DataFrame的列或Series的索引上找不见，则以NaN代替

    series3 = frame['d']
    print(frame)
    print(series3)
    print(frame.sub(series3, axis=0)) # 匹配行在列上广播,必须使用算术运算方法

    ## 函数应用和映射
    frame = DataFrame(np.random.randn(4, 3),
                      columns=list('bde'),
                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print(frame)
    print(np.abs(frame)) # numpy的通用方法
    f = lambda x : x.max() - x.min()

    # 数组级的
    print(frame.apply(f)) # DataFrame的apply方法
    print(frame.apply(f, axis=1))
    def f(x):
        return Series([x.min(), x.max()], index=['min', 'max'])
    print(frame.apply(f))

    # 元素级的
    format = lambda x : '%.2f' % x
    print(frame.applymap(format)) # DataFrame的applymap方法

    # Series元素级
    print(frame['e'].map(format))

    ## 排名和排序
    #排序
    # Series
    obj = Series(range(4), index=['d', 'a', 'b', 'c'])
    print(obj.sort_index())

    obj = Series([4, 7, -3, 2])
    print(obj.order()) # 按值对Series进行排序

    obj = Series([4, np.nan, 7, np.nan, -3, 2])
    print(obj.order())

    # DataFrame
    frame = DataFrame(np.arange(8).reshape((2, 4)),
                      index=['three', 'one'],
                      columns=['d', 'a', 'b', 'c'])
    print(frame.sort_index())  # 按行索引排序
    print(frame.sort_index(axis=1)) # 按列索引排序
    print(frame.sort_index(axis=1, ascending=False)) # 按列索引降序排列

    frame = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
    print(frame)
    print(frame.sort_index(by='b')) # 对DataFrame的列元素进行排序
    print(frame.sort_index(by=['a', 'b']))

    # 排名
    # Series
    obj = Series([7, -5, 7, 4, 2, 0, 4])
    print(obj.rank())
    print(obj.rank(method='first'))
    print(obj.rank(method='max', ascending=False))

    # DataFrame
    frame = DataFrame({'b':[4.3, 7, -3, 2],
                       'a':[0, 1, 0, 1],
                       'c':[-2, 5, 8, -2.5]})
    print(frame)
    print(frame.rank(axis=1))
    print(frame.rank(axis=0))

    ## 带有重复制的抽索引
    # Series
    obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
    print(obj)
    print(obj.index.is_unique)
    print(obj['a'])
    print(obj['c'])

    # DataFrame
    df = DataFrame(np.random.randn(4, 3),
                   index=['a', 'a', 'b', 'b'])
    print(df)
    print(df.ix['b'])