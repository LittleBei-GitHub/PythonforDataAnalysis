# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 重塑层次化索引
    data = DataFrame(np.arange(6).reshape((2, 3)),
                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
                     columns=pd.Index(['one', 'two', 'three'], name='number'))
    print(data)

    # 将列转换成行
    result = data.stack()
    print(result)

    # 将行转换成列
    print(result.unstack())
    print(result.unstack(0)) # 传入分层级别编号
    print(result.unstack('state')) # 传入分层级别名称