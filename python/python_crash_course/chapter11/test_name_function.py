from name_function import get_formatted_name

# 测试文件必须以test_开头
def test_first_last_name():
    """测试能否正常输出人名"""
    formatted_name = get_formatted_name('Janis', 'Joplin')
    formatted_name_middle = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Janis Joplin'
    assert formatted_name_middle == 'Wolfgang Amadeus Mozart'
