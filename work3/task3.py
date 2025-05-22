import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    s1 = np.sin(3*np.pi*x1)**2
    s2 = (x1-1)**2 * (1 + np.sin(3*np.pi*x2)**2)
    s3 = (x2-1)**2 * (1 + np.sin(2*np.pi*x2)**2)
    return s1 + s2 + s3

# Параметры
x1 = x2 = np.linspace(-2, 2, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)
x0, y0 = 1.0, 1.0
z0 = f(x0, y0)

# Создание графиков
fig = plt.figure(figsize=(14, 10))
fig.suptitle(f'Анализ функции\nМинимум в ({x0},{y0}) = {z0:.2f}', y=1.02)

# 3D графики
views = [('Изометрия', None), ('Вид сверху', (90, 0))]
for i, (title, view) in enumerate(views, 1):
    ax = fig.add_subplot(2, 2, i, projection='3d')
    ax.plot_surface(X1, X2, Y, cmap='plasma', alpha=0.8)
    ax.scatter([x0], [y0], [z0], 'r', s=50)
    if view: ax.view_init(*view)
    ax.set_title(f'{i}. 3D: {title}')
    ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('f(x1,x2)')

# 2D сечения
for i, (var, vals, color) in enumerate([('x1', x1, 'b'), ('x2', x2, 'g')], 3):
    ax = fig.add_subplot(2, 2, i)
    y = f(vals, y0) if i == 3 else f(x0, vals)
    ax.plot(vals, y, color, lw=2)
    ax.scatter(x0 if i==3 else y0, z0, c='r', s=80)
    ax.grid(ls='--', alpha=0.6)
    ax.set_title(f'{i}. Сечение по {var}')

plt.tight_layout()
plt.show()