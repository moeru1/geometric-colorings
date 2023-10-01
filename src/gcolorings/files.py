# lee archivo
import numpy as np
import random
import os


def otype_info(n):
    dtype_read = ">u1"
    suffix = "b08"
    dtype_m = np.int32
    if n >= 9:
        dtype = ">u2"
        suffix = "b16"
        dtype_m = np.int64
    return (dtype_read, suffix, dtype_m)


def num_otypes_from_info(n: int, ot_info):
    (_, sufix, dtype_m) = ot_info
    bsize = os.path.getsize("types/otypes{:02}.{}".format(n, suffix))
    bsize_num = 1 if suffix == "b08" else 2
    return bsize // (bsize_num * 2)


def read_otypes(n):
    dtype_read = ">u1"
    suffix = "b08"
    dtype_m = np.int32
    if n >= 9:
        dtype = ">u2"
        suffix = "b16"
        dtype_m = np.int64
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        points_all = np.fromfile(f, dtype=dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all) // (n * 2)  # numero de order types
        # print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            points = []
            for j in range(0, 2 * n, 2):
                points.append(
                    (points_all[i * (n * 2) + j], points_all[i * (n * 2) + j + 1])
                )

            # E = [(a,b) for a in range(n) for b in range(a+1, n)]
            # print(points)
            # G = D(points,E)
            # graph_list.append(G)
            points_set.append(points)
        return points_set


def read_otypes_random(n, p=0.5):
    dtype_read = ">u1"
    suffix = "b08"
    dtype_m = np.int32
    if n >= 9:
        dtype_read = ">u2"
        suffix = "b16"
        dtype_m = np.int64
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        points_all = np.fromfile(f, dtype=dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all) // (n * 2)  # numero de order types
        # print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            if random.random() <= p:
                points = []
                for j in range(0, 2 * n, 2):
                    points.append(
                        (points_all[i * (n * 2) + j], points_all[i * (n * 2) + j + 1])
                    )

                # E = [(a,b) for a in range(n) for b in range(a+1, n)]
                # print(points)
                # G = D(points,E)
                # graph_list.append(G)
                points_set.append(points)
        return points_set


def read_otypes_randomnm(n, m=1):
    indexes = []
    (dtype_read, suffix, dtype_m) = otype_info(n)
    num_otypes = num_otypes_from_info(n, (dtype_read, suffix, dtype_m))
    for i in range(m):
        r = random.randint(0, num_otypes - 1)
        indexes.append(r)
    num_otypes.sort()
    l = 0
    with open("types/otypes{:02d}.{}".format(n, suffix), "r") as f:
        # if
        points_all = np.fromfile(f, dtype=dtype_read).astype(dtype=dtype_m)
        n_ot = len(points_all) // (n * 2)  # numero de order types
        # print(n_ot)
        points_set = []
        graph_list = []
        for i in range(n_ot):
            points = []
            for j in range(0, 2 * n, 2):
                points.append(
                    (points_all[i * (n * 2) + j], points_all[i * (n * 2) + j + 1])
                )

            # E = [(a,b) for a in range(n) for b in range(a+1, n)]
            # print(points)
            # G = D(points,E)
            # graph_list.append(G)
            points_set.append(points)
        return points_set


"""Generates the adjacency graph A(G) from the point set `points_set`"""


def map_A(n, points_set, A):
    E = [(a, b) for a in range(n) for b in range(a + 1, n)]
    graph_list = []
    for points in points_set:
        G = A(points, E)
        graph_list.append(G)
    return graph_list


def write_otypes_A(n, graph_list, prefix="adj_otypes", order_i=[]):
    if order_i == []:
        order_i = range(len(graph_list))
    with open("types/{}{:02d}.in".format(prefix, n), "w") as f:
        print("{0} {1}".format(n * (n - 1) / 2, len(graph_list)), file=f)
        # relabel graph
        for k in order_i:
            V = graph_list[k].vertices()
            labels = {V[i]: i + 1 for i in range(len(V))}
            graph_list[k].relabel(labels, inplace=True)
            print("Graph {0}".format(k + 1), file=f)
            for v in graph_list[k].vertex_iterator():
                neighbors = graph_list[k].neighbors(v)
                print("{} : {}".format(v, " ".join(map(str, neighbors))), file=f)
    # f.close()
