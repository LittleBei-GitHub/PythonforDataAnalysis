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
    print('数据合并：')
    print(df.head())
    print(df[df['Continent']=='Asia'])

    ## 数据分析
    # Mongolia
    df_Mongolia = df[df['F'] == 'Mongolia'].groupby('Continent')['Num'].sum()
    print('From Mongolia to Continent:')
    print(df_Mongolia)

    # China
    df_China = df[df['F'] == 'China'].groupby('Continent')['Num'].sum()
    print('From China to Continent:')
    print(df_China)

    # Russia
    df_Russia = df[df['F'] == 'Russia'].groupby('Continent')['Num'].sum()
    print('From Russia to Continent:')
    print(df_Russia)

    ## 数据合并
    df = pd.merge(df1[['F', 'T', 'Num']], df2, left_on='F', right_on='Country')
    print('数据合并：')
    print(df.head())

    # United States
    df_UnitedStates = df[df['T'] == 'United States'].groupby('Continent')['Num'].sum()
    print('From Continent to United States:')
    print(df_UnitedStates)

    # Canada
    df_Canada = df[df['T'] == 'Canada'].groupby('Continent')['Num'].sum()
    print('From Continent to Canada:')
    print(df_Canada)

    # Australia
    df_Australia = df[df['T'] == 'Australia'].groupby('Continent')['Num'].sum()
    print('From Continent to Australia:')
    print(df_Australia)

    # New Zealand
    df_NewZealand = df[df['T'] == 'New Zealand'].groupby('Continent')['Num'].sum()
    print('From Continent to New Zealand:')
    print(df_NewZealand)