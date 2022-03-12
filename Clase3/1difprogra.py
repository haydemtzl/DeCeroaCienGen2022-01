import os

#structured programming
#
# animal = input('Write the name of the animal: ')
#
# if animal == 'gato':
#     print('This animal has '+str(4)+' legs.')
# elif animal == 'perro':
#     print('This animal has '+str(4)+' legs.')
# elif animal == 'spider':
#     print('This animal has '+str(8)+' legs.')
# else:
#    print("I don't know that animal")

 # modular programing

# animals = {'gato':4,'perro':4,'spider':8}
#
# def getName():
#      animal = input('Write the name of the animal: ')
#      return animal
#
# def setAnimal(animal):
#     if animal not in animals:
#         print("I don't know that animal")
#         animallegs = 0
#     else:
#         animallegs = animals[animal]
#     return animallegs
#
# def describeAnimal(animallegs):
#     print('This animal has '+str(animallegs)+' legs. ' )
#
# variableanimal = getName()
# variableanimallegs  = setAnimal(variableanimal)
# if variableanimallegs > 0:
#     describeAnimal(variableanimallegs)

 #Object Oriented Programming
#
# class Animal(object):
#
#     def __init__(self):
#         print('Instanciating animal class')
#         self.name = input('Write the name of the animal: ')
#         self.animallegs = 0
#
#     def setAnimal(self):
#         animals = {'gato':4,'perro':4,'spider':8}
#         animal = self.name
#         if animal not in animals:
#     	       print("I don't know that animal")
#         else:
#             self.animallegs = animals[animal]
#
#     def describeAnimal(self):
#         print('This animal has '+str(self.animallegs)+' legs. ')
#
# animal = Animal() # Instanciando un objeto de la clase animal
# print(animal.name)
# animal.setAnimal()
# if animal.animallegs > 0:
#      animal.describeAnimal()


# def sumaacumulada(lista):
#     listanueva=[]
#     suma=0
#     for i in range(len(lista)):
#         suma = suma + lista[i]
#         listanueva.append(suma)
#
# def sumaacumulada2(lista):
#     listanueva=[]
#     suma=0
#     for i in range(len(lista)):
#         suma += lista[i]
#         listanueva.append(suma)


def sumaacumulada3(lista):
    suma=0
    for i in range(len(lista)):
        suma += lista[i]
        lista[i] = suma
    print(lista)

sumaacumulada3([1,2,3])
