import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print("kiểm tra kích thước bằng shape ", arr.shape)

print("kiểu dữ liệu mảng arr: ", arr.dtype)

arrfloat = arr.astype(float)
print("mảng sau khi chuyển sang dữ liệu float: ", arrfloat)

arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("kích thước mảng 2 chiều 3x3: ", arr2.shape)
print("kiểu dữ liệu mảng arr2: ", arr2.dtype)


arr2float = arr2.astype(float)
print("mảng sau khi chuyển sang dữ liệu float: ", arr2float)

