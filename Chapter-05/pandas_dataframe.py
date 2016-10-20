# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd

# pandas数据类型DataFrame
if __name__ == '__main__':
    print('构建DataFrame数据：')
    data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year':[2000, 2001, 2002, 2001, 2002],
            'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print(frame)

    print('指定DateFrame的列顺序：')
    frame1 = DataFrame(data, columns=['year', 'state', 'pop'])
    print(frame1)

    print('自定索引：')
    frame2 = DataFrame(data=data, columns=['year', 'state', 'pop'], index=['one', 'two', 'three', 'four', 'five'])
    print(frame2)

    print('如果传入的列在数据中找不见，会产生NA值：')
    frame3 = DataFrame(data=data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
    print(frame3)

    print('获取DataFrame的列：')
    print(frame.columns)

    print('将DataFrame的列获取为一个Series：')
    print(frame['state'])
    print(frame.state)

    print('访问行：')
    print(frame.ix[0])
    print(frame2.ix['one'])

    print('通过赋值的方式对列元素进行修改：')
    frame3['debt'] = 16.5
    print(frame3)
    frame3['debt'] = range(5)
    print(frame3)

    print('使用Series对DataFrame的列赋值：')
    val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    print(val)
    frame3.debt = val
    print(frame3)

    print('为不存在的列赋值将会产生一个新列：')
    frame3['eastern'] = frame3.state == 'Ohio'
    print(frame3)

    print('删除列：')
    del(frame3['eastern'])
    print(frame3)

    print('嵌套字典：')
    pop = {'Nevada':{2001:2.4, 2002:2.9}, 'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
    frame4 = DataFrame(pop)
    print(frame4)
    print(frame4.T)

    print('设置index和columns的name属性：')
    frame4.index.name = 'year'
    frame4.columns.name = 'state'
    print(frame4)

    print('返回DataFrame中的数据使用values属性：')
    print(frame4.values)
    print(frame3.values)