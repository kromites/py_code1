import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://www.hacker-news.firebaseio.com/v0/item/9884165.json'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
r = requests.get(url, headers=headers, timeout=5)
print("Status Code:", r.status_code)