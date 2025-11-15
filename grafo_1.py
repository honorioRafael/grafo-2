class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.adjacencias:
            self.adjacencias[vertice1] = []
        if vertice2 not in self.adjacencias:
            self.adjacencias[vertice2] = []
            
        if vertice2 not in self.adjacencias[vertice1]:
            self.adjacencias[vertice1].append(vertice2)
        if vertice1 not in self.adjacencias[vertice2]:
            self.adjacencias[vertice2].append(vertice1)

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def obter_vizinhos(self, vertice):
        return self.adjacencias.get(vertice, [])

    def __str__(self):
        return str(self.adjacencias)

def bfs(grafo, inicio):
    fila = [inicio]
    visitados = [inicio]
    
    print(f"Iniciando BFS a partir de: {inicio}")

    while fila:
        vertice_atual = fila.pop(0)
        print(f"  Visitando: {vertice_atual}")

        vizinhos = grafo.obter_vizinhos(vertice_atual)
        
        for vizinho in vizinhos:
            if vizinho not in visitados:
                print(f"    Encontrando vizinho não visitado: {vizinho}")
                visitados.append(vizinho)
                fila.append(vizinho)
    
    print(f"BFS Concluído. Vértices alcançáveis: {visitados}")
    return visitados

if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta('A', 'B')
    g.adicionar_aresta('A', 'C')
    g.adicionar_aresta('B', 'D')
    g.adicionar_aresta('B', 'E')
    g.adicionar_aresta('C', 'F')
    g.adicionar_aresta('E', 'F')
    
    g.adicionar_vertice('G')

    print("Estrutura do Grafo:")
    print(g)
    print("\n--- Executando BFS para Travessia ---")
    
    bfs(g, 'A')
    
    print("\n--- Executando BFS de outro ponto ---")
    bfs(g, 'G')