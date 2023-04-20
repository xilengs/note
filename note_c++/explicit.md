### explicit

禁止构造函数的隐式调用：

```c++
class Point {
public:
    int x, y;
    Point(int x = 0, int y = 0)
        : x(x), y(y) {}
};
void displayPoint(const Point& p) 
{
    cout << "(" << p.x << "," 
         << p.y << ")" << endl;
}
int main()
{
   displayPoint(1);
   point p = 1;
}
```

这里虽然displayPoint需要一个Point参数，但在输入1后，也能得到结果：
```c++
(1,0)
```

在使用关键字explicit后可以禁止这种隐式调用。