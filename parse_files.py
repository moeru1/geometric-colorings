from sage.all import *
#lee archivo 
import numpy as np
import random
import os
from collections import defaultdict

#otype_info: int -> int
def otype_info(n):
    dtype_read = '>u1'
    suffix = 'b08'
    dtype_m = np.int32
    if n >= 9:
        dtype = '>u2'
        suffix = 'b16'
        dtype_m = np.int64
    return (dtype_read, suffix, dtype_m)

def num_otypes_from_info(n, ot_info):
    (_,sufix,dtype_m) = otype_info
    bsize = os.path.getsize("types/otypes{:02}.{}".format(n, suffix))
    bsize_num = 1 if suffix == 'b08' else 2
    return bsize // (bsize_num * 2)

#read_otypes: int -> [[int]]
def read_otypes(n):
    dtype_read = '>u1'
    suffix = 'b08'
    dtype_m = np.int32
    if n >= 9:
        dtype = '>u2'
        suffix = 'b16'
        dtype_m = np.int64
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        points_all = np.fromfile(f, dtype = dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all)//(n*2) #numero de order types
        #print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            points = []
            for j in range(0, 2*n, 2):
                points.append((points_all[i*(n*2) + j], points_all[i*(n*2) + j + 1]))
        
            #E = [(a,b) for a in range(n) for b in range(a+1, n)]
            #print(points)
            #G = D(points,E)
            #graph_list.append(G)
            points_set.append(points)
        return points_set

#read_otypes_random: int -> [[int]]
def read_otypes_random(n, p = 0.5):
    dtype_read = '>u1'
    suffix = 'b08'
    dtype_m = np.int32
    if n >= 9:
        dtype_read = '>u2'
        suffix = 'b16'
        dtype_m = np.int64
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        points_all = np.fromfile(f, dtype= dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all)//(n*2) #numero de order types
        #print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            if (random.random() <= p):
                points = []
                for j in range(0, 2*n, 2):
                    points.append((points_all[i*(n*2) + j], points_all[i*(n*2) + j + 1]))

                #E = [(a,b) for a in range(n) for b in range(a+1, n)]
                #print(points)
                #G = D(points,E)
                #graph_list.append(G)
                points_set.append(points)
        return points_set


def read_otypes_randomnm(n, m = 1):
    indexes = []
    (dtype_read, suffix, dtype_m) = otype_info(n)
    num_otypes = num_otypes_from_info(n, (dtype_read, suffix, dtype_m))
    for i in range(m):
        r = random.randint(0, num_otypes-1)
        indexes.append(r)
    num_otypes.sort()
    l = 0
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        #if 
        points_all = np.fromfile(f, dtype = dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all)//(n*2) #numero de order types
        #print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            points = []
            for j in range(0, 2*n, 2):
                points.append((points_all[i*(n*2) + j], points_all[i*(n*2) + j + 1]))
        
            #E = [(a,b) for a in range(n) for b in range(a+1, n)]
            #print(points)
            #G = D(points,E)
            #graph_list.append(G)
            points_set.append(points)
        return points_set

    
def map_A(n, points_set, A):
    E = [(a,b) for a in range(n) for b in range(a+1, n)]
    graph_list = []
    for points in points_set:
        G = A(points, E)
        graph_list.append(G)
    return graph_list

def write_otypes_A(n, graph_list, prefix="adj_otypes", order_i=[]):
    if order_i == []:
        order_i = range(len(graph_list))
    with open("types/{}{:02d}.in".format(prefix, n), "w") as f:
        print("{0} {1}".format(n*(n-1)/2, len(graph_list)), file = f)
        #relabel graph
        for k in order_i:
            V = graph_list[k].vertices()
            labels = {V[i]: i+1 for i in range(len(V))}
            graph_list[k].relabel(labels,inplace=True)
            print("Graph {0}".format(k+1), file = f)
            for v in graph_list[k].vertex_iterator():
                neighbors = graph_list[k].neighbors(v)
                print("{} : {}".format(v, " ".join(map(str, neighbors)) ), file = f )
    #f.close()
    

#test
#n = 5
#points_set = read_otypes(n)
#graph_list_D = map_A(n, points_set, D)
#write_otypes_A(n, graph_list_D)
#print(points_set[1])

#for i in range(0, n*(n-1)/2):
    #for j in range(i+1, n):
#        l = line([(points_set[2][i],points_set[2][j])])



color_list = [(0, 0, 0),
(1, 0, 103),
(213 ,255 ,0),
(255 ,0 ,86),
(158 ,0 ,142),
(14 ,76 ,161),
(255 ,229 ,2),
(0 ,95 ,57),
(0 ,255 ,0),
(149 ,0 ,58),
(255 ,147 ,126),
(164 ,36 ,0),
(0 ,21 ,68),
(145 ,208 ,203),
(98 ,14 ,0),
(107 ,104 ,130),
(0 ,0 ,255),
(0 ,125 ,181),
(106 ,130 ,108),
(0 ,174 ,126),
(194 ,140 ,159),
(190 ,153 ,112),
(0 ,143 ,156),
(95 ,173 ,78),
(255 ,0 ,0),
(255 ,0 ,246),
(255 ,2 ,157),
(104 ,61 ,59),
(255 ,116 ,163),
(150 ,138 ,232),
(152 ,255 ,82),
(167 ,87 ,64),
(1 ,255 ,254),
(255 ,238 ,232),
(254 ,137 ,0),
(189 ,198 ,255),
(1 ,208 ,255),
(187 ,136 ,0),
(117 ,68 ,177),
(165 ,255 ,210),
(255 ,166 ,254),
(119 ,77 ,0),
(122 ,71 ,130),
(38 ,52 ,0),
(0 ,71 ,84),
(67 ,0 ,44),
(181 ,0 ,255),
(255 ,177 ,103),
(255 ,219 ,102),
(144 ,251 ,146),
(126 ,45 ,210),
(189 ,211 ,147),
(229 ,111 ,254),
(222 ,255 ,116),
(0 ,255 ,120),
(0 ,155 ,255),
(0 ,100 ,1),
(0 ,118 ,255),
(133 ,169 ,0),
(0 ,185 ,23),
(120 ,130 ,49),
(0 ,255 ,198),
(255 ,110 ,65),
(232 ,94 ,190)]

for i in range(len(color_list)):
    (r,g,b) = color_list[i]
    color_list[i] = (r/255, g/255, b/255)


def read_colorings(fname):
    with open(fname, "r") as f:
        i = 0
        h = []
        h_coloring = []
        for line in f:
            if (i % 5 == 0):
                name = line
            if (i % 5 == 1):
                h_line = line
                #print(h_line, end="")
                (_,h_val) = h_line.split("=")
                h_val = int(h_val)
                h.append(h_val)
            if (i % 5 == 2):
                coloring = list(map(int, line.split()))
                h_coloring.append(coloring)
            if (i % 5 == 3):
                diameter = line
            if (i % 5 == 4):
                None
            i += 1
        return h, h_coloring


def read_kn_min(n):
    with open("types/best{:03d}.asc".format(n), "r") as f:
        n = int(f.readline())
        kn_min = []
        for line in f:
            x, y = map(int, line.split())
            kn_min.append((x,y))

        return kn_min

#Test
#kn = 8
#kn_min = read_kn_min(kn)
#kn_min_Epp2 = map_A(kn, [kn_min], Epp2)

#write_otypes_A(kn, kn_min_Epp2, prefix="epp_min")
#_m, coloringk7_min = read_colorings("Harmonious-coloring/results/epp_min07.out")
#draw_points(k7_min, coloringk7_min[0]).plot()

