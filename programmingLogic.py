def sumRec(n):
    if n > 0:
        soma = sumRec(n-1)+n
    else:
        soma = 0

    return soma


print(sumRec(1))
