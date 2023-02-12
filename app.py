from entities.Graph import Graph


def createGraphCompleted(size=1):
    """ Gera um grafo completo com um determinado tamanho """
    g = Graph(size)

    for i in range(size):
        for j in range(i+1, size):
            g.add_edge(i, j, 1)

    return g


def generateGraphs():
    """ Gera 3 grafos completos """
    graphs = []

    # Grafo 1:
    graphs.append(createGraphCompleted(2))

    # Grafo 2:
    graphs.append(createGraphCompleted(4))

    # Grafo 3:
    graphs.append(createGraphCompleted(8))

    return graphs


def main():
    graphs = generateGraphs()
    initialVertex = 1

    print("\nProblema do Carteiro Chinês | Problema da Inspeção de Rotas:\n")
    for i, graph in enumerate(graphs):
        print(f"Grafo {i+1}:\n")
        postman = graph.chinese_postman(initialVertex)
        print(f"   Caminho Partindo de {initialVertex}: {postman['path']}")
        print(f"\n   Distância: {postman['distance']}")
        print(f"\n   Complexidade: {postman['complexity']}")
        print("\n------------------------------\n")


if __name__ == "__main__":
    main()
