# namedtuple
# 用于创建一个自定义的tuple对象，并且规定了tuple元素的个数，并且可以用属性而不是索引来引用tuple的某个元素
# 可以用namedtuple很方便地定义一种数据类型，它具备tuple地不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple
# 类似class的简化版，Point是类名，有两个属性x和y
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(f"p.x = {p.x}     p.y = {p.y}")

# deque
# 使用list存储数据时，按索引访问元素很快，但插入和删除就很慢了，因为list是线性存储，数据量大时，插入和删除效率很低
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# deque不能在中间插入元素，只能在首位插入元素
# deque的pop()和popleft()方法可以从两端弹出元素

# defaultdict
# 使用dict时，如果引用的key不存在，就会抛出KeyError异常
# 如果希望key不存在时返回一个默认值，可以使用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'value1'
print(dd['key1'])  # 输出 'value1'
print(dd['key2'])  # 输出 'N/A'，因为key2不存在，返回默认值'N/A'

# OrdereedDict
# dict是无序的，OrderedDict是有序的dict，保持插入顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# OrderDict可以实现一个FIFO的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.capacity:
            last = self.popitem(last = False)
            print('remove:' , last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)

# ChainMap
# ChainMap可以一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但查找的时候，会按照顺序在内部的dict依次查找
from collections import ChainMap
import os, argparse

defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)

print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter
# Counter是一个简答的计数器
from collections import Counter
c = Counter('programming')
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
c.update('hello')
print(c)