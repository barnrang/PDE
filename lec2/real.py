import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import animation
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

dx = 0.1
dy = dx
dt = 0.1
alpha = 1.
grid_x = 100
grid_y = 100
nt = 100
d = 0.1
dt = d * (dx**2)/alpha

x = np.linspace(0,dx * (grid_x - 1), grid_x)
y = np.linspace(0,dy * (grid_y - 1), grid_y)
X,Y = np.meshgrid(x,y)


X_set = (40/grid_x * np.arange(0,grid_x))**2
Y_set = (40/grid_y * np.arange(0,grid_y))**2
cmap = plt.cm.get_cmap("jet")
cmap.set_over('grey')
T = np.zeros((grid_x,grid_y))
T += np.sqrt(X_set.reshape((grid_x,1)) + Y_set.reshape((1,grid_y)))
g = 0
levels = np.arange(0.,60.,0.2)
icount = 1
###for n in range(1,100):
###	plt.cla()
###	plt.clf()
###	Tn = T.copy()
###	T = Tn+d*(np.roll(Tn,1,axis=0)+np.roll(Tn,-1,axis=0)+np.roll(Tn,1,axis=1)+np.roll(Tn,-1,axis=1)-4*Tn)
###	plt.xlim(0.,np.max(x))
###	plt.ylim(0.,np.max(x))
###	cl = plt.contourf(X,Y,T,levels,cmap=cmap)
###	plt.colorbar(cl)
###	plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
###	plt.savefig('cyclic_%04i.jpg'%(icount))
###	icount += 1

#FIX WALL
def PDE(n):
	global T
	plt.cla()
	plt.clf()
	Tn = T.copy()
	left = np.roll(Tn,1,axis=0)
	right = np.roll(Tn,-1,axis=0)
	down = np.roll(Tn,1,axis=1)
	up = np.roll(Tn,-1,axis=1)
	left[0,:],right[grid_x-1,:],down[:,0],up[:,grid_y-1] = 0,0,0,0
	T = Tn+d*(up+down+right+left-4*Tn)
	T[0,1:grid_y-1] += d * Tn[1,1:grid_y-1]
	T[grid_x-1,1:grid_y-1] += d * Tn[grid_x-2,1:grid_y-1]
	T[1:grid_x-1,0] += d * Tn[1:grid_x-1,1]
	T[1:grid_x-1,grid_y-1] += d * Tn[1:grid_x-1,grid_y-2]
	plt.xlim(0.,np.max(x))
	plt.ylim(0.,np.max(x))
	cl = plt.contourf(X,Y,T,levels,cmap=cmap)
	plt.colorbar(cl)
	plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
	# plt.savefig('cyclic_%04i.jpg'%(icount))
	# icount += 1
fig = plt.figure()
a = animation.FuncAnimation(fig, PDE, frames = 100, interval=50)
plt.show()
