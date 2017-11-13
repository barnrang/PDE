import numpy as np
import matplotlib.pyplot as plt
import os
dir = os.path.dirname(os.path.realpath(__file__))
dt = 0.1
t = np.arange(0.,10.,dt)
x = np.linspace(0.,10.,100.)
y = np.zeros_like(x)

def pde(y):
    y += dt * dydt()
    return y

def dydt():
    return 1

for it in t:
    y = pde(y)
    plt.clf()
    plt.plot(x,y)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.savefig("test_%03i.jpg"%(it))