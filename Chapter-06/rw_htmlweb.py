# coding=utf-8

from pandas import DataFrame, Series
import numpy as np
import pandas as pd
import requests, json

if __name__ == '__main__':
    ## 使用HTML和Web API
    url = 'http://search.twitter.com/search.json?q=python%20pandas'
    resp = requests.get(url)
    data = json.loads(resp.text)
    print(data.keys())
    tweet_fields = ['created_at', 'from_user', 'id', 'text']
    tweets = DataFrame(data['results'], columns=tweet_fields)
    print(tweets)