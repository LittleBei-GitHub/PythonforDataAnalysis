# coding=utf-8

from pandas import DataFrame
import pandas as pd

# pandas数据类型DataFrame
if __name__ == '__main__':
    print('构建DataFrame数据：')
    data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year':[2000, 2001, 2002, 2001, 2002],
            'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print(frame)