from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d

import matplotlib.pyplot as plt
import numpy as np
import math
import cv2




def cylinder_lines(height: int, radius: int, density: int, ax: plt.Axes):

    teta = np.linspace(start=0, stop=2 * np.pi, num=density, endpoint=True)

    height_cyl = np.linspace(start=0, stop=height, num=height, endpoint=True)

    color = 'y'

    for h in height_cyl:
        ax.plot(radius * np.cos(teta), radius * np.sin(teta), h, color=color)

    vec_X = radius * np.cos(teta)
    vec_Y = radius * np.sin(teta)

    for i in range(0, density):
        ax.plot([vec_X[i], vec_X[i], vec_X[i]], [vec_Y[i], vec_Y[i], vec_Y[i]], [height, 0, 0], color=color)



def dots_on_cylinder(path: str, spacing: int):
    img = cv2.imread(path)

    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    img = cv2.flip(img, 0)

    height, width = img.shape[:2]

    global width_step, height_step
    width_step = int((width - spacing - 1) / spacing)
    height_step = int((height - spacing - 1) / spacing)

    matrix_dots = np.zeros((width_step + 1, height_step + 1))

    #

    for j in range(spacing, height - spacing - 1, spacing):
        for i in range(spacing, width - spacing - 1, spacing):

            if (img[i, j][1]) > 240:
                matrix_dots[int(i / spacing), int(j / spacing)] = 0
            else:
                matrix_dots[int(i / spacing), int(j / spacing)] = 1

    return matrix_dots


def _set_axes_radius(ax: plt.Axes, origin: np.ndarray, radius: int):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])


def wrap_me_a_Levi(path):
    radius_cylinder = 31  # poluprecnik cilindra

    ax = plt.axes(projection='3d')

    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.array([0, 0, 0])
    radius_sphere = 100 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius_sphere)

    # ax.axis('equal') oce kurac za 3d

    cylinder_lines(height=200, radius=radius_cylinder, density=100, ax=ax)

    map_dots = dots_on_cylinder(path, spacing=10)

    teta_map = np.linspace(start=0, stop=3 * np.pi / 2, num=2 * width_step)

    heightorino = np.linspace(start=190, stop=10, num=2 * height_step)

    for j in range(height_step):
        for i in range(width_step):

            if map_dots[i, j] == 1:
                ax.scatter(radius_cylinder * np.cos(teta_map[i]), radius_cylinder * np.sin(teta_map[i]), heightorino[j],
                           color='r', linewidths=0.0, alpha=0.7)

    plt.show()


wrap_me_a_Levi('Levi_portrait/LEVI.png')





