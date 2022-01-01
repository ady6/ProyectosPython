#comentario de linea

"""
Listas y definir tipos de funciones
"""

def bucle(dato):
    for i in range(dato):
        print(i)

bucle(15)


#muestra el total de los primeros 100 numeros
print(sum(range(101)))

#numeros primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')


#rango
for i in range(10):
    if (i!=5):
        print(i)
    else:
        break


#actividad1 explica diferencia entre range y enumerate con un ejemplo

"""
Range sirve para iterar una lista de elementos
Enumerate sirve para iterar una lista de elementos junto con el indice de cada elemento
"""

#range secuencia de números para utilizar en un bucle
print(list(range(0,20,4)))

#enumerate permite recorrer objetos con un iterator
paises=["Italia", "Francia", "España", "Portugal"]



#actividad2 cómo puedes sumar los primeros 100 números usando js

"""
var contador=0;
for (x=0; x<=100; x++) {
    contador=contador+x;
}
alert('La suma de los primeros 100 números naturales es '+contador);
"""

total=0 #acumulador
for i in range(101): #iterador, contador es i
    total=total+1
print(total)

#actividad2a : sumar 100 números gauss método

print(sum(range(101)))


#actividad3: crea una lista con 5 ciudades. Muestra el total de caracteres de cada ciudad
#si la ciudad tiene más de 10 caracteres NO la pintas

ciudades = ['Madrid','Barcelona','Málaga','CiudadLarga','Valencia']
for ciudad in ciudades:
    if (len(ciudad)<10):
        print(ciudad)
        print(len(ciudad))



