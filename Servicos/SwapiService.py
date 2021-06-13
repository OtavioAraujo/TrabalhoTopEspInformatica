from Repositorio.Entidades.Nave import Nave
from Repositorio.Entidades.Fabricante import Fabricante
from Controladores.FabricantesControlador import FabricantesControlador
from Controladores.NavesControlador import NaveControlador
import requests
from Repositorio.DTO.DTONaveSwapi import DTONaveSwapi


class SwapiService:
    def __init__(self):
        self.naveControlador = NaveControlador()
        self.fabricantesControlador = FabricantesControlador()
        self.url_veiculos = 'https://swapi.dev/api/vehicles/'
        
    def readNavesApiSwapi(self):        
        respostaAPI = requests.get(url=self.url_veiculos)
        navesApi = respostaAPI.json()['results']
        return navesApi        
    
    def converteNavesApiParaNavesDTO(self, navesApi):
        naveDTOs = [self.converteNaveApiParaNaveDTO(v) for v in navesApi]
        return naveDTOs
    
    def converteNaveApiParaNaveDTO(self, naveApi):
        naveDTO = DTONaveSwapi()
        naveDTO.setIdNave(int(naveApi['url'].replace('http://swapi.dev/api/vehicles/', '').replace('/', '')))
        naveDTO.setNomeFabricante(naveApi['manufacturer'])
        naveDTO.setNome(naveApi['name'])
        naveDTO.setModelo(naveApi['model'])
        naveDTO.setTripulacao(naveApi['crew'])
        naveDTO.setPassageiros(naveApi['passengers'])
        naveDTO.setCapacidadeCarga(naveApi['cargo_capacity'])
        naveDTO.setPreco(naveApi['cost_in_credits'])
        return naveDTO

    def createNaveApiSwapi(self, naveDTO):
        naveEntidade = self.converteNaveDTOParaNaveEntidade(naveDTO)
        self.naveControlador.createNave(naveEntidade)
    
    def converteNaveDTOParaNaveEntidade(self, naveDTO):
        fabricante = self.fabricantesControlador.readFabricantePorNome(naveDTO.getNomeFabricante())
        if fabricante == None:
            fabricante = Fabricante()
            fabricante.setNome(naveDTO.getNomeFabricante())
            fabricante = self.fabricantesControlador.createFabricante(fabricante)

        naveEntidade = Nave()
        naveEntidade.setIdNave(int(naveDTO.getIdNave()))
        naveEntidade.setIdFabricante(fabricante.getIdFabricante())
        naveEntidade.setNome(naveDTO.getNome())
        naveEntidade.setModelo(naveDTO.getModelo())
        naveEntidade.setTripulacao(naveDTO.getTripulacao())
        naveEntidade.setPassageiros(naveDTO.getPassageiros())
        naveEntidade.setCapacidadeCarga(naveDTO.getCapacidadeCarga())
        naveEntidade.setPreco(naveDTO.getPreco())
        return naveEntidade