import networkx as nx

def criar_grafo_lista_adjacencia(n):
    grafo = {}
    for vertice in range(n):
        grafo[vertice] = []
    return grafo

def visualizar_grafo(grafo):
    for vertice, adjacencias in grafo.items():
        for adjacente in adjacencias:
            print(f'Aresta: ({vertice}, {adjacente})')

def vertices_adjacentes(grafo, vertice):
    return grafo[vertice]

def existe_aresta(grafo, v1, v2):
    return v2 in grafo[v1] or v1 in grafo[v2]

def grau_vertice(grafo, vertice):
    return len(grafo[vertice])

def verificar_regularidade(grafo):
    grau = grau_vertice(grafo, 0)
    for vertice in grafo:
        if grau_vertice(grafo, vertice) != grau:
            return False
    return True

grafo = criar_grafo_lista_adjacencia(5)

grafo[0] = [1, 2]
grafo[1] = [0, 3]
grafo[2] = [0, 4]
grafo[3] = [1]
grafo[4] = [2]

visualizar_grafo(grafo)

