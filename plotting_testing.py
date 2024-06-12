import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d
import math
import random
import numpy as np

def nevena(distance: float, thread_step: float, vertical_step: float) -> None:

    ax = plt.axes(projection='3d')

    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.array([0, 0, 0])
    radius_sphere = 100 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius_sphere)

    angle = 0
    for z in range(0, 200, vertical_step):

        x: float = distance * math.cos(math.radians(angle))
        y: float = distance * math.sin(math.radians(angle))
        angle = angle + thread_step
        if angle > 360:
            angle = 0
        distance = random.randint(0, 100)

        ax.scatter(x, y, z)

    plt.show()


def _set_axes_radius(ax: plt.Axes, origin: np.ndarray, radius: int):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])


nevena(300, 10, 1)