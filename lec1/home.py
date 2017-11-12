import numpy as np

dist = 1
dim = len(np.linspace(0,100,dist))
board = np.zero((dim,dim))

def init(board):
    return board

def T(x,y,t):
    
