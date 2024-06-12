import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import Delaunay

# Step 1: Read the points from the file
def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            # Each line is expected to be in the format "x y z"
            values = line.split()
            if len(values) == 3:  # Ensure there are exactly 3 values
                point = list(map(float, values))
                points.append(point)
    return np.array(points)

# Read the points from 'point_cloud.txt'
filename = 'point_cloud.txt'
points = read_points_from_file(filename)

# Step 2: Perform Delaunay triangulation
tri = Delaunay(points)

# Step 3: Plotting the 3D triangular mesh
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vertices
ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r')

# Plot the edges and triangles
# We use Poly3DCollection to create a collection of triangles
# Since we are in 3D, Delaunay triangulation will give tetrahedrons in 3D space,
# so we will plot the triangular faces of these tetrahedrons.
for simplex in tri.simplices:
    # Each simplex is a list of indices into the points array
    triangles = [[points[simplex[0]], points[simplex[1]], points[simplex[2]]],
                 [points[simplex[0]], points[simplex[1]], points[simplex[3]]],
                 [points[simplex[0]], points[simplex[2]], points[simplex[3]]],
                 [points[simplex[1]], points[simplex[2]], points[simplex[3]]]]
    for triangle in triangles:
        poly = Poly3DCollection([triangle], alpha=0.5, edgecolor='k')
        ax.add_collection3d(poly)

# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Triangular Mesh')

plt.show()
