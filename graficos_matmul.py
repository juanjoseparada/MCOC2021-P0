# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 22:05:20 2021

@author: juanp
"""

import matplotlib.pyplot as plt 
import numpy as np 

x= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2=["1 KB","10 KB","100 KB", "1 MB","10 MB","100 MB","1 GB","10 GB"]
tiempo1=[0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1= [10**3,10*10**3,100*10**3,10**6,10*10**6,100*10**6,10**9,10*10**9]
tamaño1= [10,20,50,100,200,500,1000,2000,5000,10000]


tiempo= []
memoria=[]
tamaño =[]

text= open("Rendimiento.txt", "r")
info= text.read()
info= info.split("\n")
info.pop(0)
info.pop(-1)

a= 0

while a<len(info):
    lista= info[a]
    lista= lista.split("   ")
    tiempo.append(float(lista[0]))
    memoria.append(float(lista[1]))
    tamaño.append(float(lista[2]))
    a+=1

plt.figure(1)
plt.subplot(2,1,1)
plt.title("Rendimiento A@B")

# Ahora graficamos el primero con un ciclo while para poder meter las 10 lineas
cant= int(len(info)/10)
b=0

for i in range(11):
    for j in range(cant):
        plt.loglog(tamaño[j*30:(j+1)*30], tiempo[j*30:(j+1)*30], "o-")
        
      
plt.grid()       
plt.xticks(tamaño1, ["", "", "", "", "", "", "", "", "", ""])
plt.yticks(tiempo1, y1)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")

plt.subplot(2,1,2)
plt.loglog(tamaño, memoria, "o-")
plt.hlines(y=8*10**9, xmin=0, xmax=20000,linestyle="--")
plt.grid()       
plt.xticks(tamaño1, x, rotation=45)
plt.yticks(memoria1, y2)
plt.xlim(right=20000)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso de Memoria")


plt.savefig("Rendimiento A@B")
plt.show()
print(np.__version__)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    