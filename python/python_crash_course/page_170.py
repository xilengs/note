# 10.1
import os

fn = open('learning_python.txt', 'r')
content = fn.read()
print('-----------------------------')
print(content)
print('-----------------------------')
content_list = content.split('\n')
for line in content_list:
    print(line)

# 9.2 
content = content.replace('Python', 'C')
print('-----------------------------')
print(content)
print('-----------------------------')

fn.close()

fn = open('output.txt', 'a')
fn.write('I love programming.\n')

fn.close()
