from abc import ABC, abstractmethod

from abc import ABC,abstractmethod


class Animal(ABC): #Animal es una clase abstracta

    tono="bajo"
    @abstractmethod
    def saludar(self):
        print("estoy saludando con agua")

    def hablar(self,tono):
        print("estoy hablando en tono ",tono)

class Perro(Animal):
    def ladrar(self):
        print("el perro ladra")

    def saludar(self):
        print("levanta la patita con comida de perros")

class Gato(Animal):
    def maullar(self):
        print("el gato maúlla")

    def saludar(self):
        super().saludar()
        print("mueve la colita con comida de gatos")