import numpy as np

def min_nevyazok(A, b, max_iterations=1000, eps=1e-6):
    n = len(b)
    x = b

    r = b - np.dot(A, x)
    iterations = 0

    while np.linalg.norm(r) > eps and iterations < max_iterations:
        r = b - np.dot(A, x)
        Ar = np.dot(A, r)
        tau = np.dot(Ar, r) / np.linalg.norm(Ar) ** 2

        x = x + tau * r

        iterations += 1

    return x, iterations

if __name__ == "__main__":
    A = np.array([[0.2293, -0.1507, -0.2609, 0.3152],
                  [-0.1507, 0.181, 0.1595, -0.3722],
                  [-0.2609, 0.1595, 0.481, -0.4852],
                  [0.3152, -0.3722, -0.4852, 1.2625]])

    b = np.array([0.4708, -0.3697, -1.193, 2.0636])

    print(min_nevyazok(A, b, eps=0.01))
    print(min_nevyazok(A, b, eps=0.0001))
    print(min_nevyazok(A, b, eps=0.00000000001))