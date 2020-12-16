dicionario = dict()

dicionario['produto A'] = 12.3
dicionario['produto B'] = 38
dicionario['produto C'] = 0

print(dicionario)

print(dicionario['produto B'])

for i in dicionario.keys():
    print(dicionario[i])

for i, v in dicionario.items():
    print(f'Chave {i} : Valor {v}')
