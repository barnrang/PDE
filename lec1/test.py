import numpy as np
prime = [2]

def checkprime(x):
    bound = np.sqrt(x)
    for j in prime:
        if x % j == 0:
            return 0
        if j > bound:
            return 1


for i in range(3,1000):
    if checkprime(i):
        prime.append(i)

print(prime)