import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import random
import numpy as np

################################################################
distance_from_center_point = 100  # Distance from the center point, used to scale the display
proportion = 36  # Ratio of rotation to vertical movement
x_list: list = []
y_list: list = []
z_list: list = []
z_max = distance_from_center_point * 2  # Maximum height
vertical_step = 0.2  # Vertical movement step
thread_step = vertical_step * proportion  # Rotational movement step
stop_flag = False  # Flag to stop the program


################################################################

def create_point_lists(distance: float, angle: float, height: float) -> None:
    point_x = (distance_from_center_point - distance) * math.cos(math.radians(angle))
    point_y = (distance_from_center_point - distance) * math.sin(math.radians(angle))
    point_z = height + vertical_step
    x_list.append(point_x)
    y_list.append(point_y)
    z_list.append(point_z)


def _set_axes_radius(ax: plt.Axes, origin: np.ndarray, radius: int):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])


def plot_setup_for_3D(ax: plt.Axes):
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.array([0, 0, 0])
    radius_sphere = distance_from_center_point * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius_sphere)


def on_key_press(event):
    global stop_flag
    if event.key == 'q':
        stop_flag = True


def serial_plotting():
    global stop_flag
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_setup_for_3D(ax)

    fig.canvas.mpl_connect('key_press_event', on_key_press)

    angle = 0  # Rotation angle
    z = 0

    point_count = 0  # Counter for all points
    spiral_counts = []  # List to keep track of points per spiral
    current_spiral_points = 0  # Points in the current spiral

    # Open the file in write mode
    with open("point_cloud.txt", "w") as file:
        while z < z_max:
            if stop_flag:
                break

            distance = random.randint(20, 30)  # Simulated sensor data
            create_point_lists(distance, angle, z)

            # Write the current point to the file
            file.write(f"{x_list[-1]} {y_list[-1]} {z_list[-1]}\n")

            point_count += 1  # Increment total point counter
            current_spiral_points += 1  # Increment current spiral counter

            z += vertical_step
            angle += thread_step
            if angle >= 360:
                angle -= 360
                # When a full spiral is completed, record the number of points
                spiral_counts.append(current_spiral_points)
                current_spiral_points = 0  # Reset the counter for the next spiral

            ax.clear()
            ax.scatter(x_list, y_list, z_list, s=4)

            # Hide grid lines
            ax.grid(False)

            # Hide axes ticks
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])

            plt.draw()
            #plt.pause(0.01)

    # Print the total number of points
    print(f"Total number of points: {point_count}")

    # Calculate and print the average number of points per spiral
    if spiral_counts:  # Check if there is at least one completed spiral
        average_points_per_spiral = sum(spiral_counts) / len(spiral_counts)
        print(f"Average number of points per spiral: {average_points_per_spiral:.2f}")
    else:
        print("No complete spirals were generated.")

    plt.show()


serial_plotting()
