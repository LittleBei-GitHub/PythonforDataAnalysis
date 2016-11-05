# coding=utf-8

from pandas import DataFrame, Series
import  pandas as pd
import numpy as np

def peak_to_peak(arr):
    return arr.max() - arr.min()

if __name__ == '__main__':
    ## 数据聚合
    df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})
    print(df)

    # 计算样本分位数
    print(df.groupby('key1')['data1'].quantile(0.9))

    # 自定义函数
    print(df.groupby('key1').agg(peak_to_peak))

    #
    print(df.groupby('key1').describe())

    ### 小费例子
    tips = pd.read_csv('./data/tips.csv')
    tips['tip_pct'] = tips['tip']/tips['total_bill']
    print(tips.head())

    ## 面向列的多函数应用
    grouped = tips.groupby(['sex', 'smoker'])
    grouped_pct = grouped['tip_pct']
    print(grouped_pct.agg('mean'))

    # 传入一组函数或函数名,多函数
    print(grouped_pct.agg(['mean', 'std', peak_to_peak]))

    # 自定义分组后的列名
    print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))

    # 定义一组应用于全部列的函数，多列多函数
    functions = ['count', 'mean', 'max']
    result = grouped['tip_pct', 'total_bill'].agg(functions)
    print(result)

    print(result['tip_pct'])

    # 传入带有自定义名称的元组列表
    ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
    print(grouped['tip_pct', 'total_bill'].agg(ftuples))

    # 对不同的列应用不同的函数
    print(grouped.agg({'tip': np.max, 'size': 'sum'}))
    print(grouped.agg({'tip': [('aggmax', np.max)], 'size': [('aggsum', 'sum')]}))  # 加个列明
    print(grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
                       'size': 'sum'}))

    # 以‘无索引’的形式返回聚合数据
    print(tips.groupby(['sex', 'smoker']).mean())
    print(tips.groupby(['sex', 'smoker'], as_index=False).mean())