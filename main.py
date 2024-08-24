import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, stop: 5, num:100)
y = np.linspace(-5, stop: 5, num:100)

x, y = np.meshgrid(*xi: x, y)
z = np.sin(x) * np.cos(y)

fig = plt.figure(figsize=(14, 6))

ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('3D Plot')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')


ax2 = fig.add_subplot(122)
contour = ax2.contour(x, y, z, cmap='viridius')
fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title('Contour Plot')
ax2.set_xlabel('X-Axis')
ax2.set_ylabel('Y-Axis')

plt.tight_layout()
plt.show()