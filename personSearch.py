people = ['Monteiro Lobato', 'Jose de Alencar',
          'Celilia Meireles', 'Carlos Drummond de Andrade',
          'Machado de Assis', 'Clarice Lispector',
          'Graciliano Ramos', 'Guimaraes Rosa', 'Ruth Rocha',
          'Luis Fernando Verissimo']

print(people)

# Sort people list
people.sort()
print(people)

# Search position of a person on list
name = 'Clarice Lispector'


def searchPerson(list, search):
    if search in list:
        i = 0
        while search != list[i]:
            i = i + 1

        print(f'A pessoa {search}, encontra-se na posicao {i} lista.')

    else:
        print('A pessoa %s, nao esta na lista.' % search)


searchPerson(people, name)
