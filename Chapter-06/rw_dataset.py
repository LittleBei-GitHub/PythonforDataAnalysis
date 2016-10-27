# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import pandas.io.sql as sql
import numpy as np
import sqlite3
# import pymongo
import requests, json

if __name__ == '__main__':
    ## 使用数据库
    # 创建数据库表
    query = """
    create table test(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
    """
    con = sqlite3.connect(':memory:')
    con.execute(query)
    con.commit()

    # 插入数据
    data = [('Atlanta', 'Georgia', 1.25, 6),
            ('Tallahassee', 'Florida', 2.6, 3),
            ('Sacramento', 'California', 1.7, 5)]
    sqlString = 'insert into test VALUES(?, ?, ?, ?)'
    con.executemany(sqlString, data)

    # 将数据加载到DataFrame中
    cursor = con.execute('select * from test')
    rows = cursor.fetchall()
    sqlDF = DataFrame(rows, columns=zip(*cursor.description)[0])
    print(sqlDF)

    # 使用pandas简化数据加载到DataFrame的流程
    sqlDF2 = sql.read_sql('select * from test', con)
    print(type(sqlDF2))
    print(sqlDF2)

    ## 存取MongoDB中的数据
    # con = pymongo.Connection('localhost', port=27017)
    # tweets = con.db.tweets
    # url = 'http://search.twitter.com/search.json?q=python%20pandas'
    # data = json.loads(requests.get(url).text)
    # for tweet in data['results']:
    #     tweets.save(tweet)
    # cursor = tweets.find({'from_user': 'wesmckinn'})
    # tweet_fiels = ['created_at', 'from_user', 'id', 'text']
    # result = DataFrame(list(cursor), columns=tweet_fiels)