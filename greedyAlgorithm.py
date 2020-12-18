class Foods(object):

    # construtor da classe
    def __init__(self, n, v, c):

        # nome alimento
        self.name = n

        # valor do alimento em reais
        self.value = v

        # numero de calorias do alimento
        self.cal = c

    # metodo para obter o valor de cada alimento
    def getValue(self):
        return self.value

    # metodo para obert o custo
    def getCal(self):
        return self.cal

    # metodo para imprimir nome/valor/calorias
    def __str__(self):
        return self.name + ':<' + str(self.value) + ', ' + str(self.cal) + '>'


def createdMenu(names, values, calories):

    # criar lista vazia
    menu = []

    # inserir dados na lista
    for i in range(len(values)):
        menu.append(Foods(names[i], values[i], calories[i]))

    return menu

# greedyAlgorithm


def greedy(items, maxCost, keyFuction):

    # copia todos os itens
    itemsCopy = sorted(items, key=keyFuction, reverse=True)

    # lista de resultados
    result = []

    # valor total
    totalValue = 0

    # custo total
    totalCost = 0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCal() <= maxCost):
            result.append(itemsCopy[i])

            totalCost += itemsCopy[i].getCal()

            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)


def runGreedy(items, constraint, keyFuction):
    result, val = greedy(items, constraint, keyFuction)

    print(f'Valor total dos itens para 1000 calorias = {val}')

    for item in result:
        print(item)

# Funcao que gera melhor cardapio pelo valor individual dos alimentos e pelo
# custo dos alimentos


def buildMenu(foods, totCalories):
    print(
        f'Usando o algoritmo guloso para buscar o melhor menu pelo valor dos alimentos para {totCalories} calorias')
    runGreedy(foods, totCalories, Foods.getValue)

    print(
        f'\nUsando o algoritmo guloso para buscar o melhor menu pelo custo dos alimentos para {totCalories} calorias')
    runGreedy(foods, totCalories, lambda x: 1/Foods.getCal(x))


foodsList = ['Frango', 'Milk Shake', 'Pizza', 'Hamburgue', 'Batata Frita',
             'Refrigerante', 'Maca', 'Laranja', 'Cenoura', 'Alface']

priceList = [79, 18, 45, 38, 25, 9, 15, 10, 22, 12]

calList = [114, 156, 359, 354, 365, 153, 97, 82, 79, 40]


# criar o menu
menu_foods = createdMenu(foodsList, priceList, calList)

# busca o melhor menu para o consumo de 1000 calorias
buildMenu(menu_foods, 1000)
