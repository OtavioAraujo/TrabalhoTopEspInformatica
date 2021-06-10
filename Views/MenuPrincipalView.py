from Views.UsuariosView import UsuariosView
from Views.ImportacaoView import ImportacaoView
import os
from Views.ExportacaoView import ExportacaoView
from Views.NavesView import NavesView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuPrincipalView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.navesView = NavesView()
        self.exportacaoView = ExportacaoView()
        self.importacaoView = ImportacaoView()
        self.usuariosView = UsuariosView()


    def iniciarMenuPrincipal(self, usuarioLogado):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Menu Principal')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Visualizar perfil')
            u.printOpcao('2', 'Manipular nave')
            u.printOpcao('3', 'Manipular fabricante')
            u.printOpcao('4', 'Exportar todos os dados')
            u.printOpcao('5', 'Importar nave')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                self.usuariosView.imprimirMenu(usuarioLogado)
            elif op == 2:
                self.navesView.imprimirMenu()
            elif op == 3:
                pass
            elif op == 4:
                self.exportacaoView.exportarTodosOsDados()
            elif op == 5:
                self.importacaoView.importarNave()
            elif op == 0:
                os.system('cls')
                u.printInstrucao('Finalizando... volte sempre!')
                break
            