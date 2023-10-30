class Animales:
    def __int__(self, name):
        self.name = name

    def tipo_animal(self):
        pass
class Leon(Animales):
    def tipo_animal(self):
        print('Animal Salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('Animal Domestico')
nuevo_animal2 = Leon()
nuevo_animal2.tipo_animal()

nuevo_animal = Perro()
nuevo_animal.tipo_animal()
