from Repositorio.Entidades.Usuario import Usuario
from Views.UsuariosView import UsuariosView
import os
from Views.MenuPrincipalView import MenuPrincipalView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuLoginView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.menuPrincipalView = MenuPrincipalView()
        self.usuariosView = UsuariosView()
        
    def iniciarMenuLogin(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Menu de Login')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Logar')
            u.printOpcao('2', 'Criar uma conta')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                usuarioLogado = Usuario()
                usuarioLogado.setIdUsuario(1)
                usuarioLogado.setEMail('email@email.com.br')
                usuarioLogado.setNome('jão')
                usuarioLogado.setSenha('123')
                self.menuPrincipalView.iniciarMenuPrincipal(usuarioLogado)
            elif op == 2:
                self.usuariosView.createUsuario()
            elif op == 0:
                os.system('cls')
                u.printInstrucao('Finalizando... volte sempre!')
                break
            