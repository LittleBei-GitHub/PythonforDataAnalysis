# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 重采样及频率转换
    rng = pd.date_range('1/1/2000', periods=100, freq='D')
    ts = Series(np.random.randn(len(rng)), index=rng)
    print(rng)

    print(ts.resample('M', how='mean'))
    print(ts.resample('M', how='mean', kind='period'))

    # 降采样
    rng = pd.date_range('1/1/2000', periods=12, freq='T')
    ts = Series(np.arange(12), index=rng)

    print(rng)

    print(ts.resample('5min').sum())

    # 使区间左闭合
    print(ts.resample('5min', closed='left').sum())

    # 用面元左边界对其标记
    print(ts.resample('5min', closed='left', label='left').sum())

    # 移位
    print(ts.resample('5min', loffset='-1s').sum())

    ## OHLC重采样
    print(ts.resample('5min', how='ohlc'))

    ## 通过groupby进行重采样
    rng = pd.date_range('1/1/2000', periods=100, freq='D')
    ts = Series(np.arange(100), index=rng)

    print(ts.groupby(lambda x : x.month).mean())
    print(ts.groupby(lambda x : x.weekday).mean())

    ## 升采样和插值
    frame = DataFrame(np.random.randn(2, 4),
                      index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                      columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print(frame)

    df_daily = frame.resample('D')
    print(df_daily)

    # 填充
    print(frame.resample('D', fill_method='ffill'))

    # 指定填充的时期数
    print(frame.resample('D', fill_method='ffill', limit=2))

    ## 通过时期进行重采样
    frame = DataFrame(np.random.randn(24, 4),
                      index=pd.period_range('1-2000', '12-2001', freq='M'),
                      columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print(frame)
    annual_frame = frame.resample('A-DEC').mean()
    print(annual_frame)

    print(annual_frame.resample('Q-DEC', fill_method='ffill'))