import numpy as np
import matplotlib.pyplot as plt

# Углы (phi) с шагом pi/8
phi = np.linspace(0, 2*np.pi, 17)

# Радиусы (r) по формуле
r = 8 / (3 - np.cos(phi))

# Построение графика
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(phi, r, marker='o')

# Заголовок
ax.set_title(r'$r(\phi) = \frac{8}{3 - \cos(\phi)}$', fontsize=14)

plt.show()
