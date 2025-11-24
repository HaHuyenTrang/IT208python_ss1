import numpy as np
import time
arr = np.random.randint(1,20, size=(10))
print("mảng: ", arr)
# 1️⃣ Sử dụng vector hóa / ufunc
# -----------------------------
start = time.time()

squared_vec = np.multiply(arr, arr)   # bình phương
sqrt_vec = np.sqrt(arr)               # căn bậc hai

end = time.time()
print("\nVector hóa:")
print("Bình phương:", squared_vec)
print("Căn bậc hai:", sqrt_vec)
print("Thời gian vector hóa:", end - start)