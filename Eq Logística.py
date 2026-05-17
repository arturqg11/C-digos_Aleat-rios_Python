import matplotlib.pyplot as plt

def logistica(r,x):
    L=[]
    for k in range(N):
        x=r*x*(1-x)
        L.append(x)
    return L[-32:]


x=1/2
N=500
NR=200
r=0
for j in range(NR):
    r=r+3.95/NR
    x=1/2
    xf = logistica(r,x)    
    
    plt.plot(32*[r],xf,'o')
plt.show()