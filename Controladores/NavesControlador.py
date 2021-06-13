from Servicos.FabricantesServico import FabricantesServico
from Compartilhados.utilitarios import utilitarios
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
from Servicos.NavesServico import NavesServico


class NaveControlador:
    def __init__(self):
        self.navesServico = NavesServico()
        self.fabricanteServico = FabricantesServico()


    def createNave(self, nave):
        self.validarConsistensiaDeNave(nave)
        return self.navesServico.createNave(nave)

    def readNaves(self):
        return self.navesServico.readNaves()
        
    def readNave(self, id_nave):

        idValido = self.navesServico.idValido(id_nave)
        if (not idValido):
            raise ValoresInvalidosException(menssagem=f"O id da nave informado não é válido!")

        return self.navesServico.readNave(id_nave)

    def updateNave(self, nave):

        self.possuiId(nave.getIdNave())

        self.validarConsistensiaDeNave(nave)

        self.navesServico.updateNave(nave)

    def deleteNave(self, id_nave):
        self.possuiId(id_nave)
        self.navesServico.deleteNave(id_nave)

    def validarConsistensiaDeNave(self, nave):
        vlrsObrgNaoPreech = self.navesServico.valoresObrigatoriosNaoPreenchidos(nave)
        if (len(vlrsObrgNaoPreech) > 0):
            raise ValoresInvalidosException(menssagem=f"Os valores a seguir são obrigatórios: {utilitarios.listarPorExtenso(vlrsObrgNaoPreech)}. Por favor, preencha-os.")

        nomeJaExiste = self.navesServico.nomeJaExiste(nave)
        if (nomeJaExiste):
            raise ValoresInvalidosException(menssagem=f"O nome informado já existe!")

        fabricanteNaoExiste = self.fabricanteServico.readFabricante(nave.getIdFabricante()) == None
        if (fabricanteNaoExiste):
            raise ValoresInvalidosException(menssagem=f"A nave informada não existe!")
    
    def possuiId(self, id_nave):
        possuiId = self.navesServico.possuiId(id_nave)
        if (not possuiId):
            raise ValoresInvalidosException(menssagem=f"O id da nave informado não é válido!")