def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print ("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")
jugar()

# def recursividad(intento=1):
#     if intento < 3:
#         print ("Me estoy llamando a mi misma")
#         intento = intento + 1
#         recursividad(intento)
#     else:
#         returns
#
#
# recursividad()

# def calc_factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return(x * calc_factorial(x-1))
# num = 700
# print("The factorial of", num, "is", calc_factorial(num))
