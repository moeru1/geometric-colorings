from sage.all import *
import itertools as it
from collections import deque
   
def adyacency_pairs(G):
    def print_pairs_dfs(v):
        stack = deque()
        stack.append(v)
        while stack:
            v = stack.pop()
            visited[v] = True
            for w in G.neighbor_iterator(v):
                if not visited[w]:
                    pairs.append((v,w))
                    stack.append(w)

    pairs = deque()
    #vertices 0 ... (n-1)
    n = len(G.vertices())
    #stack = deque()
    visited = [False] * n
    for v in G.vertices():
        if (not visited[v]):
            print_pairs_dfs(v)
            
    return pairs    


def is_harmonious(G, coloring):
    S = set()
    pairs = adyacency_pairs(G)
    for (v,w) in pairs:
        c_v = coloring[v]
        c_w = coloring[w]
        if c_w != c_v and (not (frozenset((c_v, c_w)) in S)):
            S.add(frozenset((c_v, c_w)))
        else:
            return False
    return True


def find_coloring(G, n_colors, labels=dict()):
    #labels_inv = {v: k for k, v in labels.items()}
    V = G.vertices()
    if (not labels):
        print("is dict()")
        labels = {V[i]:i for i in range(len(V))}
        
    G_ = G.relabel(labels, inplace=False)
    n_colors = tuple([i for i in range(1, n_colors+1)])
    c = find_coloring_h(G_, n_colors)
    return c

def find_coloring_h(G, color_list):
    for coloring in it.product(color_list,repeat=len(G.vertices())):
        if (is_harmonious(G, coloring)):
            return coloring
    return ()


