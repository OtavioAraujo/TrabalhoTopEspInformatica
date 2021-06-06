from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.NavesControlador import NaveControlador


class NavesView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.navesControlador = NaveControlador()
    
    def imprimirNaves(self, id_nave=None):
        if not id_nave == None:
            naves = list(self.navesControlador.readNave(id_nave))
        else:
            naves = self.navesControlador.readNaves()
        self.imprimir(naves)

    def imprimir(self, naves):        
        for nave in naves:
            print('='*30)
            self.utilView.imprimirAtributo('Nome', nave.nome)
            print('-'*30)
            self.utilView.imprimirAtributo('Fabricante', nave.id_fabricante)
            self.utilView.imprimirAtributo('Modelo', nave.modelo)
            self.utilView.imprimirAtributo('Tripulacao', nave.tripulacao)
            self.utilView.imprimirAtributo('Passageiros', nave.passageiros)
            self.utilView.imprimirAtributo('Capacidade_carga', nave.capacidade_carga)
            self.utilView.imprimirAtributo('Preco', nave.preco)
        print('='*30)
