from employee import Employee
import pytest

@pytest.fixture
def employee_create():
    code_man = Employee('xi', 'long', 7000)
    return code_man

def test_give_default_raise(employee_create):
    # 注意使用的参数是装饰夹具的函数名(即形参)
    # 而不是实际返回
    # 这一点个正常函数的形参使用类似
    employee_create.give_raise()
    assert employee_create.salary == 12000

def test_give_custom_raise(employee_create):
    employee_create.give_raise(3000)
    assert employee_create.salary == 10000
