from Repositorio.Repositorios.FabricantesRepositorio import FabricantesRepositorio


class FabricantesServico:

    def __init__(self):
        self.fabricantesRepositorio = FabricantesRepositorio()

    def createFabricante(self, fabricante):
        self.fabricantesRepositorio.createFabricante(fabricante)
    
    def readFabricantes(self):
        return self.fabricantesRepositorio.readFabricantes()
    
    def readFabricante(self, id_fabricante):
        return self.fabricantesRepositorio.readFabricante(id_fabricante)

    def readFabricantePorNome(self, nome):
        return self.fabricantesRepositorio.readFabricantePorNome(nome)

    def updateFabricante(self, fabricante):
        self.fabricantesRepositorio.updateFabricante(fabricante)

    def deleteFabricante(self, id_fabricante):
        self.fabricantesRepositorio.deleteFabricante(id_fabricante)

    def valoresObrigatoriosNaoPreenchidos(self, fabricante):
        vlrsObrgNaoPreech = []

        if (fabricante.getNome() == None or fabricante.getNome() == ""):
            vlrsObrgNaoPreech.append(fabricante.getNome())

        return vlrsObrgNaoPreech    
    
    def nomeJaExiste(self, fabricante):
        return self.fabricantesRepositorio.nomeJaExiste(fabricante)

    def idValido(self, idFabricante):
        try:
            if idFabricante != None and int(idFabricante):
                return True
            else:
                return False    
        except:
            return False
    
    def possuiId(self, id_fabricante):
        return id_fabricante != None
