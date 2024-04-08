import math

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    if x == 0:
        return 0

def bisection(f, a, b, eps=1e-4, max_iterations=1000):
    c = (a + b) / 2
    n = 1
    while f(c) != 0 and (b - a) / 2 > eps and n < max_iterations:
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c
        
        c = (a + b) / 2
        n += 1
    
    return c, n

def secant(f, x0, x1, eps=1e-4, max_iterations=100):
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    for _ in range(max_iterations):
        if abs(x0 - x1) < eps: break

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
    
    return x2


if __name__ == "__main__":
    f = lambda x: x - 2 * math.exp(1 - 1/x**2)

    print(bisection(f, 5, 6)[0])
    print(secant(f, 0.5, 1))
    # для різних додатних коренів записати діапазон і тд

