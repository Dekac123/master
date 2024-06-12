import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
import serial
from matplotlib.animation import FuncAnimation

# Configure the serial port to read data
# Replace 'COM3' with the appropriate serial port for your setup
ser = serial.Serial('/tmp/ttyV1', 9600, timeout=1)  # Adjust to your serial port

distance_from_center_point = 100  # Distance from the center point, used to scale the display
proportion = 36  # Ratio of rotation to vertical movement
x_list = []
y_list = []
z_list = []
z_max = distance_from_center_point * 2  # Maximum height
vertical_step = 0.2  # Vertical movement step
thread_step = vertical_step * proportion  # Rotational movement step
stop_flag = False  # Flag to stop the program

angle = 0  # Initial rotation angle
z = 0  # Initial height

# Setup the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initial plot setup
ax.set_xlim([-distance_from_center_point, distance_from_center_point])
ax.set_ylim([-distance_from_center_point, distance_from_center_point])
ax.set_zlim([0, z_max])

# Hide grid lines and axes ticks
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Create a scatter plot object
scat = ax.scatter([], [], [], color='b', s=4)

def create_point_lists(distance: float, angle: float, height: float) -> None:
    """Calculate the x, y, z coordinates based on the distance, angle, and height."""
    point_x = (distance_from_center_point - distance) * math.cos(math.radians(angle))
    point_y = (distance_from_center_point - distance) * math.sin(math.radians(angle))
    point_z = height
    x_list.append(point_x)
    y_list.append(point_y)
    z_list.append(point_z)

def update_plot(frame):
    """Update the plot with new data from the serial port."""
    global angle, z, stop_flag

    if ser.in_waiting > 0:  # Check if there's new data in the serial buffer
        try:
            distance_str = ser.readline().decode('utf-8').strip()
            print(f"Received data: {distance_str}")  # Debug: Print received data

            if distance_str:  # Ensure the read line is not empty
                distance = float(distance_str)  # Convert the distance to a float
                create_point_lists(distance, angle, z)

                # Increment z and angle
                z += vertical_step
                angle += thread_step
                if angle >= 360:
                    angle -= 360

                # Update the scatter plot data
                scat._offsets3d = (x_list, y_list, z_list)

        except ValueError:
            print("Invalid data received, skipping.")  # Debug: Handle conversion errors

    # Stop the animation if the flag is set
    if stop_flag:
        ani.event_source.stop()

def on_key_press(event):
    """Stop the program when 'q' is pressed."""
    global stop_flag
    if event.key == 'q':
        stop_flag = True

# Connect the key press event
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Start the animation with the update function
ani = FuncAnimation(fig, update_plot, interval=10)  # Update every 100ms

# Show the plot
plt.show()

# Ensure the serial connection is closed properly
ser.close()
