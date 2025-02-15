import matplotlib.pyplot as plt
import numpy as np

#11
x1 = np.linspace(-5, 9.25)
y1 = -4 * x1**2 + 17 * x1 - 14

plt.plot(x1, y1)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('-4x^2 + 17x - 14')
plt.axhline()
plt.axvline()
plt.show()

x2 = np.linspace(-5, 5)
y2 = -3 * x2 + 13

plt.plot(x2, y2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('-3x + 13')
plt.axhline()
plt.axvline()
plt.show()

x3 = np.linspace(-5, 5)
y3 = (3 / x3) + 1

plt.plot(x3, y3)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('3 / x + 1')
plt.axhline()
plt.axvline()
plt.show()

x4 = np.linspace(-5, 5)
y4 = 5 / (x4 + 3)

plt.plot(x4, y4)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('5 / (x + 3)')
plt.axhline()
plt.axvline()
plt.show()

x5 = np.linspace(-5, 5)
y5 = 7/4 * x4 - 5/4

plt.plot(x5, y5)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('7/4 * x - 5/4')
plt.axhline()
plt.axvline()
plt.show()

#13
x6 = np.linspace(-5, 5)
y6 = 6 * np.sin(x6)**2 + 7 * np.cos(x6) - 7 

plt.plot(x6, y6)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('6sin^2(x) + 7cos(x) - 7')
plt.axhline()
plt.axvline()
plt.show()

x7 = np.linspace(-5, 5)
y7 = 4**x7+1 - 5 * 2**x7 - 3

plt.plot(x7, y7)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('4**x+1 - 5 * 2**x - 3')
plt.axhline()
plt.axvline()
plt.show()

x8 = np.linspace(-5, 5)
y8 = (13 * np.sin(x8)**2 - 5 * np.sin(x8)) / 13 * np.cos(x8) + 12

plt.plot(x8, y8)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('13sin(x)**2 - 5 *sin(x) / 13cos(x) + 12')
plt.axhline()
plt.axvline()
plt.show()

x9 = np.linspace(-5, 5)
y9 = 19 * 4**x9 - 5 * 2**x9+2 + 1
plt.plot(x9, y9)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('19 * 4**x - 5 * 2**x+2 + 1')
plt.axhline()
plt.axvline()
plt.show()

x10 = np.linspace(-5, 5)
y10 = (1 / np.cos(x10)**2) + (3 / np.cos(x10)) + 2

plt.plot(x10, y10)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('(1 / np.cos(x)**2) + (3 / np.cos(x)) + 2 = 0')
plt.axhline()
plt.axvline()
plt.show()