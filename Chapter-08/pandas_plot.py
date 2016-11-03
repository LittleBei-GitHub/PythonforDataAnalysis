# coding=utf-8

from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    ### pandas中的绘图
    ## 线型图
    # Series
    s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
    s.plot()
    plt.show()

    # DataFrame
    df = DataFrame(np.random.randn(10, 4).cumsum(0),
                   columns=['A', 'B', 'C', 'D'],
                   index=np.arange(0, 100, 10))
    df.plot()
    plt.show()

    ## 柱状图
    fig, axes = plt.subplots(2, 1)
    data = Series(np.random.randn(16), index=list('abcdefjhigklmnop'))
    data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
    data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
    plt.show()

    df = DataFrame(np.random.randn(6, 4),
                   index=['one', 'two', 'three', 'four', 'five', 'six'],
                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
    df.plot(kind='bar')
    plt.show()

    tips = pd.read_csv('./data/tips.csv')
    # party_counts = pd.crosstab(tips.day, tips.size)
    # print(party_counts)
    # party_counts = party_counts.ix[:, 2:5]
    # party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
    # print(party_pcts)
    # party_pcts.plot(kind='bar', stacked=True)
    # plt.show()

    ## 直方图和密度图
    tips['tip_pct'] = tips['tip']/tips['total_bill']
    tips['tip_pct'].hist(bins=50)
    plt.show()
    tips['tip_pct'].plot(kind='kde')
    plt.show()

    ## 散布图
    macro = pd.read_csv('./data/macrodata.csv')
    data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
    trans_data = np.log(data).diff().dropna()
    print(trans_data[-5:])
    plt.scatter(trans_data['m1'], trans_data['unemp'])
    plt.show()

    pd.scatter_matrix(trans_data, diagonal='kde', alpha=0.3)
    plt.show()