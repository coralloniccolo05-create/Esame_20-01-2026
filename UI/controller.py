import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb = int(self._view.txtNumAlbumMin.value)
            if n_alb < 0:
                self._view.show_alert('Inserire un numero maggiore di 0')
                self._view.txtNumAlbumMin.value = ''
            self._model.load_artists_with_min_albums(n_alb)
            graph = self._model.build_graph()
            self._view.txt_result.controls.append(ft.Text(f'Grafo creato: {graph.number_of_nodes()} nodi, {graph.number_of_edges()} archi'))
            self._view.ddArtist.disabled = False
            self._view.btnArtistsConnected.disabled = False
        except ValueError:
            self._view.show_alert('Numero inserito non valido')
        self._view.update_page()

    def handle_connected_artists(self, e):
        n_alb = int(self._view.txtNumAlbumMin.value)
        lista_nodi = self._model.load_artists_with_min_albums(n_alb)
        for artist in lista_nodi:
            self._view.ddArtist.options.append(str(artist))
        self._view.update_page()


