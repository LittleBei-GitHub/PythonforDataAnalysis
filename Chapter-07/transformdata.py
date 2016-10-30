# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ###  数据转换
    ## 移除重复数据
    data = DataFrame({'k1': ['one']*3+['two']*4,
                      'k2': [1, 1, 2, 3, 3 ,4, 4]})
    print(data)
    print(data.duplicated())
    print(data.drop_duplicates())

    # 移除指定列的重复项
    print(data.drop_duplicates(['k1']))
    print(data.drop_duplicates(['k1', 'k2']))

    # duplicated drop_duplicates 默认保留的是第一个出现的值组合，传入take_last=True则保留最后一个
    data['v1'] = range(7)
    print(data)
    print(data.drop_duplicates(['k1', 'k2']))
    print(data.drop_duplicates(['k1', 'k2'], take_last=True))

    ## 利用函数或映射进行数据转换
    data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'pastrami', 'corned beef',
                               'Bacon', 'Pastrami', 'honey ham', 'nova lox'],
                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
    print(data)

    meat_to_animal = {'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow',
                      'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}
    print(meat_to_animal)

    data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
    print(data)

    print(data['food'].map(lambda x : meat_to_animal[str.lower(x)]))

    ## 替换值
    data = Series([1, -999, 2, -999, -1000, 3])
    print(data)
    print(data.replace(-999, np.nan))

    # 一次替换多个值
    print(data.replace([-999, -1000], np.nan))

    # 不同值进行不同的替换
    print(data.replace([-999, -1000], [np.nan, 0]))
    print(data.replace({-999: np.nan, -1000: 0}))  # 也可以使用字典类型的参数

    ## 重命名轴索引
    data = DataFrame(np.arange(12).reshape((3, 4)),
                     index=['Ohio', 'Colorado', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    print(data)

    print(data.index.map(str.lower))
    print(data)
    data.index = data.index.map(str.upper)
    print(data)

    print(data.rename(index=str.title, columns=str.upper))

    # rename结合字典类型对象实现对部分轴标签的更新
    print(data.rename(index={'OHIO': 'INDIANA'},
                      columns={'three': 'peekaboo'}))

    # 使用rename对DataFrame就地修改
    print(data)
    data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
    print(data)

    ## 离散化和面元划分
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    bins = [18, 25, 35, 60, 100]
    cats = pd.cut(ages, bins)
    print(cats.labels)
    print(cats.levels)
    print(pd.value_counts(cats))

    #  修改开闭端
    cats2 = pd.cut(ages, bins, right=False)
    print(cats2.labels)
    print(cats2.levels)
    print(pd.value_counts(cats2))

    # 设置面元名称
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    print(pd.cut(ages, bins, labels=group_names))

    # 传入面元数而不是确切的边界
    data = np.random.randn(20)
    print(pd.cut(data, 4, precision=2))

    # 使用qcut切分
    data = np.random.randn(1000)
    cats = pd.qcut(data, 4)
    print(cats)
    print(pd.value_counts(cats))

    # qcut 设置自定义的分位数
    cats  =pd.qcut(data, [0, 0.1, 0.5, 0.9, 1])
    print(cats)
    print(pd.value_counts(cats))

    ## 检测和过滤异常值
    np.random.seed(12345)
    data = DataFrame(np.random.randn(1000, 4))
    print(data.describe())

    # 某列中绝对值大小超过3的值
    col = data[3]
    print(col[np.abs(col)>3])

    # 选出全部绝对值超过3的值
    print(data[(np.abs(data)>3).any(1)])

    # 将值限制在区间-3到3之间
    data[np.abs(data)>3] = np.sign(data)*3
    print(data.describe())