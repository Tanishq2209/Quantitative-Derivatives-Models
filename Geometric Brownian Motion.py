import numpy as np
import matplotlib.pyplot as plt

def GeneratePaths_GBM_ABM(m,n,T,r,sigma,S0):    
    
    # Fixing random seed
    np.random.seed(42)
        
    Z = np.random.normal(0.0,1.0,[m,n]) # Here m is no. of paths and n is no. of steps
    X = np.zeros([m, n+1])
    S = np.zeros([m, n+1])
    time = np.zeros([n+1])
        
    X[:,0] = np.log(S0)
    
    dt = T / n
    for i in range(0,n):
        # making sure that samples from normal have mean 0 and variance 1
        if m > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
            
        X[:,i+1] = X[:,i] + (r - 0.5 * sigma **2 ) * dt + sigma * np.power(dt, 0.5)*Z[:,i]
        time[i+1] = time[i] +dt
        
    #Compute exponent of ABM
    S = np.exp(X)
    paths = {"time":time,"X":X,"S":S}
    return paths

# Example case
m = 25
n = 500
T = 1
r = 0.05
sigma = 0.25
S0 = 100
    
Paths = GeneratePaths_GBM_ABM(m, n, T,r,sigma,S0)
timeGrid = Paths["time"]
X = Paths["X"]
S = Paths["S"]
    
plt.figure(1)
plt.plot(timeGrid, np.transpose(X))   
plt.grid()
plt.xlabel("time")
plt.ylabel("X(t)")
    
plt.figure(2)
plt.plot(timeGrid, np.transpose(S))   
plt.grid()
plt.xlabel("time")
plt.ylabel("S(t)")
