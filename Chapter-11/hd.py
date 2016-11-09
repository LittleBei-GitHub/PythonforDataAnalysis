# coding=utf-8

from pandas import DataFrame, Series
from datetime import time
import pandas as pd
import numpy as np
import pandas.io.data as web
if __name__ == '__main__':
    ## 数据规整
    s1 = Series(range(3), index=['a', 'b', 'c'])
    s2 = Series(range(4), index=['d', 'b', 'c', 'e'])
    s3 = Series(range(3), index=['f', 'a', 'c'])

    print(DataFrame({'one': s1, 'two': s2, 'three': s3}))
    print(DataFrame({'one': s1, 'two': s2, 'three': s3}, index=list('face')))

    ## 频率不同的时间序列的运算
    ts1 = Series(np.random.randn(3),
                 index=pd.date_range('2012-6-13', periods=3, freq='W-WED'))
    print(ts1)
    print(ts1.resample('B'))
    print(ts1.resample('B', fill_method='ffill'))

    dates = pd.DatetimeIndex(['2012-6-12', '2012-6-17', '2012-6-18',
                              '2012-6-21', '2012-6-22', '2012-6-29'])
    ts2 = Series(np.random.randn(6), index=dates)
    print(ts2)
    print(ts1)
    print(ts1.reindex(ts2.index, method='ffill'))
    print(ts2+ts1.reindex(ts2.index, method='ffill'))

    ## 使用Period
    gdp = Series([1.78, 1.94, 2.08, 2.01, 2.15, 2.31, 2.46],
                 index=pd.period_range('1984Q2', periods=7, freq='Q-SEP'))

    infl = Series([0.025, 0.045, 0.037, 0.04],
                  index=pd.period_range('1982', periods=4, freq='A-DEC'))
    print(gdp)
    print(infl)
    infl_q = infl.asfreq('Q-SEP', how='end').reindex(gdp.index, method='ffill')
    print(infl_q)

    ## 时间和最当前数据选取
    rng = pd.date_range('2012-06-01 09:30', '2012-06-01 15:39', freq='T')
    rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 4)])
    ts = Series(np.arange(len(rng), dtype=float), index=rng)
    print(ts)

    # 抽取特定时间点上的值
    print(ts[time(10, 0)])
    print(ts.at_time(time(10, 0)))

    # 抽取某个时间段上的点
    print(ts.between_time(time(10, 0), time(10, 1)))

    # 抽取某个时间点之前最后出现的那个值
    indexer = np.sort(np.random.permutation(len(ts))[700:])
    irr_ts = ts.copy()
    irr_ts[indexer] = np.nan
    print(irr_ts['2012-06-01 09:50' : '2012-06-01 10:00'])
    selection = pd.date_range('2012-06-01 10:00', periods=4, freq='B')
    print(selection)
    print(irr_ts.asof(selection))

    ## 拼接多个数据源
    # 使用concat连接
    data1 = DataFrame(np.ones((6, 3), dtype=float),
                      columns=['a', 'b', 'c'],
                      index=pd.date_range('6/12/2012', periods=6))
    data2 = DataFrame(np.ones((6, 3), dtype=float),
                      columns=['a', 'b', 'c'],
                      index=pd.date_range('6/12/2012', periods=6))
    print(data1)
    print(data2)

    spliced = pd.concat([data1.ix[:'2012-06-14'], data2.ix['2012-06-15':]])
    print(spliced)

    data2 = DataFrame(np.ones((6, 4), dtype=float)*2,
                      columns=['a', 'b', 'c', 'd'],
                      index=pd.date_range('6/13/2012', periods=6))
    spliced = pd.concat([data1.ix[:'2012-06-14'], data2.ix['2012-06-15':]])
    print(spliced)

    # combine_first引入合并点之前的数据
    # 由于data2没有关于2012-06-12的数据，所以那一天被填空
    spliced_filled = spliced.combine_first(data2)
    print(spliced_filled)

    # DataFrame的update方法，也可以实现就地更新
    # 如果只想填充空洞，则必须传入overwrite=False
    spliced.update(data2, overwrite=False)
    print(spliced)

    # 利用DataFrame的索引机制
    cp_spliced = spliced.copy()
    cp_spliced[['a', 'c']] = data1[['a', 'c']]
    print(cp_spliced)

    ## 收益指数和累积收益
    price = web.get_data_yahoo('AAPL', '2011-01-01')['Adj Close']
    print(price[-5:])