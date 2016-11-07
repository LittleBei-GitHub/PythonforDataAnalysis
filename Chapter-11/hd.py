# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

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