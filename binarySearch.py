def biSearch(vector, firstPos, lastPos, x):

    if lastPos >= firstPos:
        half = firstPos+(lastPos-firstPos)//2
        if vector[half] == x:
            return half

        elif vector[half] > x:
            return biSearch(vector, firstPos, half-1, x)

        else:
            return biSearch(vector, half+1, lastPos, x)

    else:
        return -1


listNum = [12, 13, 40, 56]
Num = 40

result = biSearch(listNum, 0, len(listNum)-1, Num)

if result != -1:
    print("O elemento esta presente no indice %d !" % result)

else:
    print("O elemento nao esta presente no vetor!")
