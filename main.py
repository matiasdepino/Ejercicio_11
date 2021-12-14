#Ejercicio 11
# 1. Desarrollar un modulo python llamado bubble_sort con una clase llamada BubbleSort que acepta una lista en el constructor, la ordena por el método de la burbuja y la almacena en un atributo llamado sorted_list
# 2. Desarrollar un modulo python que importa bubble_sort , pide datos de tipo int por el teclado hasta que se introduzca el número -9999. Controlar que el tipo de dato introducido es correcto mediante try , except . Almacenar los datos en una lista
# 3. Crear un objeto de tipo BubbleSort pasándole al constructor la lista leída por teclado . Escribir por pantalla el atributo sorted_list del objeto creado . Borrar el objeto creado
# 4. Repetir lo indicado en 2 y 3 hasta que se introduzca como primer dato de la lista “fin”

import bubble_sort as bs

while True:

    lista = []
    fin = False

    while True:

        while True:
            n = input("Introducir elemento de lista a ordenar: ")
            if n == "fin":
                fin = True
                break

            try:
                n = int(n)
                break

            except:
                print("El dato introducido no es un número que sea válido")
        if fin:
            break
        if (n == -9999):
            break
        lista.append(n)
    if fin:
        break
    lo = bs.BubbleSort(lista)
    print("Lista ordenada: ", '\n', lo.sorted_list)