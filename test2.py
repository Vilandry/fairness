from interpolate import interpolate
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


interpolater = interpolate()


xk = [ [1, 1], [0, 2], [2, 2],  [1, 3], [2, 3] ]
yk = [1, 1, 2,  3, 4]

interpolater.setM(1)
interpolater.setXK(xk)
interpolater.setYK(yk)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(0, 5, 1)
Y = np.arange(0, 5, 1)
X, Y = np.meshgrid(X, Y)

pZ = []
print(Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
#print(R)
for rowX in X:
    for rowY in Y:   
        toappend = []
        for ycoord in rowY:
            for xcoord in rowX:
                point = [xcoord, ycoord]
                value = interpolater.interpolate(point)
                toappend.append(value)
            break
        pZ.append(toappend)
    break

Z = np.array(pZ)
print(Z)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 5.0)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()