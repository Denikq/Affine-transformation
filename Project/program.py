# Affine transformation

# Program for affine transformation 
# Rotating to 40 degrees from given dot - (480; 480)

# Done by Denys Dolynniy
# Date: 26.11.2021

import numpy as np
from matplotlib import pyplot as plt

# function for opening and reading file
def readFile():
    with open("DS3.txt") as f:
        lines = f.readlines()
    f.close()
    return lines

# function for reading and editing text file (dataset)
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

# function for affine transformation given dataset
def affine_transform(coordinates):
    coordinates = coordinates.tolist()

    new_coordinates = list()

    for dot in coordinates:
        x = dot[0]
        y = dot[1]

        x1 = 0.766*x - 0.643*y + 420.96
        y1 = 0.643*x + 0.766*y - 196.32

        dot1 = [x1, y1]

        new_coordinates.append(dot1)
    
    return new_coordinates

# function for displayin coordinates (transformed, not-transofrmed, both simultaneously)
def displaying_results(coordinates, new_coordinates):

    x, y = coordinates.T
    x1, y1 = new_coordinates.T

    px = 1 / plt.rcParams['figure.dpi']    
    plt.subplots(figsize=(960 * px, 960 * px))

    plt.scatter(x1, y1)
    plt.scatter(x,y)

    gra_format = 'png'
    n = 3
    plt.savefig(f'Figure{n}.{gra_format}', dpi=200)

    plt.show()

# function for saving transformed coordinates
def write_transformed_coordinates(new_coordinates):
    with open("transformed_coordinates.txt", "w") as f:
        res = list(new_coordinates)
        for k in range(len(new_coordinates)):
            f.write(str(new_coordinates[k]).replace("[", "").replace("]", ""))
            f.write("\n")
        f.close()


if __name__ == "__main__":
    coordinates = editLines()
    new_coordinates = np.asarray(affine_transform(coordinates))
    write_transformed_coordinates(new_coordinates)
    displaying_results(coordinates, new_coordinates)




