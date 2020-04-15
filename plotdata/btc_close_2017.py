from __future__ import (absolute_import, division, print_function, unicode_literals)

import math
from urllib.request import urlopen
import requests
import json
import pygal

from itertools import groupby
# 数据处理
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# # response = urlopen(json_url)
# # 读取数据
# req = requests.get(json_url)
# # req = response.read()
# # 将数据写入文件
# with open('btc_close_2017_request.json', 'w') as f:
#     f.write(req.text)
# # req.text 直接读取文件数据，返回格式是字符串
# # 加载json格式
# # file_urlib = json.loads(req)
# # print(file_urlib)
# file_requests = req.json()

# 数据分析: 1. 提取数据  2.可视化
filename = 'btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)
# 创建五个列表来存储消息
dates = []
months = []
weeks = []
weekdays = []
closes = []
for btc_dict in btc_data:
    #  这些数据都是字符串类型要转换的话如下所示
    date = btc_dict['date']
    month =int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    # print("{} is month {} week {}, {}, the close price is {} RMB".format
                                                                # (date, month, week, weekday,close))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)

# 利用Pygal对数据进行可视化处理，绘制折线图
# x_label_rotation=20: 让x轴的日期标签顺时针旋转20° ,  show_minor_x_labels=False: 不用显示所有的x轴坐标
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价(¥)"
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', closes)

# 利用对数将原本指数型折线图变成线性折线图
closes_log = [math.log10(_) for _ in closes]
line_chart.add('log收盘价', closes_log)
line_chart.render_to_file('收盘价折线图(¥).svg')


def draw_line(x_data, y_data, title, y_legend):
    """先利用sorted进行排序，再利用groupby函数进行分组"""
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month],'收盘价月日均值', '月日均值')
# line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值', '周日均值')
# line_chart_week

wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week],'收盘价星期均值', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday

with open("收盘价Dashboard.html",'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset ="utf-8"></head></html>')
    # for svg in ['收盘价折线图(¥).svg', '']