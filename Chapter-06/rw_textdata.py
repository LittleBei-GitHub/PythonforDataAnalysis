# coding=utf-8

from lxml.html import parse
from urllib2 import urlopen
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import sys
import csv, json

if __name__ == '__main__':

    ## 读写文本格式的数据
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

    ## 逐块读取文本文件
    result = pd.read_csv('./data/ex6.csv')
    print(result)

    # 指定读取的行数
    result = pd.read_csv('./data/ex6.csv', nrows=5)
    print(result)

    # 迭代读取
    chunker = pd.read_csv('./data/ex6.csv', chunksize=100)

    tot = Series([])
    for piece in chunker:
        tot = tot.add(piece['key'].value_counts(), fill_value=0)
    tot = tot.order(ascending=False)
    print(tot[:10])

    ## 将数据写出文本格式
    # 将数据以分隔符的格式输出到文本中
    data = pd.read_csv('./data/ex5.csv')
    print(data)
    data.to_csv('./data/out.csv')

    # 使用不同的分隔符
    print(data.to_csv(sys.stdout, sep='|'))

    # 使用别的标记值替代缺失值
    print(data.to_csv(sys.stdout, na_rep='NULL'))

    # 禁用行和列的标签
    print(data.to_csv(sys.stdout, index=False, header=False))

    # 只写出一部分列
    print(data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c']))

    # Series 的to_csv的方法
    dates = pd.date_range('1/1/2000', periods=7)
    ts = Series(np.arange(7), index=dates)
    print(ts.to_csv('./data/tseries.csv'))

    # 将csv文件读取为Series
    print(Series.from_csv('./data/tseries.csv', parse_dates=True))

    ## 手工处理分隔符
    f = open('./data/ex7.csv')
    reader = csv.reader(f)
    for line in reader:
        print(line)

    lines = list(csv.reader(open('./data/ex7.csv')))
    print(lines)
    header, values = lines[0], lines[1:]
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    print(data_dict)

    ## JSON数据
    # obj = """
    # {'name': 'Wes',
    #  'places_lived': ['United States', 'Spain', 'Germany'],
    #  'pet': null,
    #  'siblings': [{'name': 'Scott', 'age': 25, 'pet': 'Zuko'},
    #               {'name': 'Katie', 'age': 33, 'pet': 'Cisco'}]
    # }
    # """
    # result = json.loads(obj)
    # print(result)

    ## XML和HTML：Web信息收集
    parsed = parse(urlopen('http://www.baidu.com'))
    doc = parsed.getroot()

    # 获取文档中的所有超链接
    links = doc.findall('.//a')
    urls = [link.get('href') for link in links]
    print(urls)