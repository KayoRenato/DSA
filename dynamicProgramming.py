

dic = {
    "acha": True,
    "que": True,
    "o": True,
    "clima": True,
    "pode": True,
    "mudar": True
}


def calcCost(word):
    if word in dic:
        return 0
    else:
        return len(word)


cache = {}


def splitString(inputString, beginIndex):
    if beginIndex in cache:
        return cache[beginIndex]

    subString = inputString[beginIndex:]

    if not len(subString):
        return '', 0

    minCost = None
    minString = None

    for i in range(1, len(subString)+1):
        restString, restCost = splitString(inputString, beginIndex+i)
        currentString = subString[:i]
        currentCost = calcCost(currentString)+restCost

        if minCost is None or currentCost < minCost:
            if currentString and restString:
                minString = currentString+' '+restString
                currentCost += 1
            else:
                minString = currentString + restString

            minCost = currentCost

    cache[beginIndex] = minString, minCost

    return minString, minCost


print(splitString('marceloachaqueoclimapodemudar', 0))
