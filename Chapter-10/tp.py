# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import pytz

if __name__ == '__main__':
    ## 时期及算术运算
    p = pd.Period(2007, freq='A-DEC')
    print(p)
    print(p+5)
    print(p-2)

    # 穿件规则的时间范围
    rng = pd.period_range('1/1/2000', '6/30/2000', freq='M')
    print(rng)

    #
    print(Series(np.random.randn(6), index=rng))

    ## 时间的频率转换
    p = pd.Period('2007', freq='A-DEC')
    print(p.asfreq('M', how='start'))
    print(p.asfreq('M', how='end'))