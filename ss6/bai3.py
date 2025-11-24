import numpy as np

arr2 = np.random.randint(0,100, size=(3,3))
print("mảng: ",arr2)
print("giá trị nhỏ nhất: ", arr2.min())
print("giá trị lớn nhất: ", arr2.max())
print("tổng: ", arr2.sum())
print("trung bình: ", arr2.mean())
print("độ lệch chuẩn: ", arr2.std())

print("tổng theo cột: ", arr2.sum(axis=0))
print("trung bình theo cột: ", arr2.mean(axis=0))

print("tổng theo hàng: ", arr2.sum(axis=1))
print("trung bình theo hàng: ", arr2.mean(axis=1))




