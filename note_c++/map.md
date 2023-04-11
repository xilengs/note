## map

###　１.简介

map是STL的一个关联容器，它提供一对一的hash。

1. 第一个参数称为关键词（key），每个关键词只能在map中出现一次；
2. 第二个参数称为该关键词的值（value）；

map会根据key值的大小自动建立一颗红黑树，这棵树具有对数据自动排序的功能。在map内部所有数据都是有序的。

![img](https://img-blog.csdnimg.cn/img_convert/ab94f358cc379299731b9aaa4814fd47.png)

### 2.map的功能

自动建立key-value的对应。key和value可以是任意你需要的类型，包括自定义类型。

### 3.使用map

1. 包含map所在的头文件

   ```c++
   #include<map>
   ```

2. map对象是模板类，需要关键字和存储对象两个模板参数：

   ```c++
   std::map<int,string>personnel;
   ```

   这样就定义了一个用int作为索引，并拥有相关联的指向string的指针。

   为了使用方便，可以对模板类进行以下类型定义：

   ```c++
   typedef map<int,CString> UDT_MAP_INT_CSTRING;
   UDT_MAP_INT_CSTRING enumMap;
   ```

### 4.map的构造函数

```c++
 	//以下三种构造方式再构造失败时都不会提示
	//emplace只会在key值不存在的情况下构造
 	//使用移动构造
	m.emplace(make_pair(int(1),string("a")));
    //使用隐式转换构造函数,和上一个区别是这里的“a”会隐式转换成std::string
    m.emplace(make_pair(2,"b"));
    //使用模板构造
    m.emplace(3,"c");
```

