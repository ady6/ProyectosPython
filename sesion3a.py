#funciones

#funcion con parametros
def calcular(a,b):
    return(a*b)

total=calcular(10,3)
print(total)

#funcion sin parametros
def calcular():
    return(10*2)

print(calcular())

#funcion con varios parametros
def calcular(a,b,mensaje="calculando"):
    return mensaje + str(a*b)

total=calcular(10,3,"vamos a calcular ")
print(total)


"""
ejercicio

crea una función que retorna el  total de la venta
unidades
precio
si unidades >100, tienes un descuento de 10
por defecto tienes coste de envio +20

yo llamo a la función
juan - 120 - 7.95
return string cliente Juan : total = x (con/sin  descuento)

"""

def calcularTotal(unidades,precio,envio=20):
    total=0
    if(unidades>100):
        total=unidades*precio-10+envio
    else:
        total=unidades*precio+envio
    return total

total = calcularTotal(120,7.95)
print(f"cliente Juan {total}")


"""
Con operador ternario (if else, retorna true/false)

def calcularTotal(unidades,precio,envio=20):
    total=(unidades>100)if(unidades*precio-10+envio)else(unidades*precio+envio)
    return total

total = calcularTotal(120,7.95)
print(f"cliente Juan {total}")

"""