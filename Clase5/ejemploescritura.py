file = open("archivo_detexto.txt", "r")
contenido = file.read(15)
print(contenido)
print(file.tell()) # posicion 15
contenido = file.read(30)
print(contenido)
file.close()

writing = open("archivo_deescritura.txt", "w")
writing.write("Hola estoy escribiendo en este archivo y como me abrí en w, voy a sobreescribir todo")
writing.tell() #55
writing.write("otra linea")
writing.close()

appending = open("archivo_deescritura.txt", "a")
appending.write("aquinomascontinuando")
appending.tell()
appending.close()

archivo = open("ejemplo.csv","r")
print(archivo.readline())
lista = []
for line in archivo.readlines():
    lista.append(line)
archivo.close()
archivo = open("ejemplo2.csv", "w")
archivo.writelines(lista)
archivo.close()

def suma(num1, num2):
    #print(str(num1+num2))
    return(num1+num2)

resultado = lambda 1, 2: 1 + 2

resultadosuma = suma(1,2)
