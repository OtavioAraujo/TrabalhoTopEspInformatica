import os
from Views.Compartilhados.UtilitariosView import utilitariosView


class SobreView:
    def __init__(self):
        self.utilView = utilitariosView()
    
    def imprimirSobre(self):
        u = self.utilView
        os.system('cls')
        try:
            u.printTitulo('Sobre')  
            u.printInstrucao('Tema: Sistema de gerenciamento de estoque de naves do StarWars')  
            u.printInstrucao('Desenvolvedores:\n\n - Otávio Araújo Jardim RA: 2840481923001\n - Hiago Jose Pereira RA: 2840481913011')  
            u.printSeparador(f'{"="*70}')
        except Exception as ex:     
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao visualizar a pagina Sobre! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        
        os.system('pause')
