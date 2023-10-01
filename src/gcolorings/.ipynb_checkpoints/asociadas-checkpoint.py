from sage.all import *
import itertools as it
import gcolorings.criterios_ady as ady
 
#gráfica K_n  con vértice del 0 a n-1
def D_Kn(n):
    def edge_lbl(i, j):
        return "v"+ str(i) +" - " + "v" + str(j)
        #return frozenset((i,j))
    
    def edges_comb(i, j, lb, ub, DG):
        edge1_lbl = edge_lbl(i,j)
        for l in range(lb, ub+1):
            for u in range(l+1, ub+1):
                DG.add_edge(edge1_lbl, edge_lbl(l,u))

    def right(i, j, n, DG):
        #lb = min((i+1) % n, (j-1) % n)
        #ub = max((i+1) % n, (j-1) % n)
        edge1_lbl = edge_lbl(i,j)
        for k in range(1, j-i):
            for m in range(k+1, j-i):
                a = min((i+k)%n, (i+m)%n)
                b = max((i+k)%n, (i+m)%n)
                DG.add_edge(edge1_lbl, edge_lbl(a, b))
        #edges_comb(i, j, lb, ub, DG)

    def left(i, j, n, DG):
        edge1_lbl = edge_lbl(i,j)
        for k in range(1, (n-2) - (j-i-1) + 1):
            for m in range(k+1, (n-2) - (j-i-1) + 1):
                a = min((j+k)%n, (j+m)%n)
                b = max((j+k)%n, (j+m)%n)
                DG.add_edge(edge1_lbl, edge_lbl(a, b))
        #lb = min((j+1) % n, (i-1) % n)
        #ub = max((j+1) % n, (i-1) % n)
        #print("i j:", i, j)
        #print("lb ub:", lb, ub)
        #edges_comb(i, j, lb, ub, DG)

    DG = Graph()
    for v in range(n):
        for w in range(v+1,n):
            DG.add_vertex(edge_lbl(v,w))
    
    #cierre convexo
    for i in range(n-1):
        left(i, i+1, n, DG)
    
    for j in range(2, n-1):
        left(0, j, n, DG)
        right(0, j, n, DG)
        
    for i in range(1, n):
        for j in range(i+2,n):
            #right
            #si no está el lado derecho vacio
            #if ((i+1)%n - (j-1)%n)%n > 1:
            right(i, j, n, DG)
            
            #left
            left(i, j, n, DG)
    return DG

def deg(i,j,n):
    left = (abs(i-j)-1)
    right = (n-2)-(abs(i-j)-1)
    return (n*(n-1)/2) - 1 - left*right - (n-2)*2

def sum_edges(n):
    suma = 0
    for i in range(n):
        for j in range(i+1,n):
            suma = suma + deg(i,j,n)

#graficas asociadas
def D(V, E):
    return T(V, E, ady.ady_D)

def Epp(V, E):
    return T(V, E, ady.ady_Epp)

def Epp2(V, E):
    return T(V, E, ady.ady_Epp2)

def W(V, E):
    return T(V, E, ady.ady_W)

#grafica asociada T(V, E, ady) de la grafica G=(V,E) usando el criterio de adyacencia ady
def T(V, E, ady):
    DG = Graph()
    m = len(E)
    E_set = set(E)
    for i in range(m):
        #aseguramos que agregamos todos los vertices
        DG.add_vertex(E[i])
        for j in range(i+1, m):
            #print(E[i])
            #print(E[j])
            s1 = (V[E[i][0]], V[E[i][1]])
            s2 = (V[E[j][0]], V[E[j][1]])
            #print(s1, s2)
            #if intersect(s1, s2) or ady(E[i], E[j]):
            if ady(s1, s2, E[i], E[j]):
                #print((E[i], E[j]))
                #print((s1, s2))
                DG.add_edge(E[i], E[j])
    return DG
 
