# coding=utf-8

from pandas import DataFrame, Series
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 时间序列绘图
    close_px_all = pd.read_csv('./data/stock_px.csv', parse_dates=True, index_col=0)
    close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
    close_px = close_px.resample('B', fill_method='ffill')

    close_px['AAPL'].plot()
    plot.show()

    close_px.ix['2009'].plot()
    plot.show()

    close_px['AAPL'].ix['01-2011':'03-2011'].plot()
    plot.show()

    appl_q = close_px['AAPL'].resample('Q-DEC', fill_method='ffill')
    appl_q.ix['2009':].plot()
    plot.show()