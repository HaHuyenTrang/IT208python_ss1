import numpy as np

arr2 = np.random.randint(1,100, size=(4,4))
print("mảng: ", arr2)

print("tổng hàng: ",arr2.sum(axis=0))
print("tổng cột: ",arr2.sum(axis=1))
print("trung bình hàng: ",arr2.mean(axis=0))
print("trung bình cột: ",arr2.mean(axis=1))
print("độ lệch chuẩn hàng: ",arr2.std(axis=0))
print("độ lệch chuẩn cột: ",arr2.std(axis=1))





