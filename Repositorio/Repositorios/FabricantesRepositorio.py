from Repositorio.Conexao.conexao import ConexaoPostgre

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
        listaFabricantes = cur.fetchall()

        con.close()
        return listaFabricantes
        
    def readFabricante(self, id_fabricante):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_fabricante, 
                         nome
	              FROM tb_fabricante
                  WHERE tb_fabricante.id_fabricante = {id_fabricante};"""

        cur.execute(sql)  
        fabricante = cur.fetchall()      

        con.close()
        if len(fabricante) > 0:
            return fabricante[0]
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
        