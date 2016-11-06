# coding=utf-8

from datetime import datetime, timedelta
from dateutil.parser import parse
import pandas as pd

if __name__ == '__main__':
    ## 日期和时间数据类型及工具
    now = datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)

    # 给datetime加上或减去一个或多个timedelta
    start = datetime(2011, 1, 7)
    print(start)
    print(start+timedelta(12))
    print(start-2*timedelta(12))

    ## 字符串和datetime的相互转换
    stamp = datetime(2011, 1, 3)
    print(str(stamp))
    print(stamp.strftime('%Y-%m-%d'))

    # 将字符串转成datetime
    value = '2011-01-03'
    print(datetime.strptime(value, '%Y-%m-%d'))

    print(parse('2011-01-04'))
    print(parse('6/12/2011'))
    print(parse('6/12/2011', dayfirst=True))

    datestrs = ['7/6/2012', '8/6/2012']
    print(pd.to_datetime(datestrs))