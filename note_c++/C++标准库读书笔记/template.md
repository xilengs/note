## 函数模板

```c++
template <typename AnyType>
void Swap(AnyType &a, AnyType &b)
{
    AnyType temp;
    temp = a;
    a = b;
    b = a;
}
```

第一行指出，要建立一个模板，并将类型命名为Anytype。

如果有多个原型，则编译器在选择原型时，非模板版本优先于显示具体化和模板版本，显示具体化优于使用模板生成的版本。