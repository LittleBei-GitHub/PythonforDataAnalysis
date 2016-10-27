# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 合并数据集
    # 数据库风格的DataFrame合并
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'c'],
                     'data2': range(3)})
    print(df1)
    print(df2)
    print(pd.merge(df1, df2)) # 未指定要连接的列名，默认使用重叠的列明
    print(pd.merge(df1, df2, on='key')) # 指定连接的列名