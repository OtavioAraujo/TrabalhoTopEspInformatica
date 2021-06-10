from Compartilhados.utilitarios import utilitarios
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
from Servicos.FabricantesServico import FabricantesServico


class FabricantesControlador:
    def __init__(self):
        self.fabricantesServico = FabricantesServico()

    def createFabricante(self, fabricante):
        self.validarConsistensiaDeFabricante(fabricante)
        self.fabricantesServico.createFabricante(fabricante)

    def readFabricantes(self):
        return self.fabricantesServico.readFabricantes()

    def readFabricante(self, id_fabricante):

        idValido = self.fabricantesServico.idValido(id_fabricante)
        if (not idValido):
            raise ValoresInvalidosException(
                menssagem=f"O id do fabricante informado não é válido!")

        return self.fabricantesServico.readFabricante(id_fabricante)

    def readFabricantePorNome(self, nome):

        return self.fabricantesServico.readFabricantePorNome(nome)

    def updateFabricante(self, fabricante):

        self.possuiId(fabricante.getIdFabricante())

        self.validarConsistensiaDeFabricante(fabricante)

        self.fabricantesServico.updateFabricante(fabricante)

    def deleteFabricante(self, id_fabricante):
        self.possuiId(id_fabricante)
        self.fabricantesServico.deleteFabricante(id_fabricante)

    def validarConsistensiaDeFabricante(self, fabricante):
        vlrsObrgNaoPreech = self.fabricantesServico.valoresObrigatoriosNaoPreenchidos(
            fabricante)
        if (len(vlrsObrgNaoPreech) > 0):
            raise ValoresInvalidosException(
                menssagem=f"Os valores a seguir são obrigatórios: {utilitarios.listarPorExtenso(vlrsObrgNaoPreech)}. Por favor, preencha-os.")

        nomeJaExiste = self.fabricantesServico.nomeJaExiste(fabricante)
        if (nomeJaExiste):
            raise ValoresInvalidosException(
                menssagem=f"O nome informado já existe!")

        # verificar se fabricante existe

    def possuiId(self, id_fabricante):
        possuiId = self.fabricantesServico.possuiId(id_fabricante)
        if (not possuiId):
            raise ValoresInvalidosException(
                menssagem=f"O id do fabricante informado não é válido!")
