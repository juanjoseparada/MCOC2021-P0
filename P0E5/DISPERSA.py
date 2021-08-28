# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:17:18 2021

@author: juanp
"""

from numpy import float16
from time import perf_counter
import scipy.sparse as sparse
import matplotlib.pylab as plt

def laplaciana_dispersa(N, dtype):
    return 2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)

dtsolve= []
dtens = []
xo=perf_counter()
Ns = [1,7,15,25,50,150,200,450,700,1000,2500,3000,5000,8000,15000,20000,30000,40000,50000,70000,100000,150000,200000,300000,500000,1000000,2000000,5000000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana_dispersa(N, dtype = float16)
        B= laplaciana_dispersa(N, dtype = float16)
        t2=perf_counter()
        x = A@B
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

print(dt_formar)
print(dt_solve)


##################### GRAFICOS ################################################

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento Dispersa")
plt.ylabel("Tiempo de ensamblado")
y1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
valor1 = [0.0001,0.001,0.01,0.1,1,10,60,600]
n0xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,500000,1000000,2000000,5000000]

for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='o') 

inter = [3,10,100,400]
nombres = ["O(N)","O(N^2)","O(N^3)","O(N^4)"]
exp = [1,2,3,4]
for i in range(len(inter)):    
    plt.plot([inter[i],Ns[-1]],[dt_formar[0][0]**exp[i],max(dt_formar[-1])],linestyle = "--",label=nombres[i]) 
 

plt.axis([0,Ns[-1],0.0001,60])
plt.xticks(n0xvalue, [],rotation=45) 
plt.yticks(valor1,y1) 
plt.grid(True)

plt.subplot(2,1,2)
plt.ylabel("Tiempo de solucion") 

y2 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
valor2 = [0.0001,0.001,0.01,0.1,1,10,60]
for i in range(10):
    plt.loglog(Ns, dt_solve[i],marker='o') 


for i in range(len(inter)):    
    plt.plot([inter[i],Ns[-1]],[dt_formar[0][0]**exp[i],max(dt_formar[-1])],linestyle = "--",label=nombres[i]) #IMPORTANTE###################################################
    plt.legend(loc="lower left")
plt.axis([0,Ns[-1],0.0001,60])
plt.yticks(valor2,y2)

n3xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000]
plt.xticks(n3xvalue, n3xlabel,rotation=45) 
plt.xlabel("Tamaño matriz N")

plt.grid(True)
plt.savefig("Rendimiento Solve Dispersa.jpg")  