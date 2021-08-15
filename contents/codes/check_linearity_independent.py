import numpy as np

def check_linearity_independent(matrix):
    (m, n) = matrix.shape
    if m != n:
        # Ta có ma trận A không là ma trận vuông
        # Tính hạng của ma trận A
        RA = np.linalg.matrix_rank(matrix)
        if RA == m:
            return True
        if RA < m:
            return False

    if m == n:
        # Ta có ma trận A là ma trận vuông
        # Tính định thức của ma trận A
        det = np.linalg.det(matrix)
        if det != 0:
            return True
        elif det == 0:
            return False

# Test :v
u1 = np.array([-1, 2, -1, 2])
u2 = np.array([2, 2, -4, 2])
u3 = np.array([1, 3, 1, 2])

# Hãy kiểm tra xem u1 , u2 , u3 độc lập tuyến tính hay phụ thuộc tuyến tính?

matrix = np.array([u1.T, u2.T, u3.T])

print(check_linearity_independent(matrix))
