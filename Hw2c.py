import numpy as np


def is_diagonally_dominant(A):
    """
    Check if a matrix A is diagonally dominant.
    """
    n = A.shape[0]
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if i != j)
        if abs(A[i, i]) < row_sum:
            return False
    return True


def GaussSeidel(Aaug, x, Niter=15):
    """
    Solve linear equations using the Gauss-Seidel method.
    Aaug is the augmented matrix [A|b], x is the initial guess, and Niter is the number of iterations.
    """
    n = Aaug.shape[0]  # Number of equations
    A = Aaug[:, :-1]  # Coefficient matrix
    b = Aaug[:, -1]  # Constant terms vector

    if not is_diagonally_dominant(A):
        print("Warning: The matrix is not diagonally dominant. The method may not converge.")

    for _ in range(Niter):
        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i, i]

    return x


def main():
    Aaug1 = np.array([[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]])
    x1 = np.zeros(Aaug1.shape[0])  # Initial guess
    solution1 = GaussSeidel(Aaug1, x1)
    print("Solution for the first set of equations:", solution1)

    Aaug2 = np.array([[1, -10, 2, 4, 2], [3, 1, 4, 12, 12], [9, 2, 3, 4, 21], [-1, 2, 7, 3, 37]])
    x2 = np.zeros(Aaug2.shape[0])  # Initial guess
    solution2 = GaussSeidel(Aaug2, x2)
    print("Solution for the second set of equations:", solution2)


if __name__ == "__main__":
    main()


