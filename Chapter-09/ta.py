# coding=utf-8

from pandas import DataFrame, Series
import  pandas as pd
import numpy as np

def demean(arr):
    return arr - arr.mean()

def get_stats(group):
    return {'min': group.min(),
            'max': group.max(),
            'count': group.count(),
            'mean': group.mean()}

def top(df, n=5, column='tip_pct'):
    return df.sort_index(by=column)[-n:]

if __name__ == '__main__':
    ## 分组级运算和转换
    df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})
    print(df)

    # 为一个DataFrame添加一个用于存放索引分组的平均值的列
    k1_means = df.groupby('key1').mean().add_prefix('mean_')
    print(k1_means)
    print(pd.merge(df, k1_means, left_on='key1', right_index=True))

    people = DataFrame(np.random.randn(5, 5),
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'],
                       columns=['a', 'b', 'c', 'd', 'e'])
    people.ix[2:3, ['b', 'c']] = np.nan
    print(people)

    # transform 方法
    key = ['one', 'two', 'one', 'two', 'one']
    print(people.groupby(key).mean())
    print(people.groupby(key).transform(np.mean))
    # 自定义转换函数
    demeaned = people.groupby(key).transform(demean)
    print(demeaned)
    print(demeaned.groupby(key).mean())

    ## apply
    tips = pd.read_csv('./data/tips.csv')
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    print(tips.head())
    print(top(tips, n=6))

    print(tips.groupby('smoker').apply(top))

    # 传给apply的函数可以接受其他参数，将这些参数放在函数名后面
    print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))

    ## 禁止分组键
    print(tips.groupby('smoker', group_keys=False).apply(top))

    ## 分位数和桶分析
    # 长度相同的桶
    frame = DataFrame({'data1': np.random.randn(1000),
                       'data2': np.random.randn(1000)})
    factor = pd.cut(frame.data1, 4)
    print(factor[:10])

    grouped = frame.data2.groupby(factor)
    print(grouped.apply(get_stats).unstack())

    # 大小相同的桶
    grouping = pd.qcut(frame.data1, 10, labels=False)
    grouped = frame.data2.groupby(grouping)
    print(grouped.apply(get_stats).unstack())

    ## 用特定于分组的值填充失值
    s = Series(np.random.randn(6))
    s[::2] = np.nan
    print(s)
    print(s.fillna(s.mean()))

    ## 对不同的分组填充不同的值
    states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
    group_key = ['East']*4 + ['West']*4
    data = Series(np.random.randn(8), index=states)
    data[['Vermont', 'Nevada', 'Idaho']] = np.nan
    print(data)
    print(data.groupby(group_key).apply(lambda g : g.fillna(g.mean())))

    fill_values = {'East': 0.5, 'West': -1}
    print(data.groupby(group_key).apply(lambda g : g.fillna(fill_values[g.name])))

    ## 随机采样和排列
    # 构造一副扑克牌
    # 红桃（hearts）、黑桃（spades）、梅花（clubs）、方片（diamonds）
    suits = ['H', 'S', 'C', 'D']
    card_val = (range(1, 11) + [10]*3)*4
    base_names = ['A'] + range(2, 11) + ['J', 'Q', 'K']
    cards = []
    for suit in ['H', 'S', 'C', 'D']:
        cards.extend(str(num)+suit for num in base_names)
    deck = Series(card_val, index=cards)
    print(deck)

    # 从整副牌中抽5张
    def draw(deck, n=5):
        return deck.take(np.random.permutation(len(deck))[:n])

    print(draw(deck))

    # 从每种花色中随机抽取两张
    print(deck.groupby(lambda card : card[-1]).apply(draw, n=2))

    ## 分组加权平均数和相关系数
    df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                    'data': np.random.randn(8),
                    'weights': np.random.rand(8)})
    print(df)
    grouped = df.groupby('category')
    get_wavg = lambda g : np.average(g['data'], weights=g['weights'])
    print(grouped.apply(get_wavg))

    #
    close_px = pd.read_csv('./data/stock_px.csv', parse_dates=True, index_col=0)
    print(close_px.head())
    rets = close_px.pct_change().dropna()
    by_year = rets.groupby(lambda x : x.year)
    print(by_year.apply(lambda x : x.corrwith(x['SPX'])))