import matplotlib
matplotlib.use('TkAgg')  # Must be before importing pyplot
matplotlib.rcParams['text.usetex'] = False  # Disable LaTeX rendering

import numpy as np
import matplotlib.pyplot as plt

# Create x values for arcsin/arccos (-1 to 1) and arctan/arccot (-5 to 5)
x1 = np.linspace(-1, 1, 400)  # For arcsin and arccos
x2 = np.linspace(-5, 5, 400)  # For arctan and arccot

# Calculate function values
y_arcsin = np.arcsin(x1)
y_arccos = np.arccos(x1)
y_arctan = np.arctan(x2)
y_arccot = np.pi/2 - np.arctan(x2)  # arccot(x) = π/2 - arctan(x)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# arcsin(x)
axes[0, 0].plot(x1, y_arcsin, label='arcsin(x)', color='b')
axes[0, 0].set_title('arcsin(x)')
axes[0, 0].grid(True)
axes[0, 0].legend()

# arccos(x)
axes[0, 1].plot(x1, y_arccos, label='arccos(x)', color='r')
axes[0, 1].set_title('arccos(x)')
axes[0, 1].grid(True)
axes[0, 1].legend()

# arctan(x)
axes[1, 0].plot(x2, y_arctan, label='arctan(x)', color='g')
axes[1, 0].set_title('arctan(x)')
axes[1, 0].grid(True)
axes[1, 0].legend()

# arccot(x)
axes[1, 1].plot(x2, y_arccot, label='arccot(x)', color='m')
axes[1, 1].set_title('arccot(x)')
axes[1, 1].grid(True)
axes[1, 1].legend()

# Add axis lines and labels for each plot
for ax in axes.flat:
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# Set specific limits for each function
axes[0, 0].set_ylim([-np.pi/2, np.pi/2])
axes[0, 1].set_ylim([0, np.pi])
axes[1, 0].set_ylim([-np.pi/2, np.pi/2])
axes[1, 1].set_ylim([0, np.pi])

# Adjust layout and display
plt.tight_layout()
plt.show()
