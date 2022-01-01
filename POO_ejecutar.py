from POO_Abstractas import Animal, Perro, Gato

#genera errores porque es una clase abstracta

perro=Animal() #instanciar una clase
perro.saludar()
perro.hablar("alto")

perro=Perro()
gato=Gato()
perro.hablar("bajo")
gato.hablar("alto")
gato.saludar()

Animal = [Perro(),Gato(),Perro(),Perro(),Gato()] #polimorfismo
Animal[2].saludar()
Animal[1].saludar()