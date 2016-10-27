# coding=utf-8

from pandas import DataFrame, Series
import numpy as np
import pandas as pd
import requests, json

if __name__ == '__main__':
    ## 二进制数据
    frame = pd.read_csv('./data/ex1.csv')
    print(frame)
    # frame.save('./data/frame_pickle') # 将数据持久化
    # print(pd.load('./data/frame_pickle'))

    ## 使用HDF5格式
    # store = pd.HDFStore('./data/mydata.h5')
    # store['obj1'] = frame
    # store['obj1_col'] = frame['a']
    # print(store)

    ## 读取MicrosoftExcel 文件
    xls_file = pd.ExcelFile('./data/2015.xls')
    table = xls_file.parse('Sheet1')
    print(table)