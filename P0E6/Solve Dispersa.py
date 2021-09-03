# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:17:07 2021

@author: juanp
"""


import numpy as np
from numpy import double, float64, ones
from scipy import sparse
from time import perf_counter
from scipy.sparse.linalg import spsolve
import matplotlib.pylab as plt

def laplaciana_dispersa(N, t=double):                                    #Laplaciana dispersa
    e = sparse.eye(N, dtype=t)-sparse.eye(N,N,1,dtype=t)
    return e+e.T



dtsolve= []
dtens = []
xo=perf_counter()
Ns = [1,7,15,25,50,150,200,450,700,1000,2500,3000,5000,8000,15000,20000,30000,40000,50000,70000,100000,150000,200000,300000,500000,1000000,2000000,5000000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana_dispersa(N, t = float64)
        B= ones(N)
        t2=perf_counter()
        x = spsolve(A,B)
        t3=perf_counter()
        
        dt_ensamblaje = t2-t1
        dt_solve = t3-t2
        dtens.append(dt_ensamblaje)
        dtsolve.append(dt_solve)

dt_s = []

    
def separar(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

dt_formar = list(separar(dtsolve, len(Ns)))
dt_solve = list(separar(dtens, len(Ns)))

##################### GRAFICOS ################################################

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento Solve Dispersa")
plt.ylabel("Tiempo de ensamblado")
palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
valor1 = [0.0001,0.001,0.01,0.1,1,10,60]
n0xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
n0xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,500000,1000000,2000000,5000000]

for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='.',color="black",linewidth=0.5) 

plt.axhline(y=max(dt_formar[-1]), xmin=0, xmax=max(Ns),linestyle = "--",label="constante")


cortes = [3,10,100,400]
casos = ["O(N)","O(N)","O(N^3)","O(N^4)"]
exp = [1,2,3,4]
for i in range(len(cortes)):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i]) 



plt.axis([1,max(Ns),0.00001,80])

plt.xticks(n0xvalue, [],rotation=45) 
plt.yticks(valor1,palabras1) 


plt.subplot(2,1,2)
plt.ylabel("Tiempo de solucion") 

palabras2 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
valor2 = [0.0001,0.001,0.01,0.1,1,10,60]
for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='.',color="black",linewidth=0.5) 
    
    
plt.axhline(y=max(dt_formar[-1]), xmin=0.1, xmax=max(Ns),linestyle = "--",label="constante") 
plt.legend(loc="lower left")

  
cortes = [3,10,100,400]
exp = [1,2,3,4]
for i in range(len(cortes)):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i])
    plt.legend(loc="lower left")



plt.axis([1,max(Ns)+2000000,0.00001,80])

plt.yticks(valor2,palabras2)

n3xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000]
plt.xticks(n3xvalue, n3xlabel,rotation=45) 
plt.xlabel("Tamaño matriz N")

plt.savefig("Rendimiento Solve Dispersa")  

