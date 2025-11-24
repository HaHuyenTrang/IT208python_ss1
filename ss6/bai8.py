import numpy as np

np.random.seed(0)  # để kết quả tái lập được
A = np.random.randint(1, 10, size=(3,3))
print("Ma trận gốc A:\n", A)

# Tính ma trận nghịch đảo
# Sử dụng np.linalg.inv() - vector hóa bên trong
A_inv = np.linalg.inv(A)
print("\nMa trận nghịch đảo A^-1:\n", A_inv)

# Tính giá trị riêng và véc tơ riêng
eigvals, eigvecs = np.linalg.eig(A)
print("\nGiá trị riêng của A:\n", eigvals)
print("\nVéc tơ riêng của A:\n", eigvecs)

# So sánh ma trận gốc và ma trận nghịch đảo
# Kiểm tra: A * A^-1 ≈ I (ma trận đơn vị)
I_approx = np.dot(A, A_inv)
print("\nTích A * A^-1 (gần bằng ma trận đơn vị):\n", I_approx)
