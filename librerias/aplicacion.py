from librerias.interfaz.menu import Menu

class Aplicacion():
    def __init__(self):
        self.menu = Menu(self)

    def run(self):
        self.menu.render()
