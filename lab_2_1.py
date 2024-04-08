import numpy as np

def gaussian(A, b):
    A = np.hstack((A, b))
    n = A.shape[0]

    for i in range(n):
        A[i] /= A[i][i]
        for j in range(i+1, n):
            A[j] -= A[i] * A[j][i]

        print(A)
        print()
    
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = A[i][-1]
        for j in range(n-1, i, -1):
            X[i] -= A[i][j] * X[j]

    return X


if __name__ == "__main__":
    A = np.array([[0.64, -0.42, -1.03, 0.3],
                  [0.45, -0.61, 0.11, 1.06],
                  [0.26, 0.34, -0.08, -0.65],
                  [0.26, -0.23, -0.84, 1.82]])

    f = np.array([[0.76],
                [-0.38],
                [-0.38],
                [4.37]])

    print(gaussian(A, f))
