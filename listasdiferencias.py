
#Collections en Python


"""
Listas
"""
print("Listas-------------------")
lista=["juan", True, 15, 17.9, 'madrid'] #lista soporta cualquier tipo de dato
print(lista)
lista[1]="dato cambiado" #lista es mutable: el value de sus elementos puede cambiar
print(lista)
lista.sort()


"""
Tuplas
"""
print("Tuplas-------------------")
tupla=("juan", True, 15, 17.9, 'madrid') #tupla soporta cualquier tipo de dato
print(tupla)
#tupla[1]="tupla cambiada" #tupla es inmutable: el value de sus elementos no puede cambiar
#print(tupla)


"""
Sets - conjuntos
"""
print("Conjuntos-------------------")
conjunto={"juan", True, 15, 17.9, 'madrid'} #conjunto soporta cualquier tipo de dato
print(conjunto)
#conjunto[1]="dato cambiado" #conjunto es mutable pero no puedo acceder a un elemento pq no está ordenado
#conjunto no soporta duplicados
conjunto.add("añadido") #set no es inmutable, se puede añadir / eliminar elementos
print(conjunto)
lista2=list(conjunto) #el conjunto no puede ordenarse, pero se puede convertir en lista
lista2.sort()



"""
Dictionary
"""
print("Diccionarios-------------------")
diccionario={"item1":"juan", "item2":True, "item3":15, "item4":17.9, "item5":'madrid'} #diccionario soporta cualquier tipo de dato
print(diccionario)
diccionario["item2"]="dato cambiado" #dictionary es mutable desde key
print(diccionario)
diccionario.update({"item6":"otro dato"}) #añadir elementos a un diccionario
