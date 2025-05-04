import math
import matplotlib.pyplot as plt
import numpy as np
import json

def f(x, A=0):
    numerator = math.sin(x**2 - A**2)**2 - 0.5
    denominator = 1 + 0.001 * (x**2 + A**2)
    return 0.5 + numerator / denominator

# Создание массива значений для x с шагом 0.01
x_values = np.arange(-10, 10.01, 0.01)
y_values = [f(x) for x in x_values]

# Подготовка данных для записи в JSON (только x)
data = [{"x": x} for x in x_values]
result = {"data": data}

# Запись данных в JSON-файл
with open('output.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print("x \t f(x)")
for x, y in zip(x_values[:100], y_values[:100]):
    print(f"{x:.2f} \t {y:.5f}")  # Форматирование вывода

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label="f(x)", color="purple")
plt.title("График функции f(x) при A = 0, X∈[-10;10]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
