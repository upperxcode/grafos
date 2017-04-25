from operator import itemgetter

class Graph:

    #Construtor para grafo. Leitura direta do arquivo
    def __init__(self, arq):
        self.V = 0            # número de vértices
        self.E = 0            # número de arestas
        self.adj = []         # lista de adjacências vazia
        self.degList = []     # lista de graus
        self.tam = 0          # tamanho do grafo
        self.adj_Lista(arq)   # preenche a lista

    def sortByDegree(self):
        K = []
        degree_vertex = []

        for i in range(1, self.V):
            degree_vertex.append((self.degList[i], i))

        # degree_vertices.sort(key=lambda x: x[0], reverse=True)
        for i in range(len(degree_vertex)):
            _min = i
            for j in range(i,len(degree_vertex)):
                if (degree_vertex[j][0] > degree_vertex[_min][0]):
                    _min = j
            degree_vertex[i], degree_vertex[_min] = degree_vertex[_min], degree_vertex[i]

        for a,b in degree_vertex:
            K.append(b)

        return K

    def isNeighbor(self, u, v):
        return self.adj[u][v]

    # inicia a lista de adjacências
    def init_adj(self, V):
        self.adj = []
        self.V = V+1
        self.degList = [0] * (V+1)
        for _ in range(V+1):
            self.adj.append([False] * (V+1))

    #cria a lista de adjacência
    def adj_Lista(self, fileName):
        _file = open(fileName, 'r')
        texto = _file.readlines();
        ini = 0;

        for linha in texto:
            entrada = linha.split()
            if (entrada[0] == 'p'):
                self.init_adj(int(entrada[2]))
                self.tam = int(entrada[3])
            elif (entrada[0]=='e'):
                self.addEdge(int(entrada[1]), int(entrada[2]))
            ini+=1
        _file.close()

    #metodo para adicionar arestas
    def addEdge(self,v,w):
        self.adj[v][w] = self.adj[w][v] = True
        self.degList[v] += 1  # soma a ocorrência de cada v
        self.degList[w] += 1  # soma a ocorrência de cada w
        self.E += 1
