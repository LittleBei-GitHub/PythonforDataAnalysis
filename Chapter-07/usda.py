# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json

if __name__ == '__main__':
    db = json.load(open('./data/foods-2011-10-03.json'))
    print(len(db))
    print(db[0].keys())
    print(db[0]['nutrients'][0])
    nutrients = DataFrame(db[0]['nutrients'])
    print(nutrients[:7])

    info_keys = ['description', 'group', 'id', 'manufacturer']
    info = DataFrame(db, columns=info_keys)
    print(info[:5])

    print(pd.value_counts(info.group)[:10])

    nutrients = []
    for rec in db:
        fnuts  =DataFrame(rec['nutrients'])
        fnuts['id'] = rec['id']
        nutrients.append(fnuts)
    nutrients = pd.concat(nutrients, ignore_index=True)

    print(nutrients)
    print(nutrients.duplicated().sum())
    nutrients = nutrients.drop_duplicates()

    col_mapping = {'description': 'food', 'group': 'fgroup'}
    info = info.rename(columns=col_mapping, copy=False)

    col_mapping = {'description': 'nutrient', 'group': 'nutgroup'}
    nutrients = nutrients.rename(columns=col_mapping, copy=False)

    ndata = pd.merge(nutrients, info, on='id', how='outer')
    print(ndata)