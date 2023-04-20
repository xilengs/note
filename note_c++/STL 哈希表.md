## STL 哈希表

```c++
#include<unordered_map> //头文件
```

1. 声明

   ```c++
   unordered_map<elemType_1,elemType_2> var_name;
   unordered_map<int,int> m;
   ```

2. 初始化

   ```c++
   //通过初始化列表元素初始化
   unordered_map<int,int> hmap{ {1,2},{2,3},{3,4} };
   unordered_map<int,int> hmap{ { {1,2},{2,3},{3,4} } ,3};
   //通过下标添加元素
   hmap[1] = 2;
   hmap[4] = 4;
   //通过insert()函数来添加元素
   hmap.insert({3,5});
   //赋值构造，通过其他已经初始化的哈希表来初始化新的表
   unordered_map<int,int> hmap{ {1,2},{2,3},{3,4} };
   unordered_map<int,int> hmap1(hmap);
   ```

3. 常用函数

   ```c++
   //begin()函数:该函数返回一个指向哈希表开始位置的迭代器
   unordered_map<int,int>::iterator iter = hmap.begin();
   
   
   //end()函数:作用于begin()相同，返回一个指向哈希表结尾位置的下一个元素的迭代器
   unordered_map<int,int>::iterator iter = hmap.end();
   
   
   //cbegin() 和 cend()：这两个函数的功能和begin()与end()的功能相同，唯一的区别是cbegin()和cend()是面向不可变的哈希表
   const unordered_map<int, int> hmap{ {1,10},{2,12},{3,13} };
   unordered_map<int, int>::const_iterator iter_b = hmap.cbegin(); //注意这里的迭代器也要是不可变的const_iterator迭代器
   unordered_map<int, int>::const_iterator iter_e = hmap.cend();
   
   
   //empty()函数：判断哈希表是否为空，空则返回true，非空返回false
   bool isEmpty = hmap.empty();
   
   
   //size()函数：返回哈希表的大小
   int size = hmap.size();
   
   
   //erase()函数： 删除某个位置的元素，或者删除某个位置开始到某个位置结束这一范围内的元素， 或者传入key值删除键值对
   unordered_map<int, int> hmap{ {1,10},{2,12},{3,13} };
   unordered_map<int, int>::iterator iter_begin = hmap.begin();
   unordered_map<int, int>::iterator iter_end = hmap.end();
   hmap.erase(iter_begin);  //删除开始位置的元素
   hmap.erase(iter_begin, iter_end); //删除开始位置和结束位置之间的元素
   hmap.erase(3); //删除key==3的键值对
   
   
   //at()函数：根据key查找哈希表中的元素
   unordered_map<int, int> hmap{ {1,10},{2,12},{3,13} };
   int elem = hmap.at(3);
   
   
   //clear()函数：清空哈希表中的元素
   hmap.clear();
   
   
   //find()函数：以key作为参数寻找哈希表中的元素，如果哈希表中存在该key值则返回该位置上的迭代器，否则返回哈希表最后一个元素下一位置上的迭代器
   unordered_map<int, int> hmap{ {1,10},{2,12},{3,13} };
   unordered_map<int, int>::iterator iter;
   iter = hmap.find(2); //返回key==2的迭代器，可以通过iter->second访问该key对应的元素
   if(iter != hmap.end())  
       cout << iter->second;
   
   
   //bucket()函数：以key寻找哈希表中该元素的储存的bucket编号（unordered_map的源码是基于拉链式的哈希表，所以是通过一个个bucket存储元素）
   int pos = hmap.bucket(key);
   
   
   //bucket_count()函数：该函数返回哈希表中存在的存储桶总数（一个存储桶可以用来存放多个元素，也可以不存放元素，并且bucket的个数大于等于元素个数）
   int count = hmap.bucket_count();
   
   
   //count()函数： 统计某个key值对应的元素个数， 因为unordered_map不允许重复元素，所以返回值为0或1
   int count = hmap.count(key);
   
   
   //哈希表的遍历: 通过迭代器遍历
   unordered_map<int, int> hmap{ {1,10},{2,12},{3,13} };
   unordered_map<int, int>::iterator iter = hmap.begin();
   for( ; iter != hmap.end(); iter++){
    cout << "key: " <<  iter->first  << "value: " <<  iter->second <<endl;
   }
   //or
   for(auto x : hmap)
   {
   	cout << x.first << " " << x.second << endl;
   }
   ```

   