# base64
# base64是一种用64个字符来表示任意二进制数据的方法
# 对二进制数据进行处理，每三个字节一组，划分为四组，一组6个bit
# 这样得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
# 所以Base64会把三字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
# 如果编码的二进制数据不是3的倍数，Base64会用\x00字节在末尾补足，再在编码末尾加上1个或两个=号，表示补了多少字节，解码时，会自动删掉
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_:
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))


# 练习
# 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    if '=' in s:
        return base64.b64decode(s)
    else:
        l = 3 - len(s) % 3
        str = '=' * l
        return base64.b64decode(s + str)

def test():
    assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')

test()