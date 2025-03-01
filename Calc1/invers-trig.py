import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plots

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Khởi tạo dữ liệu
x = np.linspace(-2*np.pi, 2*np.pi, 400)
sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)

# Tạo figure và các subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ["Hàm lẻ: sin(x)", "Hàm chẵn: cos(x)", "Hàm lẻ: tan(x)"]

# Vẽ đồ thị ban đầu
lines = []
mirror_lines = []
points = []
mirror_points = []

for ax, func, title in zip(axes, [sin_x, cos_x, tan_x], titles):
    ax.plot(x, func, label=title.split(": ")[1])
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(title)
    ax.legend()
    ax.grid()
    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_ylim(-1.5, 1.5)
    
    # Điểm di chuyển
    point, = ax.plot([], [], 'bo', markersize=8)
    mirror_point, = ax.plot([], [], 'ro', markersize=8)
    
    points.append(point)
    mirror_points.append(mirror_point)

# Animation update function
def update(frame):
    t = -2*np.pi + (4*np.pi) * (frame / 100)  # Di chuyển x từ -2π đến 2π
    for i, (func, point, mirror_point) in enumerate(zip([np.sin, np.cos, np.tan], points, mirror_points)):
        y = func(t)
        if i == 2 and (np.abs(np.cos(t)) < 0.1):  # Bỏ qua tiệm cận của tan(x)
            continue
        point.set_data([t], [y])  
        if i == 1:  # cos(x) là hàm chẵn
            mirror_point.set_data([-t], [y])
        else:  # sin(x) và tan(x) là hàm lẻ
            mirror_point.set_data([-t], [-y])
    return points + mirror_points

# Chạy animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
