# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:07:28 2021

@author: juanp
"""


import numpy as np
from numpy import float64, double, ones
from numpy import zeros
import matplotlib.pylab as plt
from numpy import float16
from time import perf_counter
from scipy.sparse.linalg import spsolve

def laplaciana_llena(N, t=double):            #Laplaciana llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)


dtsolve= []
dtformar = []

Ns = [1,5,15,25,50,150,200,500,700,1000,2000,5000]

for i in range(10):
    for N in Ns:
        t1= perf_counter()
        
        A= laplaciana_llena(N, t = float64)
        B= ones(N)
        t2=perf_counter()
        x = spsolve(A,B)
        t3=perf_counter()
        
        dt_ensamblaje = t2-t1
        dt_solve = t3-t2
        
        dtformar.append(dt_ensamblaje)
        dtsolve.append(dt_solve)
    
def separar(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

dt_formar = list(separar(dtsolve, len(Ns)))
dt_solve = list(separar(dtformar, len(Ns)))


########################################### GRAFICOS ###########################################

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento Solve Llena")
plt.ylabel("Tiempo de ensamblado")
y1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
yy1 = [0.0001,0.001,0.01,0.1,1,10,60]#,600]
n0xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
n0xvalue = [10,20,50,100,200,500,1000,2000,5100]

for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='.',color="black",linewidth=0.5) 


plt.axhline(y=max(dt_formar[-1]), xmin=0, xmax=max(Ns),linestyle = "--",label="constante")


casos = ["O(N)","O(N)","O(N^3)","O(N^4)"]
exp = [1,2,3,4]
for i in range(4):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i]) 


plt.axis([1,max(Ns),0.0001,100])

plt.xticks(n0xvalue, [],rotation=45)
plt.yticks(yy1,y1) 


plt.subplot(2,1,2)
plt.ylabel("Tiempo de solucion") 

y2 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
yy2 = [0.0001,0.001,0.01,0.1,1,10,60]
for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='.',color="black",linewidth=0.5)
    
plt.axhline(y=max(dt_formar[-1]), xmin=0.1, xmax=max(Ns),linestyle = "--",label="constante")
plt.legend(loc="lower left")
  
exp = [1,2,3,4]
for i in range(4):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i]) 
    plt.legend(loc="lower left")


plt.axis([1,max(Ns),0.0001,100])

plt.yticks(yy2,y2)

n3xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
n3xvalue = [10,20,50,100,200,500,1000,2000,5100]
plt.xticks(n3xvalue, n3xlabel,rotation=45) 
plt.xlabel("Tamaño matriz N")


plt.savefig("Rendimiento Solve Llena")  


