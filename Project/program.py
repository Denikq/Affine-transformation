# Convex hull

# Program for finding convex hull from dataset

# Done by Denys Dolynniy
# Date: 23.11.2021

import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d

# function for opening and reading file
def readFile():
    with open("DS3.txt") as f:
        lines = f.readlines()
    f.close()
    return lines

# class for reading and editing text file (dataset)
def editLines():
    unformed_coordinates = []
    for line in readFile():
        unformed_coordinates.append(list(line))

    arr = list()

    for dot in unformed_coordinates:
        for num in range(len(dot)):
            if dot[num] == '\n':
                dot.remove(dot[num])
        for num in range(len(dot)):
            if dot[num] == ' ':
                r1 = dot[0:num]
                r2 = dot[num + 1:len(dot)]
                r = [r1, r2]
                arr.append(r)

    coordinates_dots = []
    for dot in arr:
        dot_1 = []
        for axis in dot:
            l = ''
            for k in range(len(axis)):
                l = l + axis[k]
            axis = int(l)
            dot_1.append(axis)
        coordinates_dots.append(dot_1)

    coordinates_dots = np.array(coordinates_dots)

    return coordinates_dots


coordinates = editLines()
