# def selectionSort(array):
#   for locone in range(len(array)-1,0):
#     print(array)
#     max = 0
#     for loctwo in range(1,locone+1):
#       print(array)
#       if array[loctwo] > array[max]:
#         max = loctwo
#
#     temp = array[locone]
#     array[locone] = array[max]
#     array[max] = temp
#     print(array)

#

# def insertionSort(array):
#   for index in range(1,len(array)):
#     curval = array[index]
#     pos = index
#     while pos > 0 and array[pos-1] > curval:
#       array[pos] = array[pos-1]
#       pos = pos-1
#     array[pos]=curval
#     print(array)



# def quickSort(array):
#    quickSortHelper(array,0,len(array)-1)
#
# def quickSortHelper(array,inicio,fin):
#    if inicio<fin:
#        puntoDiv = particion(array,inicio,fin)
#        print(str(puntoDiv))
#        print(array)
#        quickSortHelper(array, inicio, puntoDiv-1)
#        quickSortHelper(array, puntoDiv+1, fin)

#
# def particion(array,inicio,fin):
#    pivot = array[inicio]
#    izq = inicio+1
#    der = fin
#    done = False
#    while not done:
#        while izq <= der and array[izq] <= pivot:
#            izq = izq + 1
#        while array[der] >= pivot and der >= izq:
#            der = der - 1
#        if der < izq:
#            done = True
#        else:
#            temp = array[izq]
#            array[izq] = array[der]
#            array[der] = temp
#    temp = array[inicio]
#    array[inicio] = array[der]
#    array[der] = temp
#    return der

#
#
def mergeSort(array):
    print("Dividiendo ",array)
    if len(array)>1:
        mitad = len(array)//2
        izq = array[:mitad]
        der = array[mitad:]
        mergeSort(izq)
        mergeSort(der)
        i=0
        j=0
        k=0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                array[k]=izq[i]
                i=i+1
            else:
                array[k]=der[j]
                j=j+1
            k=k+1
        while i < len(izq):
            array[k]=izq[i]
            i=i+1
            k=k+1
        while j < len(der):
            array[k]=der[j]
            j=j+1
            k=k+1
    print("Merging ",array)


# array = [54,26,93,17,77,31,44,55,20]
# selectionSort(array)
# print("*** Selection Sort*** \n"+str(array)+"\n")
#
# array = [54,26,93,17,77,31,44,55,20]
# insertionSort(array)
# print("*** Insertion Sort*** \n"+str(array)+"\n")
#
# array = [54,26,93,17,77,31,44,55,20]
# quickSort(array)
# print("*** Quick Sort*** \n"+str(array)+"\n")

array = [54,26,93,17,77,31,44,55,20]
mergeSort(array)
print("*** Merge Sort*** \n"+str(array)+"\n")




["a",["b", ["d",[],[]], ["e",[],[]]], ["c", ["f",[],[]], []]]
