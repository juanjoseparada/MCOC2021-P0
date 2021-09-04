# MCOC2021-P0

# Mi computador principal

* Marca/modelo: VivoBook_ASUSlaptop X571GT_X571GT
* Tipo: Notebook
* Año adquisición: 2020
* Procesador:
  * Marca/Modelo: Intel Core i5-8300H
  * Velocidad Base: 2.30 GHz
  * Velocidad Máxima: 2.304 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 2
  * Arquitectura: x86_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * L1d: 256KB
  * L1i: 256KB
  * L2: 1,0KB
  * L3: 8,0KB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 2667 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce GTX 1650
  * Memoria dedicada: 8118 MB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: ASUS
  * Tipo: SSD
  * Tamaño: 476,93 GB
  * Particiones: 3
  * Sistema de archivos: EXT4

  
* Dirección MAC de la tarjeta wifi: 40-EC-99-3C-AB-95 
* Dirección IP (Interna, del router): 192.168.0.52
* Dirección IP (Externa, del ISP): 190.160.0.14
* Proveedor internet: VTR Banda Ancha S.A.


Desempeño MATMUL

![image](https://user-images.githubusercontent.com/88350743/128542058-c9d29886-2e4e-44bb-876e-b860aae41838.png)


¿Cómo difiere del gráfico del profesor/ayudante?

Viendo los dos tipos de graficos, se puede ver una gran diferencia en los tiempos transcurridos al ejecutar el programa, esto se puede deber a la diferencia de computadores basicamente y la velocidad de estos para procesar los datos. Se pudo notar un tiempo de 0.1 ms mientras que en el mio se demoraba 0.1 s. Mi grafico tuvo un problema de ultimo segundo que pretendo no incluirlo en mis resultados, el cual unió el último trammo con el primero.


¿A qué se pueden deber las diferencias en cada corrida?

Se puede ver una diferencia en cada corrida debido a varias causas, de las cuales la principal que se me ocurre es el uso de memoria en diferentes actividades del computador, que al sobrepasar un nivel seguirá al siguiente, lo cual puede entorpecer el proceso y con esto generar varación en los tiempos de estos.


El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

En el grafico del tiempo transcurrido el comportamiento no es lineal, esto se debe a que al aumentar el tamaño de la matriz, suben la cantidad de operaciones que se estan realizando de forma exponencial,  por lo cual el tiempo también sube de forma exponencial. Por otra parte el segundo grafico tiene un comportamento lineal, ya que al aumentar las dimensiones de las matrices utilizadas también sube la cantidad de memoria necesaria, por lo que se comporta linealmente.


¿Qué versión de python está usando?

R: 3.8.3

¿Qué versión de numpy está usando?

R: 1.18.5

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.

![image](https://user-images.githubusercontent.com/88350743/128545404-1455afd5-4ecb-40a1-8a64-2dd0b4bf6d6d.png)




------------------------------------------------------------------DESEMPEÑO DE INV--------------------------------------------------------------------------

Primero que nada cabe recalcar lo que sucedio en el proceso, donde al trabajar con el caso 1 se notó que los tipos de datos half y longdouble no pudieron ser ejecutados debido a que la libreria numpy no los tiene incluidos. Por otro lado con la libreria Scipy el unico que actuó diferente fue el tipo longdouble, que al principio no corrió debido a que Python trabaja hasta los 64 bits y le estaba pidiendo 128, con lo cual se cambio el "float128" por "longdouble" al momento de importarlo y pudo correr el programa y entregar buenos rendimientos. 

También su pudo notar una gran diferencia entre el uso de distintas librerias, donde scypy actuó de forma mucho mas rápida que numpy. Y hablando mas en especifico de la libreria scypy se pudo notar que la función overwrite_a(True) se ejecuto de mejor manera que todos los otros procesos en los diferentes scripts.



PREGUNTAS

¿Que algoritmos de inversión cree que utiliza cada metodo (ver wiki)? Justifique

Librería Numpy: es ejecutado con numpy.linalg.solve(MAtrizNxN, I) donde se utiliza la factorización LU (Lapack) mediante solve. 

Librería Scipy:ejecutado con scipy.linalg.inv(), también utiliza Lapack pero  también es optimizado por Atlas y Blas. Debido a esto se demorá menos tiempo en entregar resultados, ya que procesa rapidamente funciones del algebra lineal como las que ocupamos ahora. 



¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

En este caso se pudo ver que el paralelismo en el proceso de ejecución actuó de buena manera, ya que se puede ver en la foto presente a continuación como estos se distribuyen el trabajo entre sí logrando tener un funcionamiento mas eficiente al momento de ejecutar el codigo


![image](https://user-images.githubusercontent.com/88350743/129986842-129a16fb-cd54-44e0-a5a2-507f26b87847.png)

------------------------------------------------------------P0E4    Desempeño EIGH y SOLVE----------------------------------------------------------------------------------------


Comentarios: 

Se pudo notar una subida en los tiempo en las matrices menores a 10. Esto ocurrió a ultimo momento, ya que se encontró el error pero no alcanzaba el tiempo para cambiarlo. Esto ocurre ya que al pasar el archivo de texto a una lista se llama a la función "pop()" la cual en las matrices pequeñas al eliminar el ultimo termino elimina un "elevado a..." lo cual hace que el exponente desaparezca haciendo que el tiempo transcurrido suba a esos valores. Ademas el computador demoro mas de lo esperado en los procesos, teniendo que dejar como tamaño maximo de matriz N=3000.



Preguntas:


2- La variavilidad del tiempo fue algo que se pudo notar hasta sin ver los graficos y resultados, ya que al momento de ejecutar el metodo Solve fue mucho mas rapido que al ocupar Eigh. 
Pero al evaluar el caso A, se pudo notar una demora mayor en el caso 1 y en el caso 6, ya que el overwrite_b actuó de forma menos eficiente.En el caso B , se pudo notar como el desempeño de Eigh fue notablemte mas lento, notando ademas una gran diferencia entre el caso 4 y 5.

3-  En el caso A fue notablemente mas rapido el caso 2 "assum_a="pos""
     En el caso B fue mas rapido el caso 3 con el overwrite_a= True, como se esperaba despues de la entrega anterior
     
     
4- Sí, pero también hay que asumir que el computador ocupará el paralelismo, con lo cual no afectaría tanto en el desempeño.

5- Sí, de hecho al ver el rendimiento de estos se pudo ver que actuaban todos al mismo tiempo. (Paralelismo)

6- Se pudo ver un comportamiento similar a la entrega anterior. Pero al correr Eigh se utilizó mas

----------------------------------------------------------------- P0E5 Matrices dispersas y complejidad computacional----------------------------------------------------------


Se utilizó la siguiente función para crear la matriz del tipo llena, logrando reutilizar la función ocupada en las entregas anteriores

```
def laplaciana(N, dtype):
     A = zeros((N,N) , dtype=dtype)
     for i in range(N):
         A[i,i] = 2
         for j in range(max(0,i-2),i):
             if abs(i-j) == 1:
                 A[i,j] = -1
                 A[j,i] = -1      
     return(A)

 ```
y para la  la matriz dispersa se ocupó el siguiente codigo con la función "eye" ya que para la matriz del tipo llena no lo pudo soportar por el tipo de dato utilizado  

 
 ```def laplaciana_dispersa(N, dtype):
    return 2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)
 ```   

Para esta entrega se ocupó nuevamente la operación MATMUL, donde se buscó poder ver la diferencias de tiempos transcurido en operaciones de tipo Solve realizadas entre matrices laplacianas llenas y dispersas. Después de realizar lo anterior se pudo notar una gran diferencia en los tiempos transcurridos al ocupar estos diferentes tipos de matrices, donde la matriz dipersa necesito muchisimo menos tiempo que la matriz llena. Esto hizo sentido inmediato ya que la matriz del tipo dispersa contiene menos numeros que la matriz llena, debido a que todos los números ceros son eliminados de esta, con lo cual ocupará mucho menos datos y necesitará realizar menos operaciones. Esto se pude notar facilmente en los graficos obtenidos de tiempo vs tamaño de matriz y mostrados a contianuacíón:

![Rendimiento Solve Lleno](https://user-images.githubusercontent.com/88350743/131203445-c6ef3f0c-75aa-4e3b-8072-bef5b08e266f.jpg)

![Rendimiento Solve Dispersa](https://user-images.githubusercontent.com/88350743/131203458-f6741b1b-a82a-4843-9e88-163c51a82350.jpg)

################################################################      P0E6     ############################################################################

Se editó la entrega P0E5, logrando que los graficos den lo que se pedía, obteniendo así:

![Rendimiento MATMUL Llena](https://user-images.githubusercontent.com/88350743/132075659-e925d22b-8c6d-4fd4-9d98-593df720e084.png)

![Rendimiento MATMUL Dispersa](https://user-images.githubusercontent.com/88350743/132075664-066e35b4-195b-4039-aa19-972074091670.png)


Luego se trabajó con los procesos de Solve e INV:


SOLVE:

![Rendimiento Solve Dispersa](https://user-images.githubusercontent.com/88350743/132075787-57292cbd-be42-42a3-a47b-bea3b8af6118.png)
![Rendimiento Solve Llena](https://user-images.githubusercontent.com/88350743/132075794-7d6a18ee-4f65-4355-9a6f-8c3294ae4a35.png)

Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.

La principal diferencia entre estos dos casos es el tiempo que se demora en ejecutar cada código. Donde se pudo notar que en el caso de matrices llenas se demora mucho mas en ejecutarlo, al contrario de las matrices dispersas, donde se pudo llegar a tamaños de matrices (Ns) muchísimos mas grandes. Esto se podría explicar debido a la cantidad de datos que cada algoritmo debe manejar, ya que las matrices dispersas eliminan todos los ceros que contiene la matriz, haciendo que la cantidad de datos sea mucho menor.

¿Cual parece la complejidad asintótica (para N→∞)  para el ensamblado y solución en ambos casos y porqué?

Llena: Se puede ver como al aumentar empieza a tener un comportamiento asintotico hacía O^N4, esto quiere decir que si duplicas el tamaño de tu N  y tu tiempo inicial es t, el nuevo tiempo será 2^(4)*t

Dispersa: Para este caso se puede ver como al aumentar empieza a tener un comportamiento asintotico hacía O^N3, esto quiere decir que si duplicas el tamaño de tu N  y tu tiempo inicial es t, el nuevo tiempo será 2^(3)*t

¿Como afecta el tamaño de las matrices al comportamiento aparente?

En el caso de las matrices llenas a partir del N=200 se empieza a notar una gran diferencia en el tiempo de solución, mientras que en las matrices dispersas no hay una diferencias tan notoria. Pero a simple vista se puede ver que las matrices dispersas son mucho mas rapidas


¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?

Son menos estables que en el caso INV, pero solamente se nota un poco de diferencia en ambas en las matrices de tamaños mas chicas, sobre todo las llenas ya que trabajan con menores tamaños, pero en las dispersas se notan mas estables desde N=5000 para arriba.



INV:

![Rendimiento INV Dispersa](https://user-images.githubusercontent.com/88350743/132075764-1110a6da-a194-48de-94a6-d81aaafce550.png)
![Rendimiento INV Llena](https://user-images.githubusercontent.com/88350743/132075770-28d455da-7837-4547-bc8c-36729a151c52.png)

Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.

La principal diferencia entre estos dos casos es el tiempo que se demora en ejecutar cada código. Donde se pudo notar que en el caso de matrices llenas se demora mucho mas en ejecutarlo, al contrario de las matrices dispersas, donde se pudo llegar a tamaños de matrices (Ns) muchísimos mas grandes. Esto se podría explicar debido a la cantidad de datos que cada algoritmo debe manejar, ya que las matrices dispersas eliminan todos los ceros que contiene la matriz, haciendo que la cantidad de datos sea mucho menor.



¿Cual parece la complejidad asintótica (para N→∞)  para el ensamblado y solución en ambos casos y porqué?

En ambos casos se puede ver como al aumentar empieza a tener un comportamiento asintotico hacía O^N4, esto quiere decir que si duplicas el tamaño de tu N  y tu tiempo inicial es t, el nuevo tiempo será 2^(4)*t

¿Como afecta el tamaño de las matrices al comportamiento aparente?

Afecta bastante, pero no como en el caso de los Solve. En este caso se pudo ver una gran diferencia ya que las dispersas trabajan con mucho menos datos (por que elimina los ceros), pero se puede ver un comportamiento mas lineal en el caso de las dispersas respecto al tiempo, al contrario de las matrices llenas, donde a subir los datos sube abruptamente el tiempo.



¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?

No se notan grandes diferencias entre las corridas. Las dispersas son muy estables, y en las llenas se puede ver un poco  mas diferencia entre las matrices de 10x10 y 200x200



