# coding=utf-8

from pandas import DataFrame, Series
from datetime import time
import pandas as pd
import numpy as np
import random; random.seed(0)
import string

def rands(n):
    choices = string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in xrange(n)])

def zxcore(group):
    return (group - group.mean())/group.std()

if __name__ == '__main__':
    ## 分组变换和分析
    # 随机生成1000个股票代码
    N = 1000
    tickers = np.array([rands(5) for _ in xrange(N)])
    print(tickers)

    # 创建一个含有3列的DataFrame装这些假想的数据
    M = 500
    df = DataFrame({'Momentum': np.random.randn(M)/200 + 0.03,
                    'Value': np.random.randn(M)/200 + 0.08,
                    'ShortInterest': np.random.randn(M)/200 - 0.02},
                   index=tickers[:M])
    print(df)

    # 为这些股票创建一个行业类
    ind_names = np.array(['FINANCIAL', 'TECH'])
    sampler = np.random.randint(0, len(ind_names), N)
    industries = Series(ind_names[sampler], index=tickers,
                        name='industry')

    # 根据行业分类进行分组
    by_industry = df.groupby(industries)
    print(by_industry.mean())
    print(by_industry.describe())

    # 行业内标准化处理
    df_stand = by_industry.apply(zxcore)
    print(df_stand)
    print(df_stand.groupby(industries).agg(['mean', 'std']))

    # 行业内降序排名
    ind_rank = by_industry.rank(ascending=False)
    print(ind_rank.groupby(industries).agg(['min', 'max']))

    # 行业内排名和标准化
    print(by_industry.apply(lambda x : zxcore(x.rank())))