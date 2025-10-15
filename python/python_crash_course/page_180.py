# 10.6 & 10.7
def sum_numbers():
    total = 0
    while True:
        print('Enter two numbers to add them together.')
        print('Enter "q" to quit.')
        num1 = input('First number: ')
        if num1 == 'q':
            break
        num2 = input('Second number: ')
        if num2 == 'q':
            break
        try:
            total += num1 + num2
        except ValueError:
            print('Invalid input. Please enter numeric values.')
        else:
            print(f'{num1} + {num2} = {total}')

# sum_numbers()

# 10.8
def greet_pet(file_name, pet):
    try:
        with open(file_name, encoding='utf-8') as f:
            for pet_name in f:
                print(f'Hello, {pet_name.strip()}! You are a great {pet.title()}!')
    except FileNotFoundError:
        # print(f'Sorry, the file {file_name} does not exist.')
        # 静默处理
        pass

greet_pet('cats.txt', 'cat')
greet_pet('dogs.txt', 'dog')

    