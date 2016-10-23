# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import pandas.io.data as web
import numpy as np

if __name__ == '__main__':
    df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                   index=['a', 'b', 'c', 'd'],
                   columns=['one', 'two'])
    print(df)
    print(df.sum()) # 默认按列求和
    print(df.sum(axis=1)) # 按行求和

    print(df.mean(axis=1, skipna=False)) # 按行求平均值
    print(df.values)

    # 间接统计
    print(df.idxmax()) # 返回最大值的索引

    # 累积
    print(df.cumsum())

    # 一次性产生多个统计
    print(df.describe())

    obj = Series(['a', 'a', 'b', 'c']*4)
    print(obj)
    print(obj.describe())
    print(obj.values)

    ## 相关系数与协方差
    all_data = {}
    for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
        all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    # print(all_data)
    price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
    print(price.tail())
    volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
    print(volume.tail())

    returns = price.pct_change()
    print(returns.tail())

    # Series
    print('相关系数：')
    print(returns.MSFT.corr(returns.IBM))

    print('协方差：')
    print(returns.MSFT.cov(returns.IBM))

    # DataFrame
    print('相关系数：')
    print(returns.corr())

    print('协方差矩阵：')
    print(returns.cov())

    print(returns.corrwith(returns.IBM)) # 计算一个DataFrame的列跟另一个Series的相关系数

    print(returns.corrwith(volume)) # 计算一个DataFrame的列跟另一个DataFrame的相关系数，计算时按照列名匹配

    ## 唯一值、值计数以及成员资格
    # Series
    obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    print(obj)
    print(obj.unique())
    print(obj.unique().sort())

    print(obj.value_counts())
    print(pd.value_counts(obj.values, sort=False)) # value_counts是一个顶级pandas方法

    print(obj[obj.isin(['b', 'c'])])

    # DataFrame
    data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                      'Qu2': [2, 3, 1, 2, 3],
                      'Qu3': [1, 5, 2, 4 ,4]})
    print(data)
    result = data.apply(pd.value_counts).fillna(0)
    print(result)