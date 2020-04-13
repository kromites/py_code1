import pygal
from die import Die

# 使用到的模板为 pygal
# pygal是一个用于生成SVG格式图片的python第三方库，具有十分酷炫的绘图功能.
# pygal具有交互性：将鼠标点到图中任意一个条形，都能看到与之相关联的数据
# 可视化问题一般分三步
# 一： 创建模型
# 二： 分析模型结果
# 三： 进行可视化处理

# 创建一个D6
die_1 = Die()
die_2 = Die(10)

# 将掷骰子的结果放入列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果放入列表中
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    # 六面各个面出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化 条形图Bar
hist = pygal.Bar()
# 设置条形图的各个参数
hist.title = "Results of rolling one D6 and one D10 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)  # add一系列值添加到图标中，D6是按钮名称，点击即传值
hist.render_to_file('die_visual.svg')   # 扩展名必须为svg
