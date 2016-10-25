# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# 测试
if __name__ == '__main__':
    string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
    print(string_data)
    print(string_data.isnull())
    string_data[0] = None # python内置的None值也会被当作NaN来处理
    print(string_data.isnull())
    print(string_data.notnull())

    ## 滤除缺失数据
    # Series
    data = Series([1, np.nan, 3.5, np.nan, 7])
    print(data)
    print(data.dropna())
    print(data[data.notnull()]) # 通过布尔索引达到相同的效果

    # DataFrame
    data = DataFrame([[1., 6.5, 3.],
                      [1., np.nan, np.nan],
                      [np.nan, np.nan, np.nan, np.nan],
                      [np.nan, 6.5, 3.]])
    print(data)
    print(data.dropna()) # 默认丢弃含有NaN的行
    print(data.dropna(how='all')) # 丢弃全部都是NaN的行

    data[4] = np.nan
    print(data)
    print(data.dropna(axis=1)) # 丢弃列
    print(data.dropna(axis=1, how='all'))

    df = DataFrame(np.random.randn(7,3))
    df.ix[:4, 1] = np.nan
    df.ix[:2, 2] = np.nan
    print(df)
    print(df.dropna())
    print(df.dropna(thresh=3))

    ## 填充缺失数据
    print(df.fillna(0))

    print(df.fillna({1:0.5, 2:-1})) # 通过字典实现对不同列不同值的填充

    dfInplace = df.fillna(0, inplace=True)
    print(dfInplace) # fillna默认返回新对象，但也可以对现有对象进行就地修改
    print(df)

    df = DataFrame(np.random.randn(6,3))
    print(df)
    df.ix[2:, 1] = np.nan
    df.ix[3:, 2] = np.nan
    print(df)
    print(df.fillna(method='ffill'))
    print(df.fillna(method='ffill', limit=2))

    data = Series([1., np.nan, 3.5, np.nan, 7])
    print(data.fillna(data.mean()))