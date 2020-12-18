def permuta(comb, list):
    if comb == 1:
        return list
    else:
        return [y + x for y in permuta(1, list) for x in permuta(comb-1, list)]


print(len(permuta(2, ["a", "b", "c"])), permuta(2, ["a", "b", "c"]))
