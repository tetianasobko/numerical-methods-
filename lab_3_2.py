def zeidel_method1(f1, f2, x0, y0, eps, max_iterations=100):
    x = x0
    y = y0
    
    x_p = x
    y_p = y

    for i in range(max_iterations):
        x = f1(y)
        y = f2(x)

        if abs(x - x_p) < eps and abs(y - y_p) < eps:
            return x, y
        
        x_p = x
        y_p = y

    return "Zeidel's method not converge, " + str((x0, y0))

def zeidel_method2(f1, f2, x0, y0, eps, max_iterations=100):
    x = x0
    y = y0
    
    x_p = x
    y_p = y

    for i in range(max_iterations):
        y = f1(x)
        x = f2(y)

        if abs(x - x_p) < eps and abs(y - y_p) < eps:
            return x, y
        
        x_p = x
        y_p = y

    return "Zeidel's method not converge, " + str((x0, y0))

f1 = lambda y: (1 + y**2)**(1/2)
f2 = lambda x: 1/(x**3)**(1/2)
f3 = lambda x: (x**2 - 1)**(1/2)
f4 = lambda y: (1/(y**2))**(1/3)

print(zeidel_method1(f1, f2, 1.23, 0.7, 0.01))
print(zeidel_method2(f3, f4, 1.23, 0.7, 0.01))
print(zeidel_method1(f1, f2, 1.23, 0.7, 0.0001))
print(zeidel_method2(f3, f4, 1.23, 0.7, 0.0001))