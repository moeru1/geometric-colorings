from sage.all import *

# lee archivo
from urllib.request import urlretrieve
from urllib.parse import urljoin
from pathlib import Path
import numpy as np


class OTypesIO:
    BASE_URL = "http://www.ist.tugraz.at/aichholzer/research/rp/triangulations/ordertypes/data/"
    BASE_DIR = Path("otypes")

    # maybe change name to parse_otype?
    # read_otype: self, int -> [point_set]
    def read_otype(self, n: int):
        filename = Path(self._make_filename(n))
        points_set = []
        fullpath = Path(self.BASE_DIR, filename)
        # WARNING: Potential race condition in opening file
        if not fullpath.exists():
            self._download_otype_file(n)
        with open(fullpath, "r") as f:
            (dtype_read, _, dtype_m) = self._otype_info(n)
            points_all = np.fromfile(f, dtype=dtype_read).astype(dtype=dtype_m)
            # numero de order types
            n_ot = len(points_all) // (n * 2)
            points_set = []
            for i in range(n_ot):
                points = []
                for j in range(0, 2 * n, 2):
                    points.append(
                        (points_all[i * (n * 2) + j], points_all[i * (n * 2) + j + 1])
                    )
                points_set.append(points)
            return points_set

    def _download_otype_file(self, n: int):
        filename = Path(self._make_filename(n))
        self.BASE_DIR.mkdir(exist_ok=True)
        file_url = urljoin(self.BASE_URL, str(filename))
        fullpath = Path(self.BASE_DIR, filename)
        urlretrieve(file_url, str(fullpath))

    def read_cr_min(self, n: int):
        filename = Path("types/best{:03d}.asc".format(n))
        fullpath = Path(self.BASE_DIR, filename)
        if not fullpath.exists():
            self._download_cr_min(n)
        with open(fullpath, "r") as f:
            n = int(f.readline())
            kn_min = []
            for line in f:
                x, y = map(int, line.split())
                kn_min.append((x, y))
            return kn_min

    def _download_cr_min(self, n: int):
        BASE_URL = "http://www.ist.tugraz.at/aichholzer/research/rp/triangulations/crossing/data/"
        filename = "best{:03d}.asc".format(n)
        self.BASE_DIR.mkdir(exist_ok=True)
        file_url = urljoin(BASE_URL, str(filename))
        fullpath = Path(self.BASE_DIR, filename)
        urlretrieve(file_url, str(fullpath))

    def _make_filename(self, n: int) -> str:
        suffix = "b08" if n < 9 else "b16"
        return "otypes{:02}.{}".format(n, suffix)

    def _otype_info(self, n: int):
        dtype_read = ">u1"
        suffix = "b08"
        dtype_m = np.int32
        if n >= 9:
            dtype_read = ">u2"
            suffix = "b16"
            dtype_m = np.int64
        return (dtype_read, suffix, dtype_m)


class GraphIO:
    def write_graphs(self, graph_list: list, filename: Path):
        num_graphs = len(graph_list)
        with open(filename, "w") as f:
            num_vertex = graph_list[0].order()
            print("{0} {1}".format(num_vertex, num_graphs), file=f)
            # relabel graph
            for k in range(num_graphs):
                V = graph_list[k].vertices()
                labels = {V[i]: i + 1 for i in range(len(V))}
                graph_list[k].relabel(labels, inplace=True)
                print("Graph {0}".format(k + 1), file=f)
                for v in graph_list[k].vertex_iterator():
                    neighbors = graph_list[k].neighbors(v)
                    print("{} : {}".format(v, " ".join(map(str, neighbors))), file=f)

    def write_todir(self, graph_list, dir: Path, filename: Path):
        num_graphs = graph_list[0].order()
        fullpath = Path(dir, filename)
        dir.mkdir(exist_ok=True)
        self.write_graphs(graph_list, fullpath)

    def read_graphs(self, filename: Path):
        with open(filename, "r") as f:
            line = f.readline()
            (num_vertex, num_graphs) = map(int, line.split())
            graph_list = []
            for k in range(num_graphs):
                line = f.readline()
                (graph_name, graph_num) = line.split()
                G = Graph()
                for i in range(num_vertex):
                    line = f.readline()
                    (v, v_neighbors) = line.split(":")
                    v = int(v) - 1
                    v_neighbors = list(map(int, v_neighbors.split()))
                    for w in v_neighbors:
                        w = w - 1
                        G.add_edge(v, w)
                graph_list.append(G)
            return graph_list

    def read_colorings(self, fname):
        with open(fname, "r") as f:
            i = 0
            h = []
            h_coloring = []
            for line in f:
                if i % 5 == 0:
                    name = line
                if i % 5 == 1:
                    h_line = line
                    # print(h_line, end="")
                    (_, h_val) = h_line.split("=")
                    h_val = int(h_val)
                    h.append(h_val)
                if i % 5 == 2:
                    coloring = list(map(int, line.split()))
                    h_coloring.append(coloring)
                if i % 5 == 3:
                    diameter = line
                if i % 5 == 4:
                    None
                i += 1
            return h, h_coloring

#read functions
def read_Epp_otypes(n: int):
    BASE_DIR = Path("Epp")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "Epp_otypes{:02}.in".format(n))
    graph_list = GraphIO().read_graphs(fullpath)
    return graph_list

def read_D_otypes(n: int):
    BASE_DIR = Path("D")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "D_otypes{:02}.in".format(n))
    graph_list = GraphIO().read_graphs(fullpath)
    return graph_list

def read_W_otypes(n: int):
    BASE_DIR = Path("W")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "W_otypes{:02}.in".format(n))
    graph_list = GraphIO().read_graphs(fullpath)
    return graph_list

def read_I_otypes(n: int):
    BASE_DIR = Path("I")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "I_otypes{:02}.in".format(n))
    graph_list = GraphIO().read_graphs(fullpath)
    return graph_list

#Write functions
def write_Epp_otypes(graph_list):
    n = graph_list[0].order()
    BASE_DIR = Path("Epp")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "Epp_otypes{:02}.in".format(n))
    GraphIO().write_graphs(graph_list, fullpath)

def write_D_otypes(graph_list):
    n = graph_list[0].order()
    BASE_DIR = Path("D")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "D_otypes{:02}.in".format(n))
    GraphIO().write_graphs(graph_list, fullpath)

def write_W_otypes(graph_list):
    n = graph_list[0].order()
    BASE_DIR = Path("W")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "W_otypes{:02}.in".format(n))
    GraphIO().write_graphs(graph_list, fullpath)

def write_I_otypes(graph_list):
    n = graph_list[0].order()
    BASE_DIR = Path("I")
    BASE_DIR.mkdir(exist_ok=True)
    fullpath = Path(BASE_DIR, "I_otypes{:02}.in".format(n))
    GraphIO().write_graphs(graph_list, fullpath)
