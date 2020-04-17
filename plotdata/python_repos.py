import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# status_code是表示请求完的状态码 eg:200
print("Status Code:", r.status_code)

# 将API响应存储(json形式)在一个变量中
response_dict = r.json()
#  10054 这个错误 是爬取时次数过多
# 处理结果
print("Total Repositories:", response_dict['total_count'])
# 探索仓库信息
repo_dicts = response_dict['items']
print("Repositories Returned:", len(repo_dicts))
names, stars, plot_dicts = [], [], []
# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
for repo_dict in repo_dicts:
    # print("\n Selected information about first repository:")
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
# my_config 里面包含pygal的图表所有设定参数
my_config = pygal.Config()
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False     # 隐藏图表中水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'

chart.add('', plot_dicts)       # 这个add是指鼠标放在bar上显示的数据参数
chart.render_to_file('python_repos.svg')