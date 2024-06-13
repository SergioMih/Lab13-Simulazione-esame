import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        for year in range(1910,2015):
            self._view.ddyear.options.append(ft.dropdown.Option( year))
        self._view.update_page()

    def fillShape(self,e):
        self.data_scelta=e.control.value
        print(self.data_scelta)
        for shape in self._model.getShapes(self.data_scelta):
            print (shape)
            self._view.ddshape.options.append(ft.dropdown.Option(shape))
        self._view.update_page()

    def readShape(self,e):
        self.shape = e.control.value

    def handle_graph(self, e):
        tupla = self._model.buildGraph(self.shape)
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getDetails()}"))
        for t in tupla:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {t[0]}, somma dei pesi {t[1]}"))
        self._view.update_page()
    def handle_path(self, e):
        pass