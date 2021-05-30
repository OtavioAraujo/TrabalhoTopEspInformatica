from Repositorio.Conexao.conexao import ConexaoPostgre
from Repositorio.Entidades.Fabricante import Fabricante


class FabricantesRepositorio:
    def __init__(self):
        self.conexao = ConexaoPostgre()

    def createFabricante(self, fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""INSERT INTO tb_fabricante (
                      nome
                  ) VALUES (
                      '{fabricante.getNome()}'
                  );"""

        cur.execute(sql)
        con.commit()
        con.close()

    def readFabricantes(self):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_fabricante, 
                         nome
	              FROM tb_fabricante;"""

        cur.execute(sql)
        listaFabricanteBanco = cur.fetchall()
        listaFabricanteEntidade = self.converterListaBancoParaListaEntidade(
            listaFabricanteBanco)
        con.close()
        return listaFabricanteEntidade

    def readFabricante(self, id_fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_fabricante, 
                         nome
	              FROM tb_fabricante
                  WHERE tb_fabricante.id_fabricante = {id_fabricante};"""

        cur.execute(sql)
        fabricanteBanco = cur.fetchall()
        con.close()

        if len(fabricanteBanco) > 0:
            fabricanteEntidade = self.converterBancoParaEntidade(
                fabricanteBanco[0])
            return fabricanteEntidade
        else:
            return None

    def updateFabricante(self, fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""UPDATE tb_fabricante
                  SET nome='{fabricante.getNome()}'
	              WHERE tb_fabricante.id_fabricante = {fabricante.getIdFabricante()};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
        return fabricante

    def deleteFabricante(self, id_fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""DELETE FROM tb_fabricante
	              WHERE tb_fabricante.id_fabricante = {id_fabricante};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()

    def converterBancoParaEntidade(self, fabricanteBanco):
        fabricanteEntidade = Fabricante()
        fabricanteEntidade.setIdFabricante(fabricanteBanco[0])
        fabricanteEntidade.setNome(fabricanteBanco[1])
        return fabricanteEntidade

    def converterListaBancoParaListaEntidade(self, listaFabricanteBanco):
        listaFabricanteEntidade = []
        for fabricanteBanco in listaFabricanteBanco:
            listaFabricanteEntidade.append(
                self.converterBancoParaEntidade(fabricanteBanco))
        return listaFabricanteEntidade

    def nomeJaExiste(self, fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT count(1)
	              FROM tb_fabricante
                  WHERE tb_fabricante.nome = '{fabricante.getNome()}' """

        if fabricante.getIdFabricante() != None:
            sql += f"AND tb_fabricante.id_fabricante != {fabricante.getIdFabricante() }"

        cur.execute(sql)
        qtdFabricantes = cur.fetchall()
        con.close()

        if qtdFabricantes[0][0] > 0:
            return True
        else:
            return False
