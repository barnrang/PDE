import numpy as np
import matplotlib.pyplot as plt
import os
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)

L = 100 
dim = 100
dx = 1
dt = 0.1
alpha = None
dim = len(np.linspace(0,L,dim))
T = np.arange(0,10,dt)
U1 = np.zeros((dim+2,dim+2))
G = 0.1

def U(U1):
	U_r = np.zeros_like(U1)
	for x in (1,dim+1):
		for y in (1,dim+1):
			U_r[x,y] = -alpha * dt/(dx**2)*(U1[x+1,y]+U1[x-1,y]\
			+U1[x,y+1]+U1[x,y-1]-4*U1[x,y])+U1[x,y]
	return U_r

def addbound(U):
	for i in range(1,dim+1):
		U[i,0] = U[i,1] - 2 * dx * G
		U[i,dim+1] = U[i,dim] - 2 * dx * G
		U[
for t in range(T):
		
