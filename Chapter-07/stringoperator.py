# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import re

if __name__ == '__main__':
    ## 字符串对象方法
    val = 'a, b, guido'
    print(val.split(','))
    pieces = [x.strip() for x in val.split(',')]
    print(pieces)

    # 使用字符串‘：：’连接pieces
    print('::'.join(pieces))

    # 子串定位
    print('guido' in val)
    print(val.index(','))
    print(val.find('a'))
    print(val.find(':'))

    # 字符串统计
    print(val.count(','))

    # 字符串替换
    print(val.replace(',', '::'))
    print(val.replace(',', ''))

    ## 正则表达式
    text = 'foo  bar\t baz    \t qux'
    print(re.split('\s+', text))

    # 自编译regex
    regex = re.compile('\s+')
    print(regex.split(text))

    # 匹配
    print(regex.findall(text))

    # findall search match
    text = """
    Dave dave@google.com
    Steve steve@google.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
    pattern = r'[A-Z0-9._%+-]+@[A-Z0-9._]+\.[A-Z]{2,4}'
    regex = re.compile(pattern=pattern, flags=re.IGNORECASE) # re.IGNORECASE忽略正则表达式对大小写的敏感

    print(regex.findall(text))

    s = regex.search(text)

    print(text[s.start(): s.end()])
    print(regex.match(text))

    # 替换
    print(regex.sub('REDACTED', text))

    # 将邮箱地址分成3个部分：用户名 域名 后缀名
    pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9._]+)\.([A-Z]{2,4})'
    regex = re.compile(pattern, flags=re.IGNORECASE)

    m = regex.match('wesm@bright.net')
    print(m.groups())

    print(regex.findall(text))

    print(regex.sub(r'username: \1, domain: \2, suffix: \3', text))

    ## pandas 中矢量化的字符串函数
    data = {'Dave': 'dave@google.com',
            'Steve': 'steve@google.com',
            'Rob': 'rob@gmail.com',
            'Wes': np.nan}
    data = Series(data)
    print(data)
    print(data.isnull())

    # 跳过NA值得字符串操作方法
    print(data.str.contains('gmail'))
    print(data.str.findall(pattern, flags=re.IGNORECASE))

    # 获取矢量化元素的操作
    matches = data.str.match(pattern, flags=re.IGNORECASE)
    print(matches)
    print(matches.str.get(1))
    print(matches.str[1])