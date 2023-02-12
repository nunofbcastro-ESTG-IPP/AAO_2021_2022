from functools import total_ordering
from queue import PriorityQueue
from entities.Edge import Edge
import copy


class Graph:
    def __init__(self, v_num):
        """Instancia um novo grafo, onde 'v_num' é o número de vértices."""
        self.counter = 0
        self.v_num = v_num
        self.edges = []
        self.possible_combinations = []

    def _increaseComplexity(self, c=1):
        """Incrementar a variavel c ao counter da complexidade"""
        self.counter += c

    def _getComplexity(self):
        """Retorna a variável counter que contem a complexidade"""
        return self.counter

    def add_edge(self, x, y, weight):
        """Adiciona uma aresta ao grafo, onde 'x' e 'y' são os vértices aos quais ela é ligada e 'weight' é o peso."""
        if x < self.v_num and y < self.v_num:
            self._increaseComplexity(2)
            self.edges.append(Edge(x, y, weight))
        else:
            self._increaseComplexity(3)
            raise IndexError(self.edges)

    def remove_edge(self, x, y):
        """Remove uma aresta do grafo, onde 'x' e 'y' são os vértices aos quais ela é ligada."""
        for edge in self.edges:
            self._increaseComplexity()
            if x in edge.vertices and y in edge.vertices:
                self._increaseComplexity(2)
                self.edges.remove(edge)
                return
            self._increaseComplexity(2)
        self._increaseComplexity()

    def dijkstra(self, v):
        """Executa o algoritmo de dijkstra a partir do vértice 'v'. Utiliza uma Priority Queue para facilitar processamento.
        Retorna uma lista com as menores distâncias entre 'v' e os outros vértices do grafo."""

        dijkstra_dist = {vertex: float("inf") for vertex in range(self.v_num)}
        self._increaseComplexity(self.v_num)
        dijkstra_dist[v] = 0
        visited = []

        pq = PriorityQueue()
        pq.put((0, v))
        self._increaseComplexity()

        while not pq.empty():
            self._increaseComplexity()
            (dist, current_vertex) = pq.get()
            visited.append(current_vertex)

            for neighbor in range(self.v_num):
                self._increaseComplexity()
                distance = self.get_edge_weight(current_vertex, neighbor)
                if distance != 0:
                    if neighbor not in visited:
                        old_cost = dijkstra_dist[neighbor]
                        new_cost = dijkstra_dist[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            self._increaseComplexity()
                            dijkstra_dist[neighbor] = new_cost
                        self._increaseComplexity()
                    self._increaseComplexity()
                self._increaseComplexity()
            self._increaseComplexity()
        self._increaseComplexity()
        return dijkstra_dist

    def get_edge_weight(self, x, y):
        """Retorna o peso da aresta entre os vértices 'x' e 'y'. Ou 0 se não existirem arestas entre eles."""
        for i in range(len(self.edges)):
            self._increaseComplexity()
            if x in self.edges[i].vertices and y in self.edges[i].vertices:
                return self.edges[i].weight
            self._increaseComplexity(2)
        self._increaseComplexity()
        return 0

    def get_odd_vertices(self):
        """Retorna uma lista com todos os índices dos vértices de grau ímpar presentes no grafo."""
        odd_vertices = []
        for i in range(self.v_num):
            self._increaseComplexity()
            degree = self.get_vertex_degree(i)
            if degree % 2 != 0:
                odd_vertices.append(i)
            self._increaseComplexity()
        self._increaseComplexity()
        return odd_vertices

    def get_vertex_degree(self, v_index):
        """Retorna o grau do vértice de índice 'v_index'."""
        degree = 0
        for i in range(len(self.edges)):
            self._increaseComplexity()
            if v_index in self.edges[i].vertices:
                degree += 1
            self._increaseComplexity()
        self._increaseComplexity()
        return degree

    def get_odd_pairs(self):
        """Retorna uma lista com todos os pares de vértices de grau ímpar presentes no grafo."""
        pairs = []
        odd_vertices = self.get_odd_vertices()
        for v_index in range(len(odd_vertices) - 1):
            self._increaseComplexity()
            pairs.append([])
            for i in range(v_index + 1, len(odd_vertices)):
                self._increaseComplexity()
                pairs[v_index].append([odd_vertices[v_index], odd_vertices[i]])
            self._increaseComplexity()
        self._increaseComplexity()
        return pairs

    def get_possible_combinations(self, pairs, done, final):
        """Retorna uma lista com todas as combinações de pares possíveis."""
        if pairs == self.get_odd_pairs():
            self.l = (len(pairs) + 1) // 2
        self._increaseComplexity()

        if pairs[0][0][0] not in done:
            done.append(pairs[0][0][0])

            for i in pairs[0]:
                self._increaseComplexity()
                f = final[:]
                val = done[:]
                if i[1] not in val:
                    f.append(i)
                else:
                    self._increaseComplexity(2)
                    continue
                self._increaseComplexity()

                if len(f) == self.l:
                    self.possible_combinations.append(f)
                    return
                else:
                    self._increaseComplexity()
                    val.append(i[1])
                    self.get_possible_combinations(pairs[1:], val, f)
                self._increaseComplexity()
            self._increaseComplexity()
        else:
            self._increaseComplexity()
            self.get_possible_combinations(pairs[1:], done, final)
        self._increaseComplexity()

    def chinese_postman(self, start_index):
        """Retorna a menor distância a ser percorrida para atravessar todas as arestas considerando um circuito."""

        odd_vertices = self.get_odd_vertices()

        if len(odd_vertices) != 0:
            self.eulerify(self.get_shortest_path_distance()["combination"])
        self._increaseComplexity()
        path = self.get_eulerian_path(start_index)
        distance = self.get_sum_of_edge_weights()
        return {"path": path, "distance": distance, "complexity": self._getComplexity()}

    def get_eulerian_path(self, start_index):
        """Retorna os vértices de um circuito percorrido no grafo (que precisa estar eulerizado), partindo do vértice de índice "start_index"."""
        graph = copy.deepcopy(self)
        length = len(self.edges) + len(self.possible_combinations)
        self._increaseComplexity(length)
        stack = []
        eulerian_path = []
        current_vertex = start_index
        while len(graph.get_neighbours(current_vertex)) > 0 or len(stack) > 0:
            self._increaseComplexity()
            current_neighbours = graph.get_neighbours(current_vertex)
            if len(current_neighbours) > 0:
                stack.append(current_vertex)
                neighbour = current_neighbours[0]
                graph.remove_edge(current_vertex, neighbour)
                current_vertex = neighbour
            else:
                self._increaseComplexity()
                eulerian_path.append(current_vertex)
                current_vertex = stack.pop()
            self._increaseComplexity()
        self._increaseComplexity()
        eulerian_path.append(start_index)
        return eulerian_path

    def get_neighbours(self, v):
        """Retorna o índice dos vizinhos do vértice "v"."""
        neighbours = []
        for edge in self.edges:
            self._increaseComplexity()
            if edge.vertices[0] == v or edge.vertices[1] == v:
                if edge.vertices[0] != v and edge.vertices[0] not in neighbours:
                    neighbours.append(edge.vertices[0])
                elif edge.vertices[1] not in neighbours:
                    self._increaseComplexity()
                    neighbours.append(edge.vertices[1])
                self._increaseComplexity(2)
            self._increaseComplexity()
        self._increaseComplexity()
        return neighbours

    def get_shortest_path_distance(self):
        """Retorna um dictionary contendo a menor distância e a combinação de vértices ímpares que nela resultou."""
        self.possible_combinations = []
        self.get_possible_combinations(self.get_odd_pairs(), [], [])
        combinations = self.possible_combinations
        chosen_combo = None
        shortest_distance = None

        for combo in combinations:
            self._increaseComplexity()
            total_distance = 0
            for pair in combo:
                self._increaseComplexity()
                dijkstra_distances = self.dijkstra(pair[0])
                total_distance += dijkstra_distances[pair[1]]
            self._increaseComplexity()
            if shortest_distance is None or shortest_distance > total_distance:
                shortest_distance = total_distance
                chosen_combo = combo
            self._increaseComplexity()
        self._increaseComplexity()

        return {"combination": chosen_combo, "distance": shortest_distance}

    def eulerify(self, combination):
        """Euleriza o grafo, duplicando as arestas entre os vértices especificados na lista de pares de vértices ímpares 'combination'."""
        for pair in combination:
            self._increaseComplexity()
            for edge in self.edges:
                self._increaseComplexity()
                if edge.vertices[0] == pair[0] and edge.vertices[1] == pair[1]:
                    self._increaseComplexity(2)
                    weight = edge.weight
                    self.add_edge(pair[0], pair[1], weight)
                    break
                self._increaseComplexity(2)
            self._increaseComplexity()
        self._increaseComplexity()

    def get_sum_of_edge_weights(self):
        """Retorna a soma de todos os pesos das arestas presentes no grafo."""
        total_weight = 0
        for edge in self.edges:
            self._increaseComplexity()
            total_weight += edge.weight
        self._increaseComplexity()
        return total_weight
