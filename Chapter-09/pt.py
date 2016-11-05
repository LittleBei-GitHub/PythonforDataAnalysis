# coding=utf-8

from pandas import DataFrame, Series
import  pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 透视表和交叉表
    # pivot_table默认是mean
    tips = pd.read_csv('./data/tips.csv')
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    print(tips.head())

    print(pd.pivot_table(tips, index=['sex', 'smoker']))
    print(pd.pivot_table(tips, values=['tip_pct', 'size'], index=['sex', 'day'],columns=['smoker']))
    print(pd.pivot_table(tips, values=['tip_pct', 'size'], index=['sex', 'day'],columns=['smoker'], margins=True))

    # 给pivot_table传入其他函数
    print(pd.pivot_table(tips, index=['sex', 'smoker'], columns='day', aggfunc=len, margins=True))

    # 填充
    print(pd.pivot_table(tips, values=['size'], index=['time', 'sex', 'smoker'], columns='day', aggfunc='sum', fill_value=0))

    ## 交叉表
    print(pd.crosstab([tips.time, tips.day], tips.smoker, margins=True))