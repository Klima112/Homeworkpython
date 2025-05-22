import json
import matplotlib.pyplot as plt
import numpy as np
import argparse

def load_data(file_path):
    with open(file_path) as f:
        return json.load(f)['data']

def plot(data, title='Graph', xlabel='x', ylabel='y', grid=False, step=1.0):
    x = np.array([p['x'] for p in data])
    y = np.array([p['y'] for p in data])
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'm-', label='f(x)')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    if grid:
        plt.xticks(np.arange(x.min(), x.max()+1, step))
        plt.grid(True, which='both')
        plt.minorticks_on()
        plt.grid(which='minor', alpha=0.2)
    
    plt.legend()
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='JSON file path')
    parser.add_argument('--title', default='Graph', help='Graph title')
    parser.add_argument('--xlabel', default='x', help='X-axis label')
    parser.add_argument('--ylabel', default='y', help='Y-axis label')
    parser.add_argument('--grid', action='store_true', help='Show grid')
    parser.add_argument('--step', type=float, default=1.0, help='Grid step size')
    
    args = parser.parse_args()
    plot(load_data(args.file), args.title, args.xlabel, args.ylabel, args.grid, args.step)
    # python task2.py task1.json --step 1.0 --grid --title "My Plot"