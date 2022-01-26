def sumaacumulada(lista):
    sumatemp = 0
    nuevalista = []
    for i in lista:
        sumatemp = sumatemp + i
        nuevalista.append(sumatemp)
    return nuevalista

def sumacum(lista):
    sumatemp=0
    for x in range(len(lista)):
        sumatemp = sumatemp + lista[x]
        lista[x] = sumatemp
    return lista

def elimina(lista):
    lista.pop()
    lista.pop(0)
    #del(lista[0])
    #del(lista[-1])
    return lista

def ordenada(lista):
    lista2 = lista.copy()
    if lista2 == lista.sort():
        return True
    else:
        return False

def elimina_duplicados(lista):
        return set(lista)

def duplicado(lista):
    if len(lista) != len(set(lista)):
        return True
    else:
        return False

# == igual
# != diferente
# >= mayor que o igual
# <= menor que o igual
# <
# >

listaejemplo = [1,2,3,3,4,4]
print(sumaacumulada(listaejemplo))
print(sumacum(listaejemplo))
print(elimina(listaejemplo))
print(ordenada(listaejemplo))
print(elimina_duplicados(listaejemplo))
print(duplicado(listaejemplo))
