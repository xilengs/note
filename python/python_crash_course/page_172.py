import os

fn = open('guest.txt', 'a')

while True:
    name = input('Please enter your name (enter "q" to quit): ')
    if name == 'q':
        break
    fn.write(name + '\n')

fn.close()
