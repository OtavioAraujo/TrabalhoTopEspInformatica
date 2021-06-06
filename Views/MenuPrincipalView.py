import os
from Views.NavesView import NavesView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuPrincipalView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.navesView = NavesView()

    def iniciarMenuPrincipal(self):
        while True:
            os.system('cls')
            print('Qual operação deseja realizar?')
            print('1 - Manipular usuários')
            print('2 - Manipular nave')
            print('3 - Manipular fabricante')
            print('4 - Exportar todos os dados')
            print('5 - Importar dados da API')
            print('0 - Sair')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 4))
            if op == 1: 
                pass
            elif op == 2:
                self.navesView.imprimirMenu()
            elif op == 3:
                pass
            elif op == 0:
                break
            