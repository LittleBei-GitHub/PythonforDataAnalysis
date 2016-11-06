# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import pytz

if __name__ == '__main__':
    ## 时区处理
    print(pytz.common_timezones[-5:])

    # 从pytz中获取时区对象
    print(pytz.timezone('US/Eastern'))

    ## 本地化和转换
    rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
    ts = Series(np.random.randn(len(rng)), index=rng)
    print(ts)
    print(ts.index.tz)

    # 生成数据范围时可以加上一个时区集
    print(pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC'))

    # 从单纯到本地化的转换
    ts_utc = ts.tz_localize('UTC')
    print(ts_utc)
    print(ts_utc.index)

    # 用tz_convert将其转换到别的时区
    print(ts_utc.tz_convert('US/Eastern'))

    ## 操作时区意识型Timestamp对象
    stamp = pd.Timestamp('2011-03-12 04:00')
    print(stamp)
    stamp_utc = stamp.tz_localize('utc')
    print(stamp_utc.tz_convert('US/Eastern'))

    # 创建Timestamp时可以传入一个时区
    stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
    print(stamp_moscow)

    print(stamp_utc.value)
    print(stamp_utc.tz_convert('US/Eastern').value)

    ## 不同时区之间的运算
    rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
    ts = Series(np.random.randn(len(rng)), index=rng)
    print(ts)

    ts1 = ts[:7].tz_localize('Europe/London')
    ts2 = ts1[2:].tz_convert('Europe/Moscow')
    result = ts1 + ts2
    print(result.index)