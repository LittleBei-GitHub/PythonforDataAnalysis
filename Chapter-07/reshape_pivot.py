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

    # unstack操作可能会引起缺失数据
    s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
    s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
    data2 = pd.concat([s1, s2], keys=['one', 'two'])
    print(data2)
    print(data2.unstack())
    print(data2.unstack().stack())
    print(data2.unstack().stack(dropna=False))

    # 作为旋转轴的级别将会成为结果中最低的级别
    df = DataFrame({'left': result, 'right': result+5},
                   columns=pd.Index(['left', 'right'], name='side'))
    print(df)
    print(df.unstack())
    print(df.unstack('state'))
    print(df.unstack('state').stack('side'))

    ## 将‘长格式’旋转为‘宽格式’
    ldata = DataFrame({'data': ['1959-03-31', '1959-03-31', '1959-03-31', '1959-06-31',
                                '1959-06-31', '1959-06-31', '1959-09-31', '1959-09-31',
                                '1959-09-31', '1959-12-31'],
                       'item': ['realgdo', 'infl', 'unemp', 'realgdo', 'infl', 'unemp',
                                'realgdo', 'infl', 'unemp','realgdo'],
                       'value': np.random.randn(10)})
    print(ldata)

    print(ldata.pivot('data', 'item', 'value'))
    ldata['value2'] = np.random.randn(10)
    print(ldata)
    print(ldata.pivot('data', 'item')) # 忽略最后一个参数则会得到一个带有层出化的DataFrame

    # pivot变化等价于以下操作
    unstacked = ldata.set_index(['data', 'item']).unstack('item') # set_index 创建层次化索引
    print(unstacked)