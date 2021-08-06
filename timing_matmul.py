# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:26:17 2021

@author: juanp
"""

from numpy import zeros
from time import perf_counter

text= open("Rendimiento.txt", "w")
text.write("Tiempo[s]   Memoria[bytes]   Tamaño   \n")

a=0
lista= []
tiempo= []
memoria=[]
tamaño= []
while a<10:
    N= [1,2,4,6,8,12,48,80,130,170,250,300,400,500,
        600,700,800,950,1200,1500,1800,2000,2250, 2500,
        3000,3500,4000,5000,6500,7500,10000]

    b=0
    while b<len(N):  
        A = zeros((N[b], N[b]))+1
        B = zeros((N[b], N[b]))+2
        
        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()
        mem= A.nbytes + B.nbytes + C.nbytes    
        dt = t2 - t1
        # vemos que cumpla con el tiempo menor a 2 minutos y que tampoco exceda la memoria Ram del PC
        if dt>120:
            break
        if mem> 6000000000:
            break
        print (f"dt= {dt} s")
        print (f"mem= {mem} bytes")
        print (f"N= {N[b]}") 
        print ()
        print ()
        print ()
        text.write(f"{dt}   {mem}   {N[b]}   \n")
        tiempo.append(dt)
        memoria.append(mem)
        tamaño.append(N[b])
        b+=1
    cont=0
 # "while cont<b:
  #      text.write(f"{tiempo[cont]}   {memoria[cont]}   {tamaño[cont]}   \n")  
   #     cont+=1    """
    a+=1
      
# Ahora abro abro archivo Text para poder agregar lo obtenido



text.close()









