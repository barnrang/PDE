import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import animation
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

dx = 0.1
dy = dx
alpha = 1.
grid_x = 100
grid_y = 100
nt = 100
d = 0.1
dt = d * (dx**2)/alpha




def plot_activate(X,Y,n):
    global T
    plt.cla()
    plt.clf()
    plt.xlim(0.,np.max(x))
    plt.ylim(0.,np.max(x))
    cl = plt.contourf(X,Y,T,levels,cmap=cmap)
    plt.colorbar(cl)
    plt.text(np.max(x)*0.8,np.max(y)+dy,"t=%01.5f"%(dt*n))

# def init():
#     T = np.zeros((grid_x,grid_y))
#     T[20:45, 40:60] = 80.
#     T[55:80, 40:60] = 80.
#     return T

def init():
    T = np.zeros((grid_x,grid_y))
    T[70:grid_x, 70:grid_y] = 80
    return T

x = np.linspace(0,dx * (grid_x - 1), grid_x)
y = np.linspace(0,dy * (grid_y - 1), grid_y)
X,Y = np.meshgrid(x,y)

cmap = plt.cm.get_cmap("jet")
cmap.set_over('grey')
g = 0
levels = np.arange(0.,100.,0.2)
count = 1
icount = 0
T = init()
def cyc(n, plot=True):
    global T, icount
    Tn = T.copy()
    T = Tn+d*(np.roll(Tn,1,axis=0)+np.roll(Tn,-1,axis=0)+np.roll(Tn,1,axis=1)+np.roll(Tn,-1,axis=1)-4*Tn)
    if plot:
        plot_activate(X,Y,n)
    icount += 1

def dir(n,plot=True):
    global T, icount
    T[0,:], T[:,0], T[grid_x-1,:], T[:,grid_y-1] = 0,0,0,0
    Tn = T.copy()
    T = Tn+d*(np.roll(Tn,1,axis=0)+np.roll(Tn,-1,axis=0)+np.roll(Tn,1,axis=1)+np.roll(Tn,-1,axis=1)-4*Tn)
    if plot:
        plot_activate(X,Y,n)
    icount += 1

#FIX WALL
def neu(n, g=0,plot=True):
    global T, icount
    Tn = T.copy()
    left = np.roll(Tn,1,axis=0)
    right = np.roll(Tn,-1,axis=0)
    up = np.roll(Tn,-1,axis=1)
    down = np.roll(Tn,1,axis=1)
    left[0,:],right[grid_x-1,:],up[:,grid_y-1],down[:,0] = 0,0,0,0
    T = Tn+d*(up+down+right+left-4*Tn)
    T[0,1:grid_y-1] += d * ((-2 * dx * g + Tn[1,1:grid_y-1]) > 0) * (-2 * dx * g + Tn[1,1:grid_y-1])
    T[grid_x-1,1:grid_y-1] += d * ((-2 * dx * g+Tn[grid_x-2,1:grid_y-1]) > 0) * (-2 * dx * g+Tn[grid_x-2,1:grid_y-1])
    T[1:grid_x-1,0] += d * ((-2 * dx * g+Tn[1:grid_x-1,1]) > 0) * (-2 * dx * g+Tn[1:grid_x-1,1])
    T[1:grid_x-1,grid_y-1] += d * ((-2 * dx * g+Tn[1:grid_x-1,grid_y-2]) > 0) * (-2 * dx * g+Tn[1:grid_x-1,grid_y-2])
    if plot:
        plot_activate(X,Y,n)
    icount += 1
# fig = plt.figure()
# a = animation.FuncAnimation(fig, dir,frames=200,interval=10)
# #plt.show()
# a.save('dir.mp4',fps=30,extra_args=['-vcodec','libx264'])
n = 100000
for i in range(n):
    cyc(1,False)
plot_activate(X,Y,n)
plt.savefig('cyc/cyc-end.jpg')
print('cyc-end-heat-sum:%03.5f'%(np.sum(T)))
T = init()
for i in range(n):
    dir(1,False)
plot_activate(X,Y,n)
plt.savefig('dir/dir-end.jpg')
print('dir-end-heat-sum:%03.5f'%(np.sum(T)))
T = init()
for i in range(n):
    neu(1,plot = False)
plot_activate(X,Y,n)
plt.savefig('neu/neu-d-endi-s.jpg')
print('neuG0-end-heat-sum:%03.5f'%(np.sum(T)))
T = init()
for i in range(n):
    neu(1,20,False)
plot_activate(X,Y,n)
plt.savefig('neu/neuG-end.jpg')
print('neuG20-end-heat-sum:%03.5f'%(np.sum(T)))
