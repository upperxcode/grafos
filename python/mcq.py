from state import *
from graph import *
import sys
import timeit
import time

def pre_process_instance(G):
    Q = []
    K = G.sortByDegree()
    _map = [0] * len(K)

    deltaG = max(G.degList)
    for i in range(deltaG):
        _map[i] = i+1 # i+1 para KN receber a partir de 1

    for i in range(deltaG, len(K)):
        _map[i] = deltaG+1

    return [], [State(Q, K, _map)]

def hasNeighborInColor(G, u, Cor):
    for v in Cor:
        if G.isNeighbor(v, u):
            return True
    return False

def greedy(G, q, k):
    p = []
    maiorCor = 0
    p.append([])
    for v in k:
        cor = 0
        while cor <= maiorCor and hasNeighborInColor(G, v, p[cor]):
            cor += 1
        if cor > maiorCor:
            maiorCor = cor
            p.append([])
        p[cor].append(v)
    return p

def pre_process_state(G, state, c):
    if state.map:
    	return

    p = greedy(G, state.Q, state.K)
    posicao = 0
    state.map = [0] * len(state.K)
    size = len(p)

    for cor in range(size):
        for v in p[cor]:
            state.K[posicao] = v
            state.map[posicao] = cor+1
            posicao += 1

def upper_bound(G, state, C):
    return state.map[-1]

def remove_vertex(g, state):
    state.map.pop()
    return state.K.pop()

def intersect(G, K, v):
    return [w for w in K if G.isNeighbor(v, w)]

def post_process_instance(G, C):
    return C

def mcbb(G, limit, p):
    finish = time.time() + limit
    C,S = pre_process_instance(G)
    count_states = 0
    while S:
        state = S.pop()
        pre_process_state(G, state, C)
        count_states += 1
        while state.K and len(C)<(len(state.Q)+upper_bound(G,state,C)):
            v = remove_vertex(G, state)
            S.append(state.copy())
            state.Q.append(v)
            state.K = intersect(G, state.K, v)
            state.map = []
            pre_process_state(G, state, C)
            count_states += 1
        if len(C) < len(state.Q):
            C = state.Q[:]
        if time.time() >= finish:
            print(p, 'timeout', count_states, end="")
            return 0
    print(p,count_states, end="")
    return post_process_instance(G, C)


def initial(limit):

    max_clique = mcbb(G, limit, program)
    if max_clique == 0:
        return
    print(" " + str(len(max_clique)),end="")

G = Graph(sys.argv[1])
program = sys.argv[3]

if __name__ == '__main__':
    time = timeit.timeit("initial("+sys.argv[2]+")",  "from __main__ import initial", number=1)
    print(" %.5f" %time)

