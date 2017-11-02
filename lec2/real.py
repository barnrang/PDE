import numpy as np
import matplotlib.pyplot as plt
import os
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

dx = 0.1
dy = dx
dt = 0.6
alpha = 1.
grid_x = 100
grid_y = 100
nt = 100
d = 1
dt = d * (dx**2)/alpha

x = np.linspace(0,dx * (grid_x - 1), grid_x)
y = np.linspace(0,dy * (grid_y - 1), grid_y)
X,Y = np.meshgrid(x,y)

cmap = plt.cm.get_cmap("jet")
cmap.set_over('grey')
T = np.zeros((grid_x,grid_y))
g = 0
T[40:60,40:60] = 50.
levels = np.arange(0.,100.,0.2)
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
for n in range(1,100):
	plt.cla()
	plt.clf()
	Tn = T.copy()
	T = Tn+d*(np.roll(Tn,1,axis=0)+np.roll(Tn,-1,axis=0)+np.roll(Tn,1,axis=1)+np.roll(Tn,-1,axis=1)-4*Tn)
	plt.xlim(0.,np.max(x))
	plt.ylim(0.,np.max(x))
	cl = plt.contourf(X,Y,T,levels,cmap=cmap)
	plt.colorbar(cl)
	plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
	plt.savefig('cyclic_%04i.jpg'%(icount))
	T[0,:],T[:,0],T[grid_x-1,:],T[:,grid_y-1] = T[1,:]+g*dx*2,T[:,1]+g*dx*2,T[grid_x-2,:]+g*dx*2,T[:,grid_y-2]+g*dx*2 
	icount += 1
