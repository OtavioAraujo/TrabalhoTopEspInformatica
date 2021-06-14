from Views.FabricantesView import FabricantesView
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
import os
from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.NavesControlador import NaveControlador
from Controladores.FabricantesControlador import FabricantesControlador

from Repositorio.Entidades.Nave import Nave


class NavesView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.navesControlador = NaveControlador()
        self.fabricantesControlador = FabricantesControlador()
        self.fabricantesView = FabricantesView()

    def createNave(self):
        u = self.utilView
        os.system('cls')
        nave = self.receberAtributos()
        
        try:
            naveCriada = self.navesControlador.createNave(nave)
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printSucesso('Nave criada com sucesso!')
            self.imprimir([naveCriada])
        except Exception as ex:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao criar a nave! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')

    def readNave(self):
        os.system('cls')
        id_nave = self.utilView.receberValor(chave="digite o id da nave que deseja vizualizar", tipo=int, obrigatorio=True)
        self.imprimirNaves(id_nave=id_nave, resumido=False)
        os.system('pause')

    def imprimirNaves(self, id_nave=None, resumido=True):
        u = self.utilView
        os.system('cls')
        naves = []
        try:
            if id_nave != None:
                nave = self.navesControlador.readNave(id_nave)
                if nave != None:
                    naves.append(nave)
            else:
                naves = self.navesControlador.readNaves()

            if len(naves) > 0:              
                if resumido:
                    self.imprimirResumido(naves)    
                else:
                    self.imprimir(naves)
            else:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Nenhuma nave encontrada!')
                u.printSeparador(f'{"="*70}')
        except Exception as ex:
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao buscar a(s) nave(s)! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')

    def updateNave(self):
        u = self.utilView
        os.system('cls')
        self.imprimirNaves()        
        idNave = self.utilView.receberValor(chave="informe o id da nave que será alterada (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.navesControlador.readNave(x) != None )        
        if idNave != 0:
            nave = self.navesControlador.readNave(idNave)
            
            while True:
                os.system('cls')
                self.imprimir([nave])
                u.printInstrucao('informe qual valor você quer alterar: ')
                u.printOpcao('1', 'Nome')
                u.printOpcao('2', 'Fabricante')
                u.printOpcao('3', 'Modelo')
                u.printOpcao('4', 'Tripulacao')
                u.printOpcao('5', 'Passageiros')
                u.printOpcao('6', 'Capacidade de Carga')
                u.printOpcao('7', 'Preço')
                print('')
                u.printOpcao('0', 'Finalizar alteração')
                op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
                if op == 0:     
                    break                
                else:
                    if op == 1: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de nome", tipo=str, obrigatorio=True)
                        nave.setNome(valor)
                    elif op == 2: 
                        self.fabricantesView.imprimirFabricantes(resumido=True)
                        valor = self.utilView.receberValor(chave="informe o novo valor de fabricante", tipo=int,)
                        nave.setIdFabricante(valor)
                    elif op == 3: 
                        valor = self.utilView.receberValor(chave="informe o novo modelo", tipo=str,)
                        nave.setModelo(valor)
                    elif op == 4: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de tripulacao", tipo=int,)
                        nave.setTripulacao(valor)
                    elif op == 5: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de passageiros", tipo=int,)
                        nave.setPassageiros(valor)
                    elif op == 6: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de capacidade de carga", tipo=float,)
                        nave.setCapacidadeCarga(valor)
                    elif op == 7: 
                        valor = self.utilView.receberValor(chave="informe o novo preço", tipo=float,)
                        nave.setPreco(valor)


            os.system('cls')
            self.imprimir([nave])
            u.printInstrucao('Deseja salvar as alterações?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                try:
                    self.navesControlador.updateNave(nave)
                    u.printSucesso('A nave foi atualizada com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao atualizar a nave! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def deleteNave(self):
        u = self.utilView
        os.system('cls')
        self.imprimirNaves()
        idNave = self.utilView.receberValor(chave="informe o id da nave que será removida (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.navesControlador.readNave(x) != None )
        if idNave != 0:
            self.imprimirNaves(idNave, False)
            u.printInstrucao(f'Tem cereza que quer excluir essa nave?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                try:
                    self.navesControlador.deleteNave(idNave)
                    u.printSucesso('A nave foi removida com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao remover a nave! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def imprimirMenu(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Manipulação de Naves')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Criar uma nave nova.')
            u.printOpcao('2', 'Buscar uma nave.')
            u.printOpcao('3', 'Listar todas as naves.')
            u.printOpcao('4', 'Atualizar uma nave.')
            u.printOpcao('5', 'Remover uma nave.')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')
            
            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                self.createNave()
            elif op == 2:
                self.readNave()
            elif op == 3:
                self.imprimirNaves(resumido=False)
                os.system('pause')
            elif op == 4:
                self.updateNave()
            elif op == 5:
                self.deleteNave()
            elif op == 0:
                break


    def imprimir(self, naves, navesDTO=False):
        u = self.utilView        
        for nave in naves:
            u.printSeparador(f'='*70)
            self.utilView.imprimirAtributTitulo('Id', nave.getIdNave(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', nave.getNome(), '\n')
            u.printSeparador('='*70)
            if navesDTO:
                fabricanteNome = nave.getNomeFabricante()
            else:
                try:
                    fabricanteNome = self.fabricantesControlador.readFabricante(nave.getIdFabricante()).getNome() 
                except ValoresInvalidosException as ex:
                    fabricanteNome = 'Desconhecido'
            self.utilView.imprimirAtributo('Fabricante', fabricanteNome, '\n')
            self.utilView.imprimirAtributo('Modelo', nave.getModelo(), '\n')
            self.utilView.imprimirAtributo('Tripulacao', nave.getTripulacao(), '\n')
            self.utilView.imprimirAtributo('Passageiros', nave.getPassageiros(), '\n')
            self.utilView.imprimirAtributo('Capacidade de Carga', nave.getCapacidadeCarga(), '\n')
            self.utilView.imprimirAtributo('Preco', nave.getPreco(), '\n')
            u.printSeparador(f'{"="*70}\n\n')
    
    def imprimirResumido(self, naves):   
        u = self.utilView     
        for nave in naves:
            u.printSeparador('='*70)
            self.utilView.imprimirAtributTitulo('Id', nave.getIdNave(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', nave.getNome(), '\n')
        u.printSeparador('='*70)
    
    def receberAtributos(self):
        u = self.utilView
        nave = Nave()
        atributos = ['nome', 'fabricante', 'modelo', 'tripulacao', 'passageiros', 'capacidadedecarga', 'preco']
        for atributo in atributos:
            os.system('cls')
            self.imprimir([nave])
            u.printInstrucao('Por favor digite as informações da nova nave:')        
            nave = self.receberAtributo(atributo, nave)
        return nave


    def receberAtributo(self, atributoChave, nave):
        u = self.utilView
        
        if atributoChave == 'nome':
            nave.setNome(self.utilView.receberValor(chave="nome", tipo=str, obrigatorio=True))  
        elif atributoChave == 'fabricante':
            self.fabricantesView.imprimirFabricantes(resumido=True)        
            nave.setIdFabricante(self.utilView.receberValor(chave="fabricante", tipo=int, obrigatorio=False, validos=lambda x: self.fabricantesControlador.readFabricante(x) != None ))
        elif atributoChave == 'modelo':
            nave.setModelo(self.utilView.receberValor(chave="modelo", tipo=str, obrigatorio=True))
        elif atributoChave == 'tripulacao':
            nave.setTripulacao(self.utilView.receberValor(chave="tripulacao", tipo=int, obrigatorio=False))
        elif atributoChave == 'passageiros':
            nave.setPassageiros(self.utilView.receberValor(chave="passageiros", tipo=int, obrigatorio=False))
        elif atributoChave == 'capacidadedecarga':
            nave.setCapacidadeCarga(self.utilView.receberValor(chave="capacidade de carga", tipo=float, obrigatorio=False))
        elif atributoChave == 'preco':
            nave.setPreco(self.utilView.receberValor(chave="preco", tipo=float, obrigatorio=False))
        return nave
        
        