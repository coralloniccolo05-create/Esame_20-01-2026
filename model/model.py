import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self._nodes = []
        self.id_map = {}

        self.load_all_artists()


    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()



    def load_artists_with_min_albums(self, min_albums):
        self._nodes = DAO.get_nodes(min_albums)
        return self._nodes


    def build_graph(self):
        self._graph.clear()
        for node in self._nodes:
            self._graph.add_node(node)

        peso = 0
        lista_art_gen = DAO.get_art_gen()
        for art1, gen1 in lista_art_gen:
            for art2, gen2 in lista_art_gen[1:]:
                if art1 in self._nodes and art2 in self._nodes:
                    if art1 != art2 and gen1 == gen2:
                        peso += 1
                        self._graph.add_edge(art1, art2, peso=peso)
        return self._graph

    def get_neighbur(self, n_start):
        return self._graph.neighbors(n_start)




