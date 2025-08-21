# datatime是python处理日期和时间的标准库

# 获取当前日期和时间
from datetime import datetime

now = datetime.now()    # 获取当前时间
print("当前日期和时间:", now)
print(type(now))  # 输出类型

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print("指定日期和时间:", dt)

# datetime转换为timestamp
# timestamp是自1970年1月1日以来的秒数
print(dt.timestamp())  # 输出时间戳
# python的timesstamp是浮点数，精确到毫秒,整数位表示秒，小数位表示毫秒

# timestamp转换为datetime
t = 1429417200.0
print("时间戳转换为datetime:", datetime.fromtimestamp(t))  # 输出datetime对象

# timestamp是一个浮点数，没有时区概念
# 而datetime是有时区概念的，上述转换是在timestamp为本地时间的前提下进行的

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print("字符串转换为datetime:", cday)

# datetime转换为str
now = datetime.now()
print("datetime转换为字符串:", now.strftime('%a, %b %d %H:%M'))

# datetime加减
# 对日期的进行加减实际上就是把datetime往后或往前计算，得到新的datetime
# 加减可以直接用+和-运算符，不过需要导入timedelta
from datetime import timedelta
now = datetime.now()
print("当前时间:", now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# 一个datetime对象有一个时区属性tzinfo，表示时区,但默认是None
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print("当前时间:", now)
dt = now.replace(tzinfo=tz_utc_8)  # 把时区设置为UTC+8:00
print("设置时区后的时间:", dt)

# 时区转换
# 先通过utcnow()获取当前的UTC时间，然后转换为指定时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print("当前UTC时间:", utc_dt)
# astimezone()方法可以把UTC时间转换为指定时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("转换为北京时间:", bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print("转换为东京时间:", tokyo_dt)

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_str = tz_str.strip('UTC').strip(':00')
    tz = timezone(timedelta(hours=int(tz_str)))

    timestamp = dt.replace(tzinfo=tz).timestamp()
    return timestamp

def test():
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

test()