import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 5, 500)
y = 10 * np.cos(x**2) / (x**2)

plt.figure(figsize=(8, 5))
plt.plot(x, y, linestyle='-', color='purple', linewidth=2.5, label='Y(x) = 10*cos(x^2)/x^2')

plt.ylim(-20, 50)

plt.title('Графік функції')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()