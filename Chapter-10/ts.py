# coding=utf-8

from datetime import datetime
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 时间序列基础
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
             datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

    ts = Series(np.random.randn(6), index=dates)
    print(ts)
    print(type(ts))
    print(ts.index)
    print(ts.index.dtype)

    print(ts[::2])
    print(ts+ts[::2])

    stamp = ts.index[0]
    print(stamp)

    ## 索引、选取、子集构造
    stamp = ts.index[2]
    print(ts)
    print(ts[stamp])

    print(ts['1/10/2011'])
    print(ts['20110110'])

    longer_ts = Series(np.random.randn(1000),
                       index=pd.date_range('1/1/2000', periods=1000))
    print(longer_ts)
    print('2001----------------------------------------------')
    print(longer_ts['2001'])
    print('2001-05-------------------------------------------')
    print(longer_ts['2001-05'])

    # 通过日期进行切片的方式只对Series有效
    print(ts[datetime(2011,1,7):])

    # 也可以使用不存在于改时间序列中的时间戳进行切片
    print(ts['1/6/2011':'1/11/2011'])

    # 使用truncate
    print(ts.truncate(after='1/9/2011'))

    # 对DataFrame进行索引
    dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
    long_df = DataFrame(np.random.randn(100, 4),
                        index=dates,
                        columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print(long_df)
    print(long_df.ix['2001-5'])

    ## 带有重复索引的时间序列
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
    dup_ts = Series(np.arange(5), index=dates)
    print(dup_ts)

    # 查看索引是否唯一
    print(dup_ts.index.is_unique)

    print(dup_ts['1/3/2000'])
    print(dup_ts['1/2/2000'])

    # 聚合
    grouped = dup_ts.groupby(level=0)
    print(grouped.mean())
    print(grouped.count())