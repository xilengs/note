names = ['Bob', 'Alice', 'Jack', 'Amm']
for name in names:
    print(name)
    print(f"Hello, {name}, how are you?")

vehicles = ['Honda motorcycle', 'Benz', 'BMW', 'aircraft']
for vehicle in vehicles:
    print(f"I would like to own a {vehicle}")

# pop 可以删除列表中任意位置的元素
print(vehicles)
print(vehicles.pop(1))
print(vehicles)

# remove() 方法只删除第一个指定的值，如果要删除的值可能在列表中出现多次，就需要使用循环，确保每个值都被删除
