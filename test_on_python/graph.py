from mpl_toolkits.mplot3d import Axes3D
import pylab
import numpy as np
def generate_point(L, t):
	x = L[0] + L[3] * t
	y = L[1] + L[4] * t
	z = L[2] + L[5] * t
	return [x, y, z]

def generate_line(L, T):
	X = L[0] + L[3] * T
	Y = L[1] + L[4] * T
	Z = L[2] + L[5] * T
	return [X, Y, Z]

a = -1
b = 4
T = np.arange(a, b, 0.3)
L1 = [-3, -1, -7, -18, 19, 4]
L2 = [-18, 18, -8, 6, 15, 10]
L3 = [6, 14, -2, -18, 13, 3]
P1 = generate_line(L1, T)
P2 = generate_line(L2, T)
P3 = generate_line(L3, T)
fig = pylab.figure()
pylab.ion()
for i in range(100):
	pylab.pause(0.1)
	pylab.clf()
	
	ax = fig.gca(projection='3d')
	t = a + i * (b - a) / 100
	ax.scatter(*generate_point(L1, t))
	ax.scatter(*generate_point(L2, t))
	ax.scatter(*generate_point(L3, t))
	ax.plot(*P1, label = 'line 1')
	ax.plot(*P2, label = 'line 2')
	ax.plot(*P3, label = 'line 3')
	pylab.draw()
pylab.close()