import os
from Views.NavesView import NavesView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuPrincipalView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.navesView = NavesView()

    def iniciarMenuPrincipal(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Menu Principal')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Manipular usuários')
            u.printOpcao('2', 'Manipular nave')
            u.printOpcao('3', 'Manipular fabricante')
            u.printOpcao('4', 'Exportar todos os dados')
            u.printOpcao('5', 'Importar dados da API')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                pass
            elif op == 2:
                self.navesView.imprimirMenu()
            elif op == 3:
                pass
            elif op == 4:
                pass
            elif op == 5:
                pass
            elif op == 0:
                break
            