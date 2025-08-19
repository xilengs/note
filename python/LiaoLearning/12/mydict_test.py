import unittest

from torch.utils.hipify.hipify_python import value

from mydict import Dict

# 以test开头的就是测试方法，不以test开头的方法不被认为是测试方法，测试时不会被执行
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # 测试当访问不存在的字典键时，是否抛出异常
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('SetUp...')

    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest.main()