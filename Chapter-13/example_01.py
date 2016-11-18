# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd

if __name__ == '__main__':
    ## 导入数据
    df1 = pd.read_csv('./data/refugee2008.csv')
    df2 = pd.read_csv('./data/Countries-Continents-csv.csv')
    print(df1.head())
    print(df2.head())

    ## 数据合并
    df = pd.merge(df1[['F', 'T', 'Num']], df2, left_on='T', right_on='Country')
    print(df.head())

    ## 数据分析
    # United States
    df_UnitedStates = df[df['F']=='United States'].groupby('Continent')['Num'].sum()
    print('From United States to Continent:')
    print(df_UnitedStates)

    # Canada
    df_Canada = df[df['F'] == 'Canada'].groupby('Continent')['Num'].sum()
    print('From Canada to Continent:')
    print(df_Canada)

    # Mongolia
    df_Mongolia = df[df['F'] == 'Mongolia'].groupby('Continent')['Num'].sum()
    print('From Mongolia to Continent:')
    print(df_Mongolia)

    # China
    df_China = df[df['F'] == 'China'].groupby('Continent')['Num'].sum()
    print('From China to Continent:')
    print(df_China)

    # Australia
    df_Australia = df[df['F'] == 'Australia'].groupby('Continent')['Num'].sum()
    print('From Australia to Continent:')
    print(df_Australia)

    # New Zealand
    df_NewZealand = df[df['F'] == 'New Zealand'].groupby('Continent')['Num'].sum()
    print('From New Zealand to Continent:')
    print(df_NewZealand)

    # Russia
    df_Russia = df[df['F'] == 'Russia'].groupby('Continent')['Num'].sum()
    print('From Russia to Continent:')
    print(df_Russia)