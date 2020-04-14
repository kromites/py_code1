import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从该文件获取日期,最低最高气温
filename = 'death_valley_2014.csv'

with open(filename) as f:
    # reader处理文件以逗号分隔的第一行数据，并将每项数据作为元素存储在列表中
    reader = csv.reader(f)
    # next 返回文件的下一行数据，一次next是代表返回一行
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     # enumerate ： 索引和值 这行代码是返回第一行的所有数据项并用index标记
    #     print(index, column_header)
    dates = []
    highs = []
    lows = []
    # 提取第一列日期和第二列最高温度的数据
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing_data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 几个曲线就plot几次
    # alpha = 0 , 1 , 0.5 : 完全透明， 完全不透明(default)， 介于两者之间
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # fill_between: 两条曲线之间的着色
    plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)
    plt.title("Daily high temperatures-2014\nDeath Valley, CA", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

