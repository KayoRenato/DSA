# criacao de grafo e implementacao de algoritmo BFS

# funcao para criar grafo padrao
from collections import defaultdict


class Grafo:
    def __init__(self):

        # dicionario padrao para armazenamer grafo
        self.graph = defaultdict(list)

      # funcao para adicionar arresta ao grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        # marcar todos os vertices como nao visitados
        visited = [False]*(len(self.graph))

        # cria fila para o BFS
        queue = []

        # marca o no de origem s como visitado e inclui na fila
        queue.append(s)
        visited[s] = True

        while queue:

            # remove um vertice da fila e imprime
            s = queue.pop(0)
            print(s, end=" ")

            # obtendo todos os vertices adjacente dos vertices desenfilerados
            # se um adjacente nao foi visitado, marca-o como visitado e inclui
            # na fila
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        print()


# criando uam instancia da classe, construindo um grafo com diversas arestas
g = Grafo()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print('Aqui esta o caminho a seguir para atravessar o grado(comecando do vertice 2):')
g.bfs(2)


print("-"*40)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


print(list(bfs_paths(graph, 'A', 'F')))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


print(shortest_path(graph, 'A', 'F'))
