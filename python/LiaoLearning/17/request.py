# requests, python的第三方库，处理URL资源非常方便
import requests

r = requests.get('https://www.bilibili.com/')
print(r.status_code)
print(r.text)

# 对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.bilibili.com/search', params = {'q': 'python', 'cat': '1001'})
print(r.url)
# requests自动检测编码，可以用encoding属性查看：
print(r.encoding)
# 无论响应式文本还是二进制内容，都可以用content属性获得bytes对象：
print(r.content)
# requests的方便之处在于对于特定类型的响应，例如JSON可以直接获取：
r = requests.get('https://wttr.in/Beijing?format=j1')
print(r.json())
