# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定地页面，然后返回HTTP的响应
# 例如，对豆瓣的一个URL进行抓取，并返回响应
from urllib import request
import gzip

url = 'https://www.bilibili.com/video/BV1BEeEzQEiv/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=8786534865b75da14ffe03249a9d363b'

req = request.Request(
    url, 
    headers={
        "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; win64; x64)"
                        "AppleWebKit/537.36 (KHTML, like Gecko)"
                        "Chorme/114.0.0.0 Safari/537.36"
    }
)

# 模仿浏览器发送GET请求，使用request对象，通过request对象添加HTTP头，就可以把请求伪装成浏览器。
with request.urlopen(req) as f:
    data = f.read()
    if f.headers.get('Content-Encoding') == 'gzip':
        data = gzip.decompress(data)
    html = data.decode('utf-8', errors='ignore')

    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

# Post
# 以POST发送一个请求，只需要把参数data以bytes形式传入
# 模拟微博登录，先读取登的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('clien_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
proxy_handler = request.ProxyHandler({'http': "http://www.example.com:3128/"})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass