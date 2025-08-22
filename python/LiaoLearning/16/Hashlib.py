# python的hashlib提供了常见的哈希算法，如MD5,SHA1等等
# 哈希算法就是通过哈希函数对任意长度的数据data计算出固定长度的哈希digest
# 哈希算法是一个单向函数,计算digest=hash(data)很容易,但通过digest反推data却非常困难
# 对原始数据做一个bit的修改，都会导致计算出的哈希完全不同
import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分多次调用update()
md5_2 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())

# SHA1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# 比SHA1更安全的是SHA256和SHA512

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if user not in db:
        raise ValueError('用户不存在')
    if db[user] == calc_md5(password):
        return True
    else:
        return False

def test():
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')

test()