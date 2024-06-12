import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d
import math
import random
import numpy as np

distance_from_center_point = 100 * 0.37 #duzina lasera od centra ploce uz pojacanje prikaza

#odnos maksimalnog ugla i visine
proportion = 50
def nevena(distance: float) -> None:

    vertical_step = 0.3
    thread_step = vertical_step * proportion

    ax = plt.axes(projection='3d')

    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.array([0, 0, 0])
    radius_sphere = distance_from_center_point * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius_sphere)

    z_max = 80 #visina


    z = 0
    x_list:list = []
    y_list:list = []
    z_list:list = []
    angle = 0

    while z < z_max:

        x_list.append(distance * math.cos(math.radians(angle)))
        y_list.append(distance * math.sin(math.radians(angle)))
        #print(angle)
        z = z + vertical_step
        z_list.append(z)
        angle = angle + thread_step
        if angle > 360:
            angle = angle - 360
        #distance = random.randint(0, 100)
    ax.scatter(x_list, y_list, z_list,s=4)
        #print(len(x))


    # Hide grid lines
    ax.grid(False)
    ax.grid(b=None)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    plt.show()


def _set_axes_radius(ax: plt.Axes, origin: np.ndarray, radius: int):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])


nevena(50)