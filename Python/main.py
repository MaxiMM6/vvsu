import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def func(x):
    return np.sin(2*x) + np.sqrt(3) * np.sin(x - np.pi)

# Создаем массив значений x
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = func(x)

# Находим точки пересечения с осью X
zero_crossings = np.where(np.diff(np.sign(y)))[0]

# Построим график
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$\sin(2x) + \sqrt{3} \sin(x - \pi)$')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.scatter(x[zero_crossings], y[zero_crossings], color='red', label='Пересечения с осью X')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()