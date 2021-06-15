from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
import os
from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.FabricantesControlador import FabricantesControlador

from Repositorio.Entidades.Fabricante import Fabricante


class FabricantesView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.fabricantesControlador = FabricantesControlador()

    def createFabricante(self):
        u = self.utilView
        os.system('cls')
        fabricante = self.receberAtributos()
        
        try:
            fabricanteCriado = self.fabricantesControlador.createFabricante(fabricante)
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printSucesso('Fabricante criado com sucesso!')
            self.imprimir([fabricanteCriado])
        except Exception as ex:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao criar o fabricante! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')

    def readFabricante(self):
        os.system('cls')
        id_fabricante = self.utilView.receberValor(valorPrint="id do fabricante", chave="digite o id do fabricante que deseja vizualizar", tipo=int, obrigatorio=True)
        self.imprimirFabricantes(id_fabricante=id_fabricante, resumido=False)
        os.system('pause')

    def imprimirFabricantes(self, id_fabricante=None, resumido=True):
        u = self.utilView
        os.system('cls')
        fabricantes = []
        try:
            if id_fabricante != None:
                fabricante = self.fabricantesControlador.readFabricante(id_fabricante)
                if fabricante != None:
                    fabricantes.append(fabricante)
            else:
                fabricantes = self.fabricantesControlador.readFabricantes()

            if len(fabricantes) > 0:              
                if resumido:
                    self.imprimirResumido(fabricantes)    
                else:
                    self.imprimir(fabricantes)
            else:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Nenhum fabricante encontrado!')
                u.printSeparador(f'{"="*70}')
        except Exception as ex:
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao buscar o(s) fabricante(s)! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')

    def updateFabricante(self):
        u = self.utilView
        os.system('cls')
        self.imprimirFabricantes()        
        idFabricante = self.utilView.receberValor(valorPrint="id do fabricante", chave="informe o id do fabricante que será alterado (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.fabricantesControlador.readFabricante(x) != None )        
        if idFabricante != 0:
            fabricante = self.fabricantesControlador.readFabricante(idFabricante)
            
            while True:
                os.system('cls')
                self.imprimir([fabricante])
                u.printInstrucao('informe qual valor você quer alterar: ')
                u.printOpcao('1', 'Nome')
                print('')
                u.printOpcao('0', 'Finalizar alteração')
                op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
                if op == 0:     
                    break                
                else:
                    if op == 1: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de nome", tipo=str, obrigatorio=True)
                        fabricante.setNome(valor)


            os.system('cls')
            self.imprimir([fabricante])
            u.printInstrucao('Deseja salvar as alterações?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                try:
                    self.fabricantesControlador.updateFabricante(fabricante)
                    u.printSucesso('O fabricante foi atualizado com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao atualizar a fabricante! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def deleteFabricante(self):
        u = self.utilView
        os.system('cls')
        self.imprimirFabricantes()
        idFabricante = self.utilView.receberValor(valorPrint="id do fabricante", chave="informe o id do fabricante que será removido (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.fabricantesControlador.readFabricante(x) != None )
        if idFabricante != 0:
            self.imprimirFabricantes(idFabricante, False)
            u.printInstrucao(f'Tem certeza que quer excluir esse fabricante?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                try:
                    self.fabricantesControlador.deleteFabricante(idFabricante)
                    u.printSucesso('O fabricante foi removido com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao remover o fabricante! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def imprimirMenu(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Manipulação de Fabricantes')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Criar um fabricante novo.')
            u.printOpcao('2', 'Buscar um fabricante.')
            u.printOpcao('3', 'Listar todos os fabricantes.')
            u.printOpcao('4', 'Atualizar um fabricante.')
            u.printOpcao('5', 'Remover um fabricante.')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')
            
            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                self.createFabricante()
            elif op == 2:
                self.readFabricante()
            elif op == 3:
                self.imprimirFabricantes(resumido=False)
                os.system('pause')
            elif op == 4:
                self.updateFabricante()
            elif op == 5:
                self.deleteFabricante()
            elif op == 0:
                break


    def imprimir(self, fabricantes):
        u = self.utilView        
        for fabricante in fabricantes:
            u.printSeparador(f'='*70)
            self.utilView.imprimirAtributTitulo('Id', fabricante.getIdFabricante(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', fabricante.getNome(), '\n')
            u.printSeparador(f'{"="*70}\n\n')
    
    def imprimirResumido(self, fabricantes):   
        u = self.utilView     
        for fabricante in fabricantes:
            u.printSeparador('='*70)
            self.utilView.imprimirAtributTitulo('Id', fabricante.getIdFabricante(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', fabricante.getNome(), '\n')
        u.printSeparador('='*70)
    
    def receberAtributos(self):
        u = self.utilView
        fabricante = Fabricante()
        atributos = ['nome']
        for atributo in atributos:
            os.system('cls')
            self.imprimir([fabricante])
            u.printInstrucao('Por favor digite as informações do novo fabricante:')        
            fabricante = self.receberAtributo(atributo, fabricante)
        return fabricante


    def receberAtributo(self, atributoChave, fabricante):
        u = self.utilView
        
        if atributoChave == 'nome':
            fabricante.setNome(self.utilView.receberValor(chave="nome", tipo=str, obrigatorio=True))
        return fabricante
        
        