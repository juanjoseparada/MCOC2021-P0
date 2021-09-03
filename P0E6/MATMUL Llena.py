# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:31:12 2021

@author: juanp
"""

from numpy import zeros
import matplotlib.pylab as plt
from numpy import float16
from time import perf_counter


 # Se crea laplaciana como las entregas anteriores
def laplaciana(N, dtype):
    A = zeros((N,N) , dtype=dtype)
    
    for i in range(N):
        A[i,i] = 2
        for j in range(max(0,i-2),i):
            if abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1      
    return(A)


dtsolve= []
dtformar = []
xo = perf_counter()
Ns = [1,5,15,25,50,150,200,500,700,1000]

for i in range(10):
    for N in Ns:
        t1= perf_counter()
        
        A= laplaciana(N, dtype = float16)
        B= laplaciana(N, dtype = float16)
        t2=perf_counter()
        x = A@B
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
plt.title("Rendimiento MATMUL Dispersa")
plt.ylabel("Tiempo de ensamblado")
palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]
valor1 = [0.0001,0.001,0.01,0.1,1,10,60]
n0xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000"]
n0xvalue = [10,20,50,100,200,500,1100]

for i in range(10):
    plt.loglog(Ns, dt_formar[i],marker='.',color="black",linewidth=0.5)

plt.axhline(y=max(dt_formar[-1]), xmin=0, xmax=max(Ns),linestyle = "--",label="constante")


cortes = [3,10,100,400]
casos = ["O(N)","O(N)","O(N^3)","O(N^4)"]
exp = [1,2,3,4]
for i in range(len(cortes)):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i])




plt.axis([1,max(Ns),0.000001,100])

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

exp = [1,2,3,4]
for i in range(4):    
    plt.plot([min(dt_formar[-1]),max(Ns)],[min(dt_formar[-1])**exp[i],max(dt_formar[-1])],linestyle = "--",label=casos[i]) 
    plt.legend(loc="lower left")



plt.axis([1,max(Ns),0.000001,100])

plt.yticks(valor2,palabras2)

n3xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000"]
n3xvalue = [10,20,50,100,200,500,1100]
plt.xticks(n3xvalue, n3xlabel,rotation=45) 
plt.xlabel("Tamaño matriz N")

plt.savefig("Rendimiento MATMUL Llena")  


