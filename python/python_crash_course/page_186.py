from pathlib import Path 
import json

# 10.1
def enter_number(file_name):
    """存储用户最喜欢的数字"""
    path = Path(file_name)
    if path.exists():
        with open(file_name, 'w') as f:
            number = input('Enter a number you like: ')
            json.dump(number, f, ensure_ascii=False, indent=4)
    else:
        print(f'The file {file_name} does not exist.')

def read_number(file_name):
    """读取用户最喜欢的数字"""
    path = Path(file_name)
    if path.exists():
        with open(file_name, 'r') as f:
            number = json.load(f)
            print(f'Your favorite number is {number}.')
    else:
        print(f'The file {file_name} does not exist.')

for i in range(3):
    enter_number('number.json')
    read_number('number.json')

    