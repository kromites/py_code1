import requests

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

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\n Selected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])

