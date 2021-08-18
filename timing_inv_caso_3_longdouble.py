# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:47:26 2021

@author: juanp
"""


#-------------------------------------------CASO 3  LONGDOUBLE-------------------------------------

from numpy.linalg import inv
from time import perf_counter
from numpy import float32
from laplaciana import laplaciana
import numpy as np
from numpy import zeros, float16, float32,float64, longdouble
import matplotlib.pylab as plt
from scipy import linalg



dt_e1=[]
dt_i1=[]
bytes_t1=[]


Ns= [1,2,3,4,5,6,7,8,9,10,14,16,20,23,27,36,50,100,130,150,210,
     270,350,420,500,560,600,750,890,950,1000,5000]


texto= open(f"Rendimiento Caso 3, longdouble.txt", "w")

for i in range(10):
    
    for N in Ns:
        
# Con el metodo aprendido en clases llamamos a la funcion previamente creada        
        t1= perf_counter()
        A= laplaciana(N, dtype= longdouble)
        t2= perf_counter()
        
        C= linalg.inv(A, overwrite_a=True)
        
        t3= perf_counter()
        
        dt_ensamblaje= t2-t1
        dt_inversion= t3-t2
        bt= A.nbytes + C.nbytes
        
        dt_e1.append(dt_ensamblaje)
        dt_i1.append(dt_inversion)
        bytes_t1.append(bt)
        
        
        texto.write(f"{N}   {dt_ensamblaje}   {dt_inversion}   {bt}\n")
        
        print(f" {N}   {dt_ensamblaje}   {dt_inversion}   {bt}   ")
    
texto.close()
    
    
# ---------------------------------------------GRAFICAR-----------------------------------   
    
x= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2=["1 KB","10 KB","100 KB", "1 MB","10 MB","100 MB","1 GB","10 GB"]
tiempo1=[0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1= [10**3,10*10**3,100*10**3,10**6,10*10**6,100*10**6,10**9,10*10**9]
tamaño1= [10,20,50,100,200,500,1000,2000,5000,10000,20000]
   
N1=[] 
tiempo= []
memoria=[]
tamaño =[]

text= open("Rendimiento Caso 3, longdouble.txt", "r")
info= text.read()
info= info.split("\n")
info.pop(0)
info.pop(-1)

a= 0

while a<len(info):
    lista= info[a]
    lista= lista.split("   ")
    N1.append(float(lista[0]))
    tiempo.append(float(lista[1]))  
    tamaño.append(float(lista[2]))
    memoria.append(float(lista[3]))
    a+=1



plt.subplot(2,1,1)
plt.title("Rendimiento Inversa")

# Ahora graficamos el primero con un ciclo for para poder meter las 10 lineas
cant= int(len(info)/10)
N= int(N)
b=0



for i in range(11):
    for j in range(len(lista)+1):
        plt.loglog(N1[j:j+27], tiempo[j:j+27], "o-")
        
  
        
      
plt.xticks(tamaño1, ["", "", "", "", "", "", "", "", "", ""])
plt.yticks(tiempo1, y1)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.grid() 



plt.subplot(2,1,2)
plt.loglog(N1,memoria , "o-")
plt.hlines(y=8*10**9, xmin=0, xmax=20000,linestyle="--")
plt.grid()       
plt.xticks(tamaño1, x, rotation=45)
plt.yticks(memoria1, y2)
plt.xlim(right=20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso de Memoria")


plt.savefig("CASO 3 LONGDOUBLE")
plt.show()    