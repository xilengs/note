def get_formatted_name(first, last, middle=''):
    """生成格式规范的姓名"""
    if middle:
        return f"{first} {middle} {last}".title()
    else:
        return f"{first} {last}".title()
    # full_name = f"{first} {last}"
    # return full_name.title()
