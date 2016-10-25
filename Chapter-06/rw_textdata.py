# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    df1 = pd.read_csv('./data/ex1.csv')
    print(df1)
    df2 = pd.read_table('./data/ex1.csv', sep=',')
    print(df2)

    #无列名
    df3 = pd.read_csv('./data/ex2.csv', header=None) # 默认分配列名
    print(df3)

    df4 = pd.read_csv('./data/ex2.csv', names=['a', 'b', 'c', 'd', 'message']) # 自定义列名
    print(df4)

    # 指定索引
    names = ['a', 'b', 'c', 'd', 'message']
    print(pd.read_csv('./data/ex2.csv', names=names, index_col='message'))

    # 将多个列做成一个层次化索引
    parsed = pd.read_csv('./data/csv_mindex.csv', index_col=['key1', 'key2'])
    print(parsed)

    # 使用正则表达式做分隔符(适用情况，各个字段由数量不定的空白符分隔)
    result = pd.read_table('./data/ex3.txt', sep='\s+')
    print(result)

    # 跳过文件中的一些行
    print(pd.read_csv('./data/ex4.csv', skiprows=[0, 2, 3]))

    # 缺失值
    result = pd.read_csv('./data/ex5.csv')
    print(result)
    print(pd.isnull(result))
    print(pd.read_csv('./data/ex5.csv', na_values=['NULL']))

    sentinels = {'message':['foo', 'NA'], 'something':['two', 'one']} # 指定各列中把哪些元素替换成NaN
    print(pd.read_csv('./data/ex5.csv', na_values=sentinels))
