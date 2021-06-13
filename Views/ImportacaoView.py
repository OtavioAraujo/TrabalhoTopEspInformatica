import os
from Views.NavesView import NavesView
from Controladores.GeralControlador import GeralControlador
from Views.Compartilhados.UtilitariosView import utilitariosView


class ImportacaoView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.geralControlador = GeralControlador()
        self.navesView = NavesView()
    
    def importarNave(self):
        u = self.utilView
        os.system('cls')
        try:
            navesSwapi = self.geralControlador.readNavesApiSwapi()
            self.navesView.imprimir(navesSwapi, navesDTO=True)

            u.printInstrucao('Digite o ID da nave que deseja importar (digite 0 para cancelar):')
            op = self.utilView.receberValor(chave="id da nave", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or x in [n.getIdNave() for n in navesSwapi if n.getIdNave() == x])
            
            if op != 0:
                self.geralControlador.createNaveApiSwapi([n for n in navesSwapi if n.getIdNave() == op][0])
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                u.printSucesso('A nave foi importada com sucesso!')  
                u.printSeparador(f'{"="*70}')
                os.system('pause') 
        except Exception as ex:     
            os.system('cls')               
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao importar a nave! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
            os.system('pause')
