import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from matplotlib import animation
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

dx = 0.1
dy = dx
a = 1.
v = 2.
grid_x = 100
grid_y = 100
nt = 100
d1 = 0.07
d2 = 0.05
dt = d2 * (dx**2)/v

def init():
    T = np.zeros((grid_x,grid_y))
    T[70:90, 70:90] = 80.
    return T

x = np.linspace(0,dx * (grid_x - 1), grid_x)
y = np.linspace(0,dy * (grid_y - 1), grid_y)
X,Y = np.meshgrid(x,y)
print(X,Y)
cmap = plt.cm.get_cmap("jet")
cmap.set_over('grey')
g = 0
levels = np.arange(0.,100.,0.2)
count = 1
icount = 0
T = init()
fig = plt.figure()
ax = fig.gca(projection='3d')
def cyc_var(n):
    global T,d1,d2
    ax.cla()
    #plt.clf()
    Tn = T.copy()
    left = np.roll(Tn,1,axis=0)
    right = np.roll(Tn,-1,axis=0)
    up = np.roll(Tn,-1,axis=1)
    down = np.roll(Tn,1,axis=1)
    T = Tn-dt*(np.sqrt(80**2 - Tn ** 2))/dx*(2 * Tn - left - down) + d2 * (left+right+up+down-4*Tn)
    ax.set_xlim(0.,np.max(x))
    ax.set_ylim(0.,np.max(y))
    ax.set_zlim(0.,300)
    cl = ax.plot_surface(X,Y,T,linewidth=0, cmap=cmap,antialiased=False)
    #fig.colorbar(cl)
    #ax.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
    # plt.savefig('cyclic_%04i.jpg'%(icount))
    # icount += 1

def cyc_con(n):
    global T,d1,d2
    plt.cla()
    plt.clf()
    Tn = T.copy()
    left = np.roll(Tn,1,axis=0)
    right = np.roll(Tn,-1,axis=0)
    up = np.roll(Tn,-1,axis=1)
    down = np.roll(Tn,1,axis=1)
    T = Tn-d1*(2 * Tn - left - down) + d2 * (left+right+up+down-4*Tn)
    plt.xlim(0.,np.max(x))
    plt.ylim(0.,np.max(x))
    cl = plt.contourf(X,Y,T,levels,cmap=cmap)
    plt.colorbar(cl)
    plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
    # plt.savefig('cyclic_%04i.jpg'%(icount))
    # icount += 1

def der_var(n):
    global T,d1,d2
    plt.cla()
    plt.clf()
    T[0,:],T[:,0], T[grid_x-1,:], T[:, grid_y-1] = 0,0,0,0
    Tn = T.copy()
    left = np.roll(Tn,1,axis=0)
    right = np.roll(Tn,-1,axis=0)
    up = np.roll(Tn,-1,axis=1)
    down = np.roll(Tn,1,axis=1)
    T = Tn-dt*(np.sqrt(80**2 - Tn ** 2))/dx*(2 * Tn - left - down) + d2 * (left+right+up+down-4*Tn)
    plt.xlim(0.,np.max(x))
    plt.ylim(0.,np.max(x))
    cl = plt.contourf(X,Y,T,levels,cmap=cmap)
    plt.colorbar(cl)
    plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))

def matpde(n):
    global T, icount
    plt.cla()
    plt.clf()
    Tn = T.copy()
    left = np.roll(Tn,1,axis=0)
    right = np.roll(Tn,-1,axis=0)
    up = np.roll(Tn,-1,axis=1)
    down = np.roll(Tn,1,axis=1)
    left[0,:],right[grid_x-1,:],up[:,grid_y-1],down[:,0] = 0,0,0,0
    T = Tn+d*(up+down+right+left-4*Tn)
    T[0,1:grid_y-1] = d * Tn[1,1:grid_y-1]
    T[grid_x-1,1:grid_y-1] += d * Tn[grid_x-1,1:grid_y-1]
    T[1:grid_x-1,0] += d * Tn[1:grid_x-1,1]
    T[1:grid_x-1,grid_y-1] += d * Tn[1:grid_x-1,grid_y-2]
    #T[0,0],T[0,grid_y-1],T[grid_x-1,0],T[grid_x-1,grid_y-1] = Tn[0,0], Tn[0,grid_y-1], Tn[grid_x-1,0],Tn[grid_x-1,grid_y-1]
    plt.xlim(0.,np.max(x))
    plt.ylim(0.,np.max(x))
    cl = plt.contourf(X,Y,T,levels,cmap=cmap)
    plt.colorbar(cl)
    plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))
    plt.savefig('neumann_%04i.jpg'%(icount))
    icount += 1
#fig = plt.figure()
a = animation.FuncAnimation(fig, cyc_var, frames=200,interval=100)
a.save('3d-var.mp4',fps=30,extra_args=['-vcodec','libx264'])
# for i in range(100):
#     matpde(1)
