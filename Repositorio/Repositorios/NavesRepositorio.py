from Repositorio.Entidades.Nave import Nave
from Repositorio.Conexao.conexao import ConexaoPostgre

class NavesRepositorio:
    def __init__(self):
        self.conexao = ConexaoPostgre()

    def createNave(self, nave):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""INSERT INTO tb_nave (
                      id_fabricante, 
                      nome, 
                      modelo, 
                      tripulacao,
                      passageiros, 
                      capacidade_carga, 
                      preco
                  ) VALUES (
                      {nave.getIdFabricante()}, 
                      '{nave.getNome()}', 
                      '{nave.getModelo()}', 
                      {nave.getTripulacao()}, 
                      {nave.getPassageiros()}, 
                      {nave.getCapacidadeCarga()}, 
                      {nave.getPreco()}
                  );"""

        cur.execute(sql)        
        con.commit()
        con.close()

    def readNaves(self):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_nave, 
                         id_fabricante, 
                         nome, 
                         modelo, 
                         tripulacao, 
                         passageiros, 
                         capacidade_carga, 
                         preco
	              FROM tb_nave;"""

        cur.execute(sql)  
        listaNaveBanco = cur.fetchall()
        listaNaveEntidade = self.converterListaBancoParaListaEntidade(listaNaveBanco)
        con.close()
        return listaNaveEntidade
        
    def readNave(self, id_nave):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_nave, 
                         id_fabricante, 
                         nome, 
                         modelo, 
                         tripulacao, 
                         passageiros, 
                         capacidade_carga, 
                         preco
	              FROM tb_nave
                  WHERE tb_nave.id_nave = {id_nave};"""

        cur.execute(sql)  
        naveBanco = cur.fetchall()      
        con.close()
        
        if len(naveBanco) > 0:
            naveEntidade = self.converterBancoParaEntidade(naveBanco[0])
            return naveEntidade
        else:
            return None

    def updateNave(self, nave):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""UPDATE tb_nave
	              SET id_fabricante={nave.getIdFabricante()},
                      nome='{nave.getNome()}', 
                      modelo='{nave.getModelo()}', 
                      tripulacao={nave.getTripulacao()}, 
                      passageiros={nave.getPassageiros()}, 
                      capacidade_carga={nave.getCapacidadeCarga()}, 
                      preco={nave.getPreco()}
	              WHERE tb_nave.id_nave = {nave.getIdNave()};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
        return nave

    def deleteNave(self, id_nave):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""DELETE FROM tb_nave
	              WHERE tb_nave.id_nave = {id_nave};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
    
    def converterBancoParaEntidade(self, naveBanco):
        naveEntidade = Nave()
        naveEntidade.setIdNave(naveBanco[0])
        naveEntidade.setIdFabricante(naveBanco[1])
        naveEntidade.setNome(naveBanco[2])
        naveEntidade.setModelo(naveBanco[3])
        naveEntidade.setTripulacao(naveBanco[4])
        naveEntidade.setPassageiros(naveBanco[5])
        naveEntidade.setCapacidadeCarga(naveBanco[6])
        naveEntidade.setPreco(naveBanco[7])
        return naveEntidade

    def converterListaBancoParaListaEntidade(self, listaNaveBanco):
        listaNaveEntidade = []
        for naveBanco in listaNaveBanco:
            listaNaveEntidade.append(self.converterBancoParaEntidade(naveBanco))
        return listaNaveEntidade
    
    def nomeJaExiste(self, nave):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT count(1)
	              FROM tb_nave
                  WHERE tb_nave.nome = '{nave.getNome()}' """

        if nave.getIdNave() != None:
            sql += f"AND tb_nave.id_nave != {nave.getIdNave()}"

        cur.execute(sql)  
        qtdNaves = cur.fetchall()      
        con.close()
        
        if qtdNaves[0][0] > 0:            
            return True
        else:
            return False