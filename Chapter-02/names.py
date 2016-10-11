# coding=utf-8

from pandas import *
import pandas as pd
import matplotlib.pylab as plt

## 美国新生婴儿的名字
# 读取数据
names_1880 = pd.read_csv('data/names/yob1880.txt', names=['name', 'sex','births'])
#names_1880['year'] = 1880

# 该年度不同性别的出生总计
total_births_by_sex = names_1880.groupby('sex').births.sum()

# 将所有数据都装到一个DataFrame中
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'data/names/yob'+str(year)+'.txt'
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)

# 插入一个prop列，用于存放指定名字的婴儿数相对于总出生数的比例
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

# 统计不同年份的男女出生数量
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# 检查这个分组总计值是否接近于1
boolean_flag = np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

## 对每个sex/year组合取出其前1000个名字
def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
top1000 = names.groupby(['year', 'sex']).apply(get_top1000)

## 分析命名趋势
# 将1000个名字分为男女两部分
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
# 生成一张按照year和name统计的总出生数透视表
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Marry', 'Marilyn']]
#subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
# plt.show()

# 计算1000个最流行的名字所占额比例
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)

## 名字中最后一个字母的变革
get_last_letter = lambda x : x[-1]
last_letters = names.name.map(get_last_letter)
#last_letters.name = 'last_letter'
names['last_letters'] = last_letters
table = names.pivot_table('births', index='last_letters', columns=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
letter_prop = subtable/subtable.sum().astype(float)
# 生成一张各年度个性别的条形图
# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

# 创建完整的表
letter_prop = table/table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T

# 绘制出dny_ts的图
dny_ts.plot()

print('读取数据：')
print(names_1880[:5])
print('年度不同性别的出生总计:')
print(total_births_by_sex)
print('讲所有数据整合到单个DataFrame中：')
print(names[:10])
print('统计不同年份的男女出生数量:')
print(total_births.tail()) #tail()查看最后的五行
print('插入一个prop列，用于存放指定名字的婴儿数相对于总出生数的比例：')
print(names[:5])
print(boolean_flag)
print('对每个sex/year组合取出其前1000个名字：')
print(top1000[:10])
print('生成一张按照year和name统计的总出生数透视表：')
print(subset[:10])
# print(plt.show())
print('计算1000个最流行的名字所占额比例：')
print(table)
print('名字中最后一个字母的变革：')
print(last_letters[:10])
print(subtable.head())
print(subtable.sum())
print(letter_prop.head())
#print(plt.show())
print(dny_ts.head())
print(plt.show())