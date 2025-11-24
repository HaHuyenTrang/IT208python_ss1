import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print("phần tử đầu tiên: ", arr[0])
print("phần tử cuối cùng: ", arr[-1])
print("phần tử giữa mảng: ", arr[len(arr)//2])

print("các phần tử từ vị trí 2 - 5: ", arr[2:5])


arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("các phần tử từ vị trí hàng 2: ", arr2[1, :])
print("các phần tử từ vị trí cột 3: ", arr2[:, 2])

