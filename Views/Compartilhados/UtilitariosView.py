from Views.Compartilhados.Estilos import Estilos


class utilitariosView:

    def __init__(self):
        self.estilos = Estilos()

    def imprimirAtributo(self, chave, valor):
        e = self.estilos
        print(f'{e.atributoChave(f"{chave}:")} {e.atributoValor(valor)}')