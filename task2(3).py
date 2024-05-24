import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтегралу за допомогою методу Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = y_random < f(x_random)
area_estimate_mc = (b - a) * f(b) * np.sum(under_curve) / N

print("Оцінка площі під кривою методом Монте-Карло:", area_estimate_mc)

# Аналітичний результат
area_analytical = (b**3 / 3) - (a**3 / 3)
print("Аналітичний результат:", area_analytical)

# Обчислення інтегралу за допомогою функції quad
area_quad, error = quad(f, a, b)
print("Результат за допомогою функції quad:", area_quad)
print("Похибка оцінки:", error)

# Створення діапазону значень для x для графіку
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2, label='$f(x) = x^2$')

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Інтеграл')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

# Додавання випадкових точок до графіка
ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.1)

# Додавання легенди
ax.legend()

# Додавання сітки
plt.grid()

# Показ графіка
plt.show()
