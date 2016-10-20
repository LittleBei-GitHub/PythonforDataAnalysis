# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd

# 索引对象
if __name__ == '__main__':
    obj = Series(range(3), index=['a', 'b', 'c'])
    index = obj.index
    print(index)
    print(index[1:])