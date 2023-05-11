from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    @property
    def ativos(self):
        return self.model.ativos

    @property
    def periodos(self):
        return self.model.periodos



