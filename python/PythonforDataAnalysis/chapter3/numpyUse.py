import numpy as np

# ndarray 的数据类型
def ndarray_dtype():
    # dtype 是一个特殊的对象, 用于描述 ndarray 中的数据类型
    arr1 = np.array([1, 2, 3.2], dtype=np.float64)
    arr2 = np.array([1, 2, 3], dtype=np.int32)

    print(f"arr1: {arr1}, arr1.dtype: {arr1.dtype}")
    print(f"arr2: {arr2}, arr2.dtype: {arr2.dtype}")

    print(f"可以通过 ndarray 的 astype 方法明确地将一个数组从一个 dtype 转换成另一个 dtype")
    int_arr1 = arr1.astype(np.int32)
    float_arr2 = arr2.astype(np.float64)
    print(f"int_arr1: {int_arr1.dtype}, int_arr1 = arr1.astype(np.int32)")
    print(f"float_arr2: {float_arr2.dtype}, float_arr2 = arr2.astype(np.float64)")
    print("将浮点数转换成整数, 则小数部分会被截取删除")
    print(f"arr1 : {arr1}\nint_arr1 = {int_arr1}")

# Numpy 数组的运算
def cal_ndarray():
    # 矢量化, 大小相等的数组之间的任何算术运算都将运算应用到元素级
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("矢量化, 大小相等的数组之间的任何算术运算都将运算应用到元素级")
    print(f"arr: {arr}\narr * arr = {arr * arr}\narr - arr = {arr - arr}")
    print("数组与标量之间的算术运算将标量值传播到各个元素")
    print(f"1 / arr = {1 / arr}\narr ** 0.5 = {arr ** 0.5}")
    arr2 = np.array([[0, 4, 1], [7, 2, 12]])
    print("size 大小相同的数组之间的比较会生成布尔值数组")
    print(f"arr2: {arr2}\narr = {arr}\narr2 > arr1 = {arr2 > arr}")

# ndarray 的切片和索引
def ndarray_slice_index():
    arr = np.arange(10)
    print(f"arr: {arr}\narr[5] = {arr[5]}\narr[5:8] = {arr[5:8]}")

    arr[5:8] = 12
    print(f"赋值：arr[5:8] = 12\n arr = {arr}")
    print("跟列表最重要的区别在于, 数组切片是原始数组的视图, 这意味这数据不会被复制, 试图上的任何修改都会直接反映到源数组上")
    arr_slice = arr[5:8]
    print(f"arr_slice = {arr_slice}")
    arr_slice[1] = 12345
    print(f"arr_slice[1] = 12345\narr_slice = {arr_slice}\narr = {arr}")


def spilt_line():
    print('-------------------------------------------------------')

if __name__ == "__main__":
    spilt_line()
    ndarray_dtype()
    spilt_line()
    cal_ndarray()
    spilt_line()
    ndarray_slice_index()
    spilt_line()