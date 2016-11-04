# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})
    print(df)

    # 按key1进行分组， 并计算data1列的平均值
    print(df['data1'].groupby(df['key1']).mean())

    # 一次传入多个数据组
    means = df['data1'].groupby([df['key1'], df['key2']]).mean()
    print(means)
    print(means.unstack())

    # 分组建可以是任何长度适当的数组
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])
    print(df['data1'].groupby([states, years]).mean())

    # 将列名用作分组键
    print(df.groupby('key1').mean())
    print(df.groupby(['key1', 'key2']).mean())

    # 计算分组的大小
    print(df.groupby(['key1', 'key2']).size())

    ## 对分组进行迭代
    # 单键
    for name, group in df.groupby('key1'):
        print(name)
        print(group)
    # 多键重组
    for (k1, k2), group in df.groupby(['key1', 'key2']):
        print(k1, k2)
        print(group)
    # 将数据片段做成字典
    pieces = dict(list(df.groupby('key1')))
    print(pieces['b'])

    ## 在列上进行分组
    print(df.dtypes)
    grouped = df.groupby(df.dtypes, axis=1)
    print(dict(list(grouped)))

    ## 选取一个或一组列
    print(df['data2'].groupby([df['key1'], df['key2']]).mean())
    print(df.groupby(['key1', 'key2'])['data2'].mean())

    ## 通过字典或Series进行分组
    people = DataFrame(np.random.randn(5, 5),
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'],
                       columns=['a', 'b', 'c', 'd', 'e'])
    people.ix[2:3, ['b', 'c']] = np.nan
    print(people)

    # 给出列的映射关系
    # 字典
    mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
               'd': 'blue', 'e': 'red', 'f': 'orange'}
    by_column = people.groupby(mapping, axis=1)
    print(by_column.sum())

    # Series
    map_series = Series(mapping)
    print(map_series)
    print(people.groupby(map_series, axis=1).count())

    ## 通过函数进行分组
    print(people.groupby(len).sum())

    # 将函数与其他方式混合使用
    key_list = ['one', 'one', 'one', 'two', 'two']
    print(people.groupby([len, key_list]).min())

    ## 根据索引级别分组
    columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                         [1, 3, 5, 1, 3]],
                                        names=['cty', 'tenor'])
    hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
    print(hier_df)
    print(hier_df.groupby(level='cty', axis=1).count())