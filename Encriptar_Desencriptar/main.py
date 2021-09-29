"""
crea una función en Python que le pida dos parámetros
un parámetro es texto a cifrar
segundo parámetro es la clave de paso : número
retorna el texto encriptado

"""

#funcion para encriptar
def encriptar(texto, posicion):

    texto_encriptado = ""
    for c in texto:
        numero=ord(c)+posicion
        print(numero)
        print(chr(numero))

#funcion para desencriptar
def desencriptar(texto,posicion):
    texto_descifrado=""
    for c in texto:
        letra=ord(c)
        letra_ok=letra-posicion
        print(letra)
        print(chr(letra_ok))

#resultado
encriptar("hola", 3)
desencriptar("krod",3)
