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

