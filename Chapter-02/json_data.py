# coding=utf-8

import matplotlib.pylab as plt
import json
import collections as clt
import pandas as pd
import numpy as np

path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'

# json数据
print('json数据：')
print(open(path).readline())

# 将json数据转换成python字典类型
print('将json数据转换成python字典类型：')
records = [json.loads(line) for line in open(path).readlines()]
print(records[0]['tz'])

# 统计数据集中最常出现的时区
time_zones = [record['tz'] for record in records if 'tz' in record]
print(time_zones[:10])
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] =1
    return counts

def get_counts2(sequence):
    counts = clt.defaultdict(int) # 创建一个初始值均为0的字典
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print('统计时区的值：')
print(counts['America/New_York'])

# 得到前10位的时区及其计数值
def top_counts(count_dic, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dic.items()]
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[:n]

def top_counts2(sequence, n=10):
    counts = clt.Counter(sequence)
    return counts.most_common(n)

print('得到前10位的时区及其计数值：')
print(top_counts(counts))
print(top_counts2(time_zones))

# pandas中DataFrame对象的使用
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
print('pandas中DataFrame对象的使用')
print(tz_counts[:10])
# print(frame)

# 处理未知或缺失的时区
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print('处理未知或缺失的时区')
print(tz_counts[:10])

# 绘制时区图
# tz_counts[:10].plot(kind='barh', rot=0)
# plt.show()

#