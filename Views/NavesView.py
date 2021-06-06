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

    def createNave(self):
        os.system('cls')
        nave = self.receberValores()
        try:
            naveCriada = self.navesControlador.createNave(nave)
            os.system('cls')
            print('Nave criada com sucesso!')
            self.imprimir([naveCriada])
        except Exception as ex:
            os.system('cls')
            print('Erro ao criar a nave! Tente novamente.')
            print(F'ERRO: {ex}')
        os.system('pause')

    def readNave(self):
        os.system('cls')
        id_nave = self.utilView.receberValor(chave="digite o id da nave que deseja vizualizar", tipo=int, obrigatorio=True)
        self.imprimirNaves(id_nave=id_nave, resumido=False)
        os.system('pause')

    def imprimirNaves(self, id_nave=None, resumido=True):
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
                print('Nenhuma nave encontrada!')
        except Exception as ex:
            print('Erro ao buscar a(s) nave(s)! Tente novamente.')
            print(F'ERRO: {ex}')

    def updateNave(self):
        os.system('cls')
        self.imprimirNaves()        
        idNave = self.utilView.receberValor(chave="informe o id da nave que será alterada", tipo=int, obrigatorio=True, validos=lambda x: self.navesControlador.readNave(x) != None)
        nave = self.navesControlador.readNave(idNave)
        
        while True:
            os.system('cls')
            self.imprimir([nave])
            print('informe qual valor você quer alterar: ')
            print('1 - Nome')
            print('2 - Fabricante')
            print('3 - Modelo')
            print('4 - Tripulacao')
            print('5 - Passageiros')
            print('6 - Capacidade de Carga')
            print('7 - Preço')
            print('0 - Finalizar alteração')
            op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
            if op == 0:     
                break                
            else:
                if op == 1: 
                    valor = self.utilView.receberValor(chave="informe o novo nome", tipo=str, obrigatorio=True)
                    nave.setNome(valor)
                elif op == 2: 
                    # Imprimir resumido fornecedores
                    print('Imprimir resumido fornecedores')
                    valor = self.utilView.receberValor(chave="informe o novo fabricante", tipo=int,)
                    nave.setIdFabricante(valor)
                elif op == 3: 
                    valor = self.utilView.receberValor(chave="informe o novo modelo", tipo=str,)
                    nave.setModelo(valor)
                elif op == 4: 
                    valor = self.utilView.receberValor(chave="informe o novo tripulacao", tipo=int,)
                    nave.setTripulacao(valor)
                elif op == 5: 
                    valor = self.utilView.receberValor(chave="informe o novo passageiros", tipo=int,)
                    nave.setPassageiros(valor)
                elif op == 6: 
                    valor = self.utilView.receberValor(chave="informe o novo capacidade de carga", tipo=float,)
                    nave.setCapacidadeCarga(valor)
                elif op == 7: 
                    valor = self.utilView.receberValor(chave="informe o novo preço", tipo=float,)
                    nave.setPreco(valor)


        os.system('cls')
        self.imprimir([nave])
        print('Deseja salvar as alterações?')
        print('1 - Sim')
        print('2 - Não')
        op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
        if op == 1: 
            try:
                self.navesControlador.updateNave(nave)
                print('A nave foi atualizada com sucesso!')  
            except Exception as ex:
                print('Erro ao atualizar a nave! Tente novamente.')  
                print(F'ERRO: {ex}')
            os.system('pause')

    def deleteNave(self):
        os.system('cls')
        self.imprimirNaves()
        idNave = self.utilView.receberValor(chave="informe o id da nave que será removida (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.navesControlador.readNave(x) != None )
        if idNave != 0:
            self.imprimirNaves(idNave, False)
            print(f'Tem cereza que quer excluir essa nave?')
            print('1 - Sim')
            print('2 - Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(1, 3))
            if op == 1:
                os.system('cls')
                try:
                    self.navesControlador.deleteNave(idNave)
                    print('A nave foi removida com sucesso!')  
                except Exception as ex:
                    print('Erro ao remover a nave! Tente novamente.')  
                    print(F'ERRO: {ex}')
                os.system('pause')

    def imprimirMenu(self):
        while True:
            os.system('cls')
            print('Qual operação desja realizar?')
            print('1 - Criar uma nave nova.')
            print('2 - Buscar uma nave.')
            print('3 - Listar todas as naves.')
            print('4 - Atualizar uma nave.')
            print('5 - Remover uma nave.')
            print('0 - Sair')
            
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


    def imprimir(self, naves):        
        for nave in naves:
            print('='*50)
            self.utilView.imprimirAtributo('Id', nave.getIdNave(), '\n')
            self.utilView.imprimirAtributo('Nome', nave.getNome(), '\n')
            print('-'*50)
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
        print('='*50)
    
    def imprimirResumido(self, naves):        
        for nave in naves:
            print('='*50)
            self.utilView.imprimirAtributo('Id', nave.getIdNave(), ' ')
            self.utilView.imprimirAtributo('Nome', nave.getNome(), '\n')
        print('='*50)
    
    def receberValores(self):
        print('Por favor digite as informações da nova nave:')
        nave = Nave()
        nave.setNome(self.utilView.receberValor(chave="nome", tipo=str, obrigatorio=True))  
        # Listar os fabricantes        
        nave.setIdFabricante(self.utilView.receberValor(chave="fabricante", tipo=int, obrigatorio=False))
        nave.setModelo(self.utilView.receberValor(chave="modelo", tipo=str, obrigatorio=True))
        nave.setTripulacao(self.utilView.receberValor(chave="tripulacao", tipo=int, obrigatorio=False))
        nave.setPassageiros(self.utilView.receberValor(chave="passageiros", tipo=int, obrigatorio=False))
        nave.setCapacidadeCarga(self.utilView.receberValor(chave="capacidade de carga", tipo=float, obrigatorio=False))
        nave.setPreco(self.utilView.receberValor(chave="preco", tipo=float, obrigatorio=False))
        return nave