#
# #Ejercicio1  #[1,2,3]  result:6  i:2  len(array):3
# def sumaDeLista(array):
#    result = 0
#    for i in range(len(array)): #0,3
#       result += array[i]
#       array[i] = result
#    return array
#
# a=(SumaDeLista([1,2,3]))

#Ejercicio2
def elimina(lista):
   lista.pop()
   lista.pop(0)
   print(lista)

elimina([1,2,3])



#Ejercicio4
def Elimina_duplicados (lista1):
   lista1=[3,3,4,1,1,1]
   listsindup=list(set(lista1))
   return listsindup
print(listsindup)

#Ejercicio5
def EliminaDuplicados (lista1):
lista1=[3,4,1,1,1]
listsindup=list(set(lista1))
valor= True
if len(lista1) != len(listsindup):
   valor = True
else:
   valor = False
print(valor)






#Ejercicio3
def ListaOrdenada(array):
lista=[1,2,3,5,4]
a = lista
a.sort()
valor=True
if lista != a:
   valor = False
else:
   valor = True
print(valor)
