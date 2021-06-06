from Repositorio.Repositorios.NavesRepositorio import NavesRepositorio


class NavesServico:

    def __init__(self):
        self.navesRepositorio = NavesRepositorio()

    def createNave(self, nave):
        return self.navesRepositorio.createNave(nave)
    
    def readNaves(self):
        return self.navesRepositorio.readNaves()
    
    def readNave(self, id_nave):
        return self.navesRepositorio.readNave(id_nave)

    def updateNave(self, nave):
        self.navesRepositorio.updateNave(nave)

    def deleteNave(self, id_nave):
        self.navesRepositorio.deleteNave(id_nave)

    def valoresObrigatoriosNaoPreenchidos(self, nave):
        vlrsObrgNaoPreech = []

        if (nave.getNome() == None or nave.getNome() == ""):
            vlrsObrgNaoPreech.append(nave.getNome())

        if (nave.getModelo() == None or nave.getModelo() == ""):
            vlrsObrgNaoPreech.append(nave.getModelo())

        return vlrsObrgNaoPreech    
    
    def nomeJaExiste(self, nave):
        return self.navesRepositorio.nomeJaExiste(nave)

    def idValido(self, idNave):
        try:
            if idNave != None and int(idNave):
                return True
            else:
                return False    
        except:
            return False
    
    def possuiId(self, id_nave):
        return id_nave != None