# 练习
# 写一个验证Email地址的正则表达式
import re

def is_valid_email(addr):
    pattern = r'^[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.com$'
    return re.match(pattern, addr)

def test():
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print('ok')

test()