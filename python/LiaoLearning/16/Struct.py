# struct
# 在python中，要把一个32位无符号整数变成字节，也就是4个长度的bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)
# 非常麻烦，如果换成浮点数就无能为力了
# atruct模块用于解决bytes和其他二进制数据类型的转换
import struct
# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian,也就是网络序，I表示4字节无符号整数
print(struct.pack('>I', 10240099))
# unpack把bytes变成相应的数据类型
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))