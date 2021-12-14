class BubbleSort:
    def __init__(self, lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lista[j] > lista[j + 1]:
                    aux = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = aux

        self.sorted_list = lista