# Bubble Sort - Compare side elements (worst case)

def bubbleSort(list):

    def changePosition(a, b):
        list[a], list[b] = list[b], list[a]

    n = len(list)
    changed = True
    x = -1
    e = 0

    while changed:
        changed = False
        x = x + 1

        for i in range(1, n-x):
            if list[i - 1] > list[i]:
                changePosition(i-1, i)
                changed = True

        e = e + 1

    return print(f'Lista: {list} ordenada com {e} iteracoes.')


ListMessy = [9, 3, 5, 4, 6, 2, 7, 1, 8]

bubbleSort(ListMessy)
