from sage.all import *
#Test de interseccion

def orientation(p, q, r):
    (px, py) = p
    (qx, qy) = q
    (rx, ry) = r
    a = qx-px
    b = rx-px
    c = qy-py
    d = ry-py
    return a*d-b*c


def ccw(a,b,c):
    (ax, ay) = a
    (bx, by) = b
    (cx, cy) = c
    return (cy-ay) * (bx-ax) > (by-ay) * (cx-ax)


# Return true if line segments AB and CD intersect
def intersect(s1, s2):
    (a, b) = s1
    (c, d) = s2
    inter  = ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)
    return inter


#Criterio D(G)

def ady_vertices(e1, e2):
    (a, b) = e1
    (c, d) = e2
    #print(e1, e2)
    return a == c or a == d or b == c or b == d

def ady_D(s1, s2, e1, e2):
    return not (intersect(s1, s2) or ady_vertices(e1, e2))


#criterio Epp(G)

def ady_Epp(s1, s2, e1, e2):
    #return (not ady_vertices(e1, e2)) and intersect(s1, s2)
    return intersect(s1, s2)

def ady_Epp2(s1, s2, e1, e2):
    return intersect(s1,s2) and (not ady_vertices(e1, e2))


#criterio W(G)

def ady_W(s1, s2, e1, e2):
    return not (ady_vertices(e1, e2)) or intersect(s1, s2) 


