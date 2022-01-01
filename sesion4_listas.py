"""
listas : stack / queue / nested
https://docs.python.org/3/tutorial/datastructures.html
"""

#python utiliza las listas como stacks
users=["juan","laura"]
print(users)
users.append("maria")
print(users)
users.pop()
print(users)

#python con queues
from collections import deque
usuarios=deque(["juan","laura"])
print(usuarios)
usuarios.append("maria")
usuarios.popleft()
print(usuarios)


matrix=[
    ["maria","sevilla","valencia"],
    ["roma","milán","bolonia"],
    ["paris","niza","marsella"],
    ["londres","liverpool","newcastle"]
]

print(matrix)
for item in matrix:
    for ciudad in item:
        print(len(ciudad))


#almacenar por equipo los puntos q tiene en la liga: 5 equipos te los inventas y les pones puntos
#tupla cuidado, son inmutables
liga = {
    "Atleti":8,
    "Barcelona":17,
    "Real Madrid":28,
    "Malaga":15,
    "Betis":10
    }

for key in liga:
    print (key, ":", liga[key])

#reto1: ordenados por puntos

orden=sorted(liga.items(),key=lambda i:i[1], reverse=True) #i:i[1] ordena por puntos, [0] nombres
print(orden)

for i in orden:
    print(i[0]," - ", i[1])

#reto2: el primero tiene 2 puntos más, modificar los puntos

liga["Atleti"]=65 #diccionario es mutable, puede cambiar su valor
print(liga)