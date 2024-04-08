import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Задана вибірка даних
data = {
    2013: 37,
    2014: 39,
    2015: 55,
    2016: 44,
    2017: 48,
    2018: 59,
    2019: 54,
    2020: 58,
    2021: 93,
    2022: 99,
}

# Крок 1: Поліноміальна інтерполяція
x_data = np.array(list(data.keys()))
y_data = np.array(list(data.values()))

# Використовуємо numpy.polyfit для отримання коефіцієнтів полінома
coefficients = np.polyfit(x_data, y_data, len(x_data) - 1)

# Інтерполяційний поліном
def polynomial_interpolation(x, coefficients):
    return np.polyval(coefficients, x)

phi_polynomial = polynomial_interpolation(2023, coefficients)

# Крок 3: Кубічна сплайн-інтерполяція
cs = CubicSpline(x_data, y_data)

# Крок 4: Метод найменших квадратів
# Побудова матриці A та вектора b
A = np.vstack([np.ones_like(x_data), x_data]).T
b = y_data

# Розв'язок системи лінійних рівнянь Ax = b
# Коефіцієнти a та b для найкращого середньоквадратичного наближення
coefficients_least_squares = np.linalg.lstsq(A, b, rcond=None)[0]

# Функція для найкращого середньоквадратичного наближення
def phi_least_squares(x, coefficients):
    return coefficients[0] + coefficients[1] * x

# Крок 5: Графічне представлення
x_range = np.linspace(min(x_data), max(x_data), 1000)
plt.scatter(x_data, y_data, label='Дані')
plt.plot(x_range, polynomial_interpolation(x_range, coefficients), label='phi(x) (Поліноміальна інтерполяція)', linestyle='dashed')
plt.plot(x_range, cs(x_range), label='phi(x) (Кубічний сплайн)')
plt.plot(x_range, phi_least_squares(x_range, coefficients_least_squares), label='phi(x) (Найменші квадрати)')
plt.legend()
plt.title('Інтерполяція та апроксимація')
plt.xlabel('Рік')
plt.ylabel('Кількість')
plt.show()
