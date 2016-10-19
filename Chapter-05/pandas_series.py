# coding=utf-8

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# pandas数据类型Series
if __name__ == '__main__':
    print('Series:')
    print('自动创建索引：')
    obj = Series([4, 7, -5, 3])
    print(obj)
    print(obj[0])
    print(obj.values)
    print(obj.index)

    print('自定义索引：')
    obj2 = Series(data=[4, 7, -8, 3], index=['d', 'b', 'a', 'c'])
    print(obj2)
    print(obj2[2])
    print(obj2['a'])
    print(obj2[['c', 'a', 'd']])
    print(obj2.values)
    print(obj2.index)
    obj2['e'] = 0
    print(obj2)
    print(obj2[obj2>2])
    print(obj2*2)
    print(np.exp(obj2))
    print('b' in obj2)
    print('f' in obj2)
    print(4 in obj2)
    print(9 in obj2)

    print('将字典类型转换成Series类型：')
    sdata = {'a':1, 'b':2, 'c':3, 'd':4}
    print(sdata)
    obj3 = Series(sdata)
    print(obj3)

    obj4 = Series(sdata, index=['a', 'b', 'c'])
    print(obj4)

    print('检测数据的缺失：')
    print(pd.isnull(obj4))
    print(pd.notnull(obj4))

    print('Series中一个最重要的功能是在相加的时候有索引自动对齐功能：')
    obj5 = Series({'b':2, 'c':3, 'd':4, 'e':6, 'f':9})
    obj6 = obj3 + obj5
    print(obj6)
    print(obj6.notnull())

    print('Series对象本身及其索引都有一个name属性：')
    obj6.name = 'list'
    obj6.index.name = 'word'
    print(obj6)

    print('Series的索引可以通过赋值的方式修改：')
    print(obj)
    obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    print(obj)