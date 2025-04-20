import json
import math
import matplotlib.pyplot as plt
import numpy as np
import argparse

def f(x, A=0):
    numerator = math.sin(x**2 - A**2)**2 - 0.5
    denominator = 1 + 0.001 * (x**2 + A**2)
    return 0.5 + numerator / denominator

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['data']

def plot_graph(data, title=None, xlabel=None, ylabel=None, grid=False, x_step=1.0):
    x_values = np.array([point['x'] for point in data])
    y_values = np.array([f(point['x']) for point in data])

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, label="f(x)", color="red")

    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if grid:
        plt.grid(True)

    plt.xticks(np.arange(min(x_values), max(x_values) + 1, x_step))
    plt.legend()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Plot graph from JSON data.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('--title', type=str, help='Title of the graph')
    parser.add_argument('--xlabel', type=str, help='Label for the X axis')
    parser.add_argument('--ylabel', type=str, help='Label for the Y axis')
    parser.add_argument('--grid', action='store_true', help='Show grid on the graph')
    parser.add_argument('--x_step', type=float, default=1.0, help='Step for X axis ticks')

    args = parser.parse_args()

    data = load_data(args.input_file)
    plot_graph(data, args.title, args.xlabel, args.ylabel, args.grid, args.x_step)

if __name__ == '__main__':
    main()
    