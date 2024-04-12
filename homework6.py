import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np


#PROBLEM 1

# making three random lists
random_data1 = np.random.randint(0, 101, size=40)
random_data2 = np.random.randint(0, 101, size=40)
random_data3 = np.random.randint(0, 101, size=40)

# making empty figure and subplots
fig, axs = plt.subplots(2, 1)

# top plot - orange thick line and red dashed line
axs[0].plot(range(40), random_data1, color='orange', linewidth=10)
axs[0].plot(range(40), random_data2, color='red', linestyle='--')
axs[0].set_title('Top Plot')
axs[0].set_xlabel('Position in List')
axs[0].set_ylabel('Random Data')

# bottom plot - magenta diamonds scatter plot
axs[1].scatter(range(40), random_data3, color='magenta', marker='D')
axs[1].set_title('Bottom Plot')
axs[1].set_xlabel('Position in List')
axs[1].set_ylabel('Random Data')

# adjust the layout
plt.tight_layout()

# show the plot
plt.show()


#PROBLEM 2


import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 16.02  # bar L^2 / mol^2
b = 0.1124  # L / mol
R = 0.083144  # bar L / mol K
n = 1  # number of moles

# defining pressure and volume ranges
pressure = np.linspace(1, 10, 100)  # bar
volume = np.linspace(10, 30, 100)  # L

# make a grid of pressure and volume values
P, V = np.meshgrid(pressure, volume)

# solve for temperature in the Van der Waals equation
T = (P + a * (n ** 2) / (V ** 2)) * (V - n * b) / (n * R)
vmin = np.min(T)
vmax = np.max(T)
# plotting colormap
plt.figure(figsize=(10, 6))
plt.pcolormesh(P, V, T, cmap='viridis', shading='auto', vmin=np.min(T), vmax=np.max(T))
plt.colorbar(label='Temperature (K)')
plt.xlabel('Pressure (bar)')
plt.ylabel('Volume (L)')
plt.title('Temperature of One Mole of Acetone (Van der Waals Gas)')
plt.grid(True)
plt.show()

#PROBLEM 3

def estimate_pi(N):
    # generate random points in the 1x1 square
    points = np.random.rand(int(N), 2)
    
    # find distance from each point to the origin
    distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    
    # count points within the quarter circle
    points_inside = np.sum(distances <= 1)
    
    # estimate pi using the ratio of points inside the quarter circle to the total points
    pi_estimate = 4 * points_inside / N
    
    return pi_estimate

# values of N
Ns = [1e3, 1e4, 1e5, 1e6]

# calculate pi for each value of N
for N in Ns:
    pi_estimate = estimate_pi(N)
    print(f"π estimate for N={N}: {pi_estimate}")

# plot points for N=1e4
N = 1e4
points = np.random.rand(int(N), 2)
distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
points_inside = points[distances <= 1]
points_outside = points[distances > 1]

plt.figure(figsize=(6, 6))
plt.scatter(points_inside[:, 0], points_inside[:, 1], color='magenta', label='Inside Quarter Circle')
plt.scatter(points_outside[:, 0], points_outside[:, 1], color='yellow', label='Outside Quarter Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Monte Carlo Estimate of π')
plt.text(0.1, 0.9, f'π ≈ {4 * len(points_inside) / N}', transform=plt.gca().transAxes)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
