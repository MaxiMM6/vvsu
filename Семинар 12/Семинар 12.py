import matplotlib.pyplot as plt
import numpy as np

#1 f(x) = -4x**2 + 17x - 14
a = -4
b = 17
c = -14

x = np.linspace(0, 5)
y = -4 * x**2 + 17 * x -14

plt.figure(figsize=(5, 6))
plt.plot(x, y)
plt.grid()
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('f(x) = -4x**2 + 17x -14')
plt.legend()
plt.show()



'''# Создаем график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = ax^2 + bx + c', color='blue')
plt.title('График параболы')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')

plt.legend()
'''