"""
SQLite: bbdd server-less que se puede utilizar en casi todos los lenguajes de programación
server-less significa que no hay necesidad de instalar un servidor separado para trabajar con SQLite para que
pueda conectarse directamente con la bbdd
en principio no se requiere tener más que Python instalado para poder trabajar con SQLite
"""
#primero hay que importar el módulo 'sqlite3'
import sqlite3

"""
para crear o abrir una conexión con una bbdd existente creo un objeto de conexión y llamo a la función 'connect' del módulo 'sqlite3'
la primera vez que ejecuto este programa como no existe la bbdd 'tienda.db' se crea
consiste en un único archivo que se localiza en la misma carpeta de mi aplicación (tienda.db)
"""
conexion = sqlite3.connect('tienda.db')

#creo tabla en un try/except debido a que si ejecuto por segunda vez este programa
#se tratará de crear nuevamente la tabla 'clientes' y al ya existir se genera una excepción de tipo 'OperationalError'
try:
    #bloque de código donde creo tabla y sus campos
    conexion.execute("""create table clientes (
                              id integer primary key autoincrement,
                              nombre text,
                              apellido text,
                              email text,
                              telefono int,
                              productoPedido text,
                              precioProducto float
                        )""")
    print("SE HA CREADO LA TABLA CLIENTES") #informo que se ha creado la tabla
except sqlite3.OperationalError:
    #si ocurre esta excepción informo que la tabla ya existe
    #esto nunca ocurrirá ya que al final del programa siempre la elimino para evitar duplicados durante las ejecuciones
    print("LA TABLA CLIENTES YA EXISTE")

"""
llamo a execute y le paso como primer parámetro un comando SQL 'insert' que añade datos a la tabla
con el caracter '?' indico las posiciones donde se van a sustituir
el segundo parámetro es una tupla con los datos que se utilizarán en la sustitución
"""
#CRUD: INSERT
conexion.execute("insert into clientes(nombre,apellido,email,telefono,productoPedido,precioProducto) values (?,?,?,?,?,?)",
                ("Rocío", "Sánchez", "rociosanchez@gmail.com", 672730495, "Ordenador", 1050.99))
conexion.execute("insert into clientes(nombre,apellido,email,telefono,productoPedido,precioProducto) values (?,?,?,?,?,?)",
                ("Pepe", "Hurtado", "pepehurtado@hotmail.es", 672639229, "Televisor", 2350.85))
conexion.execute("insert into clientes(nombre,apellido,email,telefono,productoPedido,precioProducto) values (?,?,?,?,?,?)",
                ("Diego", "Troyano", "diegotroyano@gmail.com", 671934758, "Ordenador", 3400.27))
conexion.execute("insert into clientes(nombre,apellido,email,telefono,productoPedido,precioProducto) values (?,?,?,?,?,?)",
                ("Andrea", "García", "andreagarcia@campusfp.es", 673789932, "Monitor", 345.99))
conexion.execute("insert into clientes(nombre,apellido,email,telefono,productoPedido,precioProducto) values (?,?,?,?,?,?)",
                ("Andrés", "Roldán", "andresroldan@gmail.com", 672736541, "Teclado", 45.95))
conexion.commit() #guarda todos los cambios

#ejecuto un 'select' en la tabla 'clientes' para que retorne todas sus filas
#cursor: estructura de control que permite atravesar los registros de una bbdd, facilita el procesamiento posterior junto con el recorrido
print('\n\nCRUD: SELECT\n----------------------------------------------------------------------------')
print('TODAS LAS FILAS DE LA TABLA')
cursor=conexion.execute("SELECT * FROM clientes") #uso un cursor para recorrer el conjunto de filas de la tabla
for fila in cursor: #muestro cada fila de la tabla recorriendola con un bucle
    print(fila)

print('\nNOMBRE, APELLIDO Y EMAIL DE LOS CLIENTES QUE HAN PEDIDO UN ORDENADOR')
cursor=conexion.execute("SELECT nombre,apellido,email FROM clientes WHERE productoPedido='Ordenador'")
for fila in cursor:
    print(fila)

print('\nCLIENTES CON PEDIDOS DE MAS DE 1000€ ORDENADOS POR PRECIO')
cursor=conexion.execute("SELECT * FROM clientes WHERE precioProducto >= 1000 ORDER BY precioProducto DESC")
for fila in cursor:
    print(fila)

print('\nMOSTRAR EL NOMBRE Y EMAIL DE LOS CLIENTES QUE USAN GMAIL')
cursor=conexion.execute("SELECT nombre,email FROM clientes WHERE email LIKE '%gmail.com'")
for fila in cursor:
    print(fila)

print('\nMOSTRAR EL NOMBRE, APELLIDO Y TELEFONO DE LOS CLIENTES CUYO TELEFONO NO CONTENGA EL PREFIJO 672+')
cursor=conexion.execute("SELECT nombre, apellido,telefono FROM clientes WHERE NOT telefono LIKE '672%'")
for fila in cursor:
    print(fila)

#ejecuto un 'update' en la tabla 'clientes' para sustituir el monitor que pidió Andrea por un Ratón
#para ello busco al cliente a través de su correo y modifico el campo de productoPedido
conexion.execute('UPDATE clientes SET productoPedido = "Ratón" WHERE email = "andreagarcia@campusfp.es"')
conexion.commit() #guardo los cambios
print('\n\nCRUD: UPDATE\n----------------------------------------------------------------------------')
print('COMPRUEBO QUE EL CLIENTE ANDREA HA SIDO MODIFICADO CORRECTAMENTE')
cursor=conexion.execute("SELECT * FROM clientes WHERE email = 'andreagarcia@campusfp.es'")
for fila in cursor:
    print(fila)

#ejecuto un 'delete' en la tabla 'clientes' para eliminar a los clientes que hayan pedido un ordenador
#para ello les busco a traves del producto que han pedido (ordenador) y les elimino
conexion.execute('DELETE FROM clientes WHERE productoPedido = "Ordenador"')
conexion.commit() #guardo los cambios
print('\n\nCRUD: DELETE\n----------------------------------------------------------------------------')
print('COMPRUEBO QUE LOS CLIENTES QUE PIDIERON UN ORDENADOR HAN SIDO ELIMINADOS CORRECTAMENTE')
cursor=conexion.execute("SELECT * FROM clientes")
for fila in cursor:
    print(fila)

#para finalizar el programa elimino la tabla para evitar duplicados en caso de que se ejecute mas de una vez
cursor=conexion.execute("drop table clientes")

#por ultimo cierro la conexion
conexion.close()