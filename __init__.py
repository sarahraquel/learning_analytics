import csv 
from matplotlib import pyplot as plt
import numpy as np

'''
with open('texto.txt', 'r') as file:
    reader = csv.reader(file)
'''
def generate_bar_graph(x, y, title, xlabel,ylabel):
    plt.bar(x, y)
    plt.title("Grafico de Barra")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def generate_line_graph(x, y, title, xlabel, ylabel):
    plt.plot(x, y, color="green", marker="o", linestyle='solid')
    plt.title("Grafico de linha")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def get_media(array):
    return np.mean(array)

def get_median(array):
    return np.median(array)

def get_mode(array):
    return np.bincount(array).argmax()

a = [1, 2, 3]
print (np.amin(a))
print(np.amax(a))