import matplotlib.pyplot as plt 
import numpy as np

def poligonoin(r,n):
    
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    t = 0
    dt = 2*np.pi/n
    
    for i in range(n+1):
        
        x[i] = r*np.cos(t)
        y[i] = r*np.sin(t)
        t = t+dt
        
    plt.plot(x,y,'-.')
    return r

def circulo(r):
    n=500
    
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    t = 0
    dt = 2*np.pi/n
    
    for i in range(n+1):
        
        x[i] = r*np.cos(t)
        y[i] = r*np.sin(t)
        t = t+dt
        
    plt.plot(x,y,'-')
    return r
    
def poligonoc(r,n):
    r1 = r/(np.cos(np.pi/n))
    
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    
    t = 0
    dt = 2*np.pi/n
    
    for i in range(n+1):
        
        x[i] = r1*np.cos(t)
        y[i] = r1*np.sin(t)
        t = t+dt
        
    plt.plot(x,y,'-.')
    return r1
    
r=1
for i in range(3,1000):
    r = poligonoc(circulo(r),i)

print(r)
plt.show()