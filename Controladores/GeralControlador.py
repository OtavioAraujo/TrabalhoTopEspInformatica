from Servicos.SwapiService import SwapiService
import os
import json
from Servicos.NavesServico import NavesServico
from Servicos.UsuariosServico import UsuariosServico
from Servicos.FabricantesServico import FabricantesServico
import zipfile as zip


class GeralControlador:
    def __init__(self):
        self.fabricantesServico = FabricantesServico() 
        self.navesServico = NavesServico()        
        self.usuariosServico = UsuariosServico()
        self.SwapiService = SwapiService()
    
    def exportarTodosOsDados(self):
        fabricantes = self.fabricantesServico.readFabricantes()
        naves = self.navesServico.readNaves()
        usuarios = self.usuariosServico.readUsuarios()

        for nave in naves:
            nave.capacidade_carga = float(nave.capacidade_carga) if nave.capacidade_carga != None else None
            nave.preco = float(nave.preco) if nave.preco != None else None

        listaTotal = {
            "fabricantes" : [fabricante.__dict__ for fabricante in fabricantes],
            "naves": [nave.__dict__ for nave in naves],
            "usuarios" : [usuario.__dict__ for usuario in usuarios],
        }
        listaTotalJson = json.dumps(listaTotal, ensure_ascii=False)

        dirDownloads = os.path.join(os.sep, os.path.expanduser('~') , 'Downloads', )
        dir = os.path.join(os.sep, dirDownloads, 'DadosExportadosTopEspInf.zip')
        
        arquivoZip = zip.ZipFile(dir, 'w')
        arquivoZip.writestr('DadosExportadosTopEspInf.json', listaTotalJson)
        arquivoZip.close()
        
    def readNavesApiSwapi(self):
        navesApi = self.SwapiService.readNavesApiSwapi()
        naves = self.SwapiService.converteNavesApiParaNavesDTO(navesApi)
        return naves
    
    def createNaveApiSwapi(self, nave):
        self.SwapiService.createNaveApiSwapi(nave)