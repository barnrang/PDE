import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from matplotlib import animation
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)
dx = 1.
model = np.arange(0,100 + dx, dx)
f = np.zeros_like(model)
g = np.zeros_like(model)
f[40:60] = 1.
g[40], g[60] = 1./dx, -1./dx
C = 0.9
u = 1.
dt = np.abs(C * dx/u)

def plot_line(n):
    global model,f
    plt.clf()
    plt.cla()
    plt.ylim(-.5,1.5)
    plt.plot(model,f)
    plt.text(80.,1.51,'t=%05.2f'%(n))

def upwind(n):
    global f
    fn = f.copy()
    usign = int(np.sign(u))
    f = fn + C * (np.roll(fn,usign,0)-fn)
    plot_line(n)

def lex(n):
    global f
    fn = f.copy()
    c = fn
    b = 1/(2*dx) * (np.roll(fn,-1,0) - np.roll(fn,1,0))
    a = 1/(2*dx**2) * (np.roll(fn,-1,0) - 2*fn + np.roll(fn,1,0))
    f = a * (u*dt)**2 - b*(u*dt) + c
    plot_line(n)

def cip(n):
    global f,g
    fn = f.copy()
    gn = g.copy()
    usign = np.int(np.sign(u))
    x_iiup = (-usign*dx)
    a = -2*(np.roll(fn,usign,0)-fn)/x_iiup**3 + (gn + np.roll(gn,usign,0))/x_iiup**2
    b = -3*(-np.roll(fn,usign,0)+fn)/x_iiup**2 - (2*gn + np.roll(gn,usign,0))/x_iiup
    eps = -u*dt
    f = a * eps**3 + b*eps**2+gn*eps+fn
    g = (3*a*eps**2+2*b*eps+gn)
    plot_line(n)

fig = plt.figure()
a = animation.FuncAnimation(fig, cip, frames=200,interval=10)
plt.show()