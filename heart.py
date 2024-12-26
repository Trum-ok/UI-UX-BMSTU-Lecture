import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200
plt.style.use('default')


def heart(x, y, z):
    return (x ** 2 + ((9 * y ** 2) / 4) + z ** 2 - 1) ** 3 - x ** 2 * z ** 3 - ((9 * y ** 2 * z ** 3) / 80)

def plot_implicit(fn, bbox=(-1.5, 1.5), resolution=100, slices=100, rotation_speed=0.5):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    resolution = np.linspace(xmin, xmax, resolution)
    slices = np.linspace(xmin, xmax, slices)
    resolution1, resolution2 = np.meshgrid(resolution, resolution)

    for z in slices:
        X, Y = resolution1, resolution2
        Z = fn(X, Y, z)
        ax.contour(X, Y, Z, levels=[0], zdir='z', offset=z, colors='red', alpha=0.5)

    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)

    plt.show()


if __name__ == '__main__':
    plot_implicit(heart)
