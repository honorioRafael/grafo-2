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

def bfs_menor_caminho(grafo, inicio, destino):
    fila = [(inicio, [inicio])]
    visitados = [inicio]
    
    while fila:
        (vertice_atual, caminho) = fila.pop(0)
        
        if vertice_atual == destino:
            return caminho
            
        vizinhos = grafo.obter_vizinhos(vertice_atual)
        
        for vizinho in vizinhos:
            if vizinho not in visitados:
                visitados.append(vizinho)
                
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                
                fila.append((vizinho, novo_caminho))

    return []

if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta('A', 'B')
    g.adicionar_aresta('A', 'C')
    g.adicionar_aresta('B', 'D')
    g.adicionar_aresta('B', 'E')
    g.adicionar_aresta('C', 'F')
    g.adicionar_aresta('E', 'F')
    g.adicionar_aresta('F', 'G')
    g.adicionar_aresta('E', 'H')
    
    print("Estrutura do Grafo:")
    print(g)
    
    print("\n--- Buscando Menor Caminho ---")
    
    inicio = 'A'
    destino = 'G'
    caminho = bfs_menor_caminho(g, inicio, destino)
    print(f"Menor caminho de '{inicio}' para '{destino}': {caminho}")

    inicio = 'D'
    destino = 'G'
    caminho = bfs_menor_caminho(g, inicio, destino)
    print(f"Menor caminho de '{inicio}' para '{destino}': {caminho}")
    
    inicio = 'A'
    destino = 'H'
    caminho = bfs_menor_caminho(g, inicio, destino)
    print(f"Menor caminho de '{inicio}' para '{destino}': {caminho}")

    inicio = 'A'
    destino = 'Z'
    caminho = bfs_menor_caminho(g, inicio, destino)
    print(f"Menor caminho de '{inicio}' para '{destino}': {caminho}")