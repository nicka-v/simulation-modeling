import numpy as np

def matrix_multiply(A, B):
    try:
        result = np.matmul(A, B)
        return result
    except Exception as e:
        print(f"Ошибка при перемножении матриц: {e}")
        raise

A = np.random.randint(0, 10, size=(2, 3))
B = np.random.randint(0, 10, size=(3, 2))
    
print("Матрица A:")
print(A)
print("\nМатрица B:")
print(B)
    
print("\nРезультат умножения A и B:")
print(matrix_multiply(A, B))
