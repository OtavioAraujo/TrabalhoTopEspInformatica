from Controladores.NavesControlador import NaveControlador
import requests
from Repositorio.Entidades.Nave import Nave


class SwapiService:
    def __init__(self):
        self.naveControlador = NaveControlador()
        self.url_veiculos = 'https://swapi.dev/api/vehicles/'
        
    def readNavesApiSwapi(self):        
        respostaAPI = requests.get(url=self.url_veiculos)
        navesApi = respostaAPI.json()['results']
        return navesApi        
    
    def converteNavesApiParaNavesEntidade(self, navesApi):
        navesEntidades = [self.converteNaveApiParaNaveEntidade(v) for v in navesApi]
        return navesEntidades
    
    def converteNaveApiParaNaveEntidade(self, naveApi):
        naveEntidade = Nave()
        naveEntidade.setIdNave(int(naveApi['url'].replace('http://swapi.dev/api/vehicles/', '').replace('/', '')))
        naveEntidade.setNome(naveApi['name'])
        # Verificar se o fabricante existe no banco - se n existir criar
        # buscar pelo nome        
        naveEntidade.setIdFabricante(1)
        naveEntidade.setModelo(naveApi['model'])
        naveEntidade.setTripulacao(naveApi['crew'])
        naveEntidade.setPassageiros(naveApi['passengers'])
        naveEntidade.setCapacidadeCarga(naveApi['cargo_capacity'])
        naveEntidade.setPreco(naveApi['cost_in_credits'])
        return naveEntidade

    def createNaveApiSwapi(self, nave):
        self.naveControlador.createNave(nave)