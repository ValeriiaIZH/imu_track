import numpy as np
from matplotlib import pyplot as plt
from math import *

d_time = 0.03
array = []
accel = []
gx = []
gy = []
gz = []
ax = []
ay = []
az = []
mx = []
my = []
mz = []
mag_x = []
mag_y = []
yaw = []
pitch = []
roll = []

with open("values_from_gym_2.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        array.append([float(x) for x in line.split()])
    num = sum(1 for line in data)
    for i in range(0, num):

        ax.append(array[i][0])
        ay.append(array[i][1])
        az.append(array[i][2])

        gx.append(array[i][3])
        gy.append(array[i][4])
        gz.append(array[i][5])

        mx.append(array[i][6])
        my.append(array[i][7])
        mz.append(array[i][8])

        #pitch.append(atan2(ax[i], sqrt(ay[i] * ay[i] + az[i] * az[i])))
        #roll.append(atan2(ay[i], sqrt(ax[i] * ax[i] + az[i] * az[i])))
        #mag_x.append(mx[i] * cos(pitch[i]) + my[i] * sin(roll[i]) * sin(pitch[i]) + mz[i] * cos(roll[i]) * sin(pitch[i]))
        #mag_y.append(my[i] * cos(roll[i]) - mz[i] * sin(roll[i]))
        #yaw.append(atan2(mag_x[i],mag_y[i]))
        yaw.append(array[i][9] * pi / 180)
        if yaw[i] > 1 : yaw[i] = 1
        if yaw[i] < -1 : yaw[i] = -1
        accel.append(np.sqrt(array[i][4] ** 2 + array[i][5] ** 2 + array[i][6] ** 2))
    # print(yaw)

vel = []
v = 0
for i in range(0, num):
    v = v + ax[i]*d_time
    vel.append(v)
vel = np.array(vel)

dy = vel * d_time

dist = []
d = 0
for i in range(0, num):
    d = d + dy[i]
    dist.append(d)

rot_angle = 2 * np.arcsin(yaw)

x = 0
y = 0
x_arr = []
y_arr = []
for i in range(0, num-1):
    x = x + dy[i+1] * np.sin(rot_angle[i])
    y = y + dy[i+1] * np.cos(rot_angle[i])
    x_arr.append(x)
    y_arr.append(y)

# real trajectory
real_coordinate_x = [0, 0, -6, -6]
real_coordinate_y = [0, 9.5, 9.5, 0]

'''
fig, plotting = plt.subplots()
plotting.set_title('Accelerations (m/s^2)')
line1, = plotting.plot(ax, color='red', label='x-axis')
line2, = plotting.plot(ay, color='blue', label='y-axis')
line3, = plotting.plot(az, color='green', label='z-axis')
plt.xlabel("time step")
plt.ylabel("Accelaration")
leg = plotting.legend(loc='upper left', fancybox=True, shadow=True)
plt.grid()
leg.get_frame().set_alpha(0.4)
plt.show()
'''
'''
plt.plot(ax)
plt.title("Accelaration  (m/s2)")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Accelaration")
plt.show()

plt.plot(ay)
plt.title("Accelaration y (m/s2)")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Accelaration")
plt.show()

plt.plot(az)
plt.title("Accelaration z (m/s2)")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Accelaration")
plt.show()

plt.plot(ax)
plt.title("Length of accel vector")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Length")
plt.show()
'''

'''
plt.plot(vel, color='black')
plt.title("Velocity in x-axis (m/s)")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Velocity")
plt.show()

plt.plot(dy, color='black')
plt.title("Displacement")
plt.grid()
plt.xlabel("time step")
plt.ylabel("Displacement")
plt.show()

plt.plot(dist, color='black')
plt.title("Total distance in meter")
plt.grid()
plt.xlabel("time step")
plt.ylabel("distance")
plt.show()

plt.plot(rot_angle, color='black')
plt.title("Rotational vector in radian")
plt.grid()
plt.xlabel("time step")
plt.ylabel("angle")
plt.show()
'''
'''
plt.scatter(x_arr, y_arr, color='black')
plt.title("Trajectory")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
'''

fig1, plotting = plt.subplots()
plotting.set_title('Trajectory')
plt.scatter(x_arr, y_arr, color='black', label='values from mpu-9265')
plt.plot(real_coordinate_x, real_coordinate_y, color='blue', label='real trajectory', linewidth=5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
leg = plotting.legend(loc='lower right', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)
plt.show()

