# coding=utf-8

from pandas import DataFrame, Series
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd
from datetime import datetime
import pandas as pd
import numpy as np


if __name__ == '__main__':
    ## 日期的范围频率以及移动
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
             datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

    ts = Series(np.random.randn(6), index=dates)
    print(ts)

    print(ts.resample('D'))

    ## 生成日期范围
    index = pd.date_range('4/1/2012', '6/1/2012')
    print(index)

    # 只传入起始或结束日期，还得传入一个表示时间的数字
    print(pd.date_range(start='4/1/2012', periods=20))
    print(pd.date_range(end='6/1/2012', periods=20))

    # 生成要给由每月结束的日期
    print(pd.date_range('1/1/2000', '12/1/2000', freq='BM'))

    # date_range默认会保留起始和结束时间戳
    print(pd.date_range('5/2/2012 12:56:31', periods=5))

    # 产生一组被规范化到午夜的时间戳
    print(pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True))

    # 频率和日期偏移量
    hour = Hour()
    print(hour)
    four_hour = Hour(4)
    print(four_hour)

    print(pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h'))

    print(Hour(2)+Minute(30))

    print(pd.date_range('1/1/2000', periods=10, freq='1h30min'))

    ## WOM日期
    rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
    print(rng)

    ## 移动数据
    ts = Series(np.random.randn(4),
                index=pd.date_range('1/1/2000', periods=4, freq='M'))
    print(ts)

    # 对时间戳位移
    print(ts.shift(2, freq='M'))
    print(ts.shift(3, freq='D'))
    print(ts.shift(1, freq='3D'))
    print(ts.shift(1, freq='90T'))

    ## 通过偏移量对日期进行位移
    now = datetime(2011, 11, 17)
    print(now+3*Day())

    # 加的是锚点偏移量
    print(now+MonthEnd())
    print(now+MonthEnd(2))

    offset = MonthEnd()
    print(now)
    print(offset.rollforward(now))
    print(offset.rollback(now))

    # 与groupby结合
    ts  =Series(np.random.randn(20),
                index=pd.date_range('1/15/2000', periods=20, freq='4d'))
    print(ts)
    print(ts.groupby(offset.rollforward).mean())
    print(ts.resample('M', how='mean'))