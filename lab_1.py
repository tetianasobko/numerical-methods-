import numpy as np

def norm1_float(X):
    return np.float32( sum(X ** 2) ** 0.5)

def norm1_double(X):
    return np.float64( sum(X ** 2) ** 0.5)

def norm2_float(X):
    a = X.max()
    return np.float32(a * sum((X / a) ** 2) ** 0.5)

def norm2_double(X):
    a = X.max()
    return np.float64(a * sum((X / a) ** 2) ** 0.5)

if __name__ == "__main__":
    x = np.array([1e-4, 1e-6, 1e-8])

    print("Norm 1 (float): ", norm1_float(x))
    print("Norm 1 (double): ", norm1_double(x))
    print("Norm 2 (float): ", norm2_float(x))
    print("Norm 2 (double): ", norm2_double(x))