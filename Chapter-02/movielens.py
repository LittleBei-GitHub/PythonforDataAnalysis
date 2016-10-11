# coding=utf-8

from pandas import *
import pandas as pd

## 加载数据
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timetamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_table('data/movielens/users.dat', sep='::', header=None, names=unames)
ratings = pd.read_table('data/movielens/ratings.dat', sep='::', header=None, names=rnames)
movies = pd.read_table('data/movielens/movies.dat', sep='::', header=None, names=mnames)

print('验证数据是否加载成功：')
print(users[:5])
print(ratings[:5])
print(movies[:5])

## 根据性别和年龄计算某部电影的平均得分
# 合并 users、ratings 以及 movies
data = pd.merge(pd.merge(ratings, users), movies)
# pivot_table() 是pandas中的透视函数，可用于建立各种复杂的数据透视表
mean_ratings = data.pivot_table('rating', index=['title'], columns='gender', aggfunc='mean')
# 过滤掉评分数据不够250条的电影
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title[ratings_by_title>=250]
mean_ratings = mean_ratings.ix[active_titles]
# 找出女性观众最喜欢的电影
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
# 找出男性和女性观众分歧最大的电影
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')

## 找出分歧最大的电影
# 根据电影名称分组的得分数据的标准差
rating_std_by_title = data.groupby('title')['rating'].std()
# 根据active_titles进行过滤
rating_std_by_title = rating_std_by_title.ix[active_titles]
# 根据值对Series进行降序排列
#rating_std_by_title = rating_std_by_title.order(ascending='True')


print('合并数据表：')
#print(data)
print('data.ix[0]------')
print(data.ix[0])
print('(mean_ratings[:5]------')
print(mean_ratings[:5])
print('ratings_by_title[:10]------')
print(ratings_by_title[:10])
print('active_titles------')
print(active_titles)
print('mean_ratings[:5]------')
print(mean_ratings[:5])
print('top_female_ratings[:10]------')
print(top_female_ratings[:10])
print('sorted_by_diff[:15]------')
print(sorted_by_diff[:15])

print('找出分歧最大的电影：')
print('rating_std_by_title------')
print(rating_std_by_title[:10])