from Compartilhados.utilitarios import utilitarios
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
from Servicos.UsuariosServico import UsuariosServico


class UsuariosControlador:
    def __init__(self):
        self.usuariosServico = UsuariosServico()

    def createUsuario(self, usuario):
        self.validarConsistensiaDeUsuario(usuario)
        self.usuariosServico.createUsuario(usuario)

    def readUsuarios(self):
        return self.usuariosServico.readUsuarios()
        
    def readUsuario(self, id_usuario):

        idValido = self.usuariosServico.idValido(id_usuario)
        if (not idValido):
            raise ValoresInvalidosException(menssagem=f"O id da usuario informado não é válido!")

        return self.usuariosServico.readUsuario(id_usuario)

    def updateUsuario(self, usuario):

        self.possuiId(usuario.getIdUsuario())

        self.validarConsistensiaDeUsuario(usuario)

        self.usuariosServico.updateUsuario(usuario)

    def deleteUsuario(self, id_usuario):
        self.possuiId(id_usuario)
        self.usuariosServico.deleteUsuario(id_usuario)

    def validarConsistensiaDeUsuario(self, usuario):
        vlrsObrgNaoPreech = self.usuariosServico.valoresObrigatoriosNaoPreenchidos(usuario)
        if (len(vlrsObrgNaoPreech) > 0):
            raise ValoresInvalidosException(menssagem=f"Os valores a seguir são obrigatórios: {utilitarios.listarPorExtenso(vlrsObrgNaoPreech)}. Por favor, preencha-os.")

        emailJaExiste = self.usuariosServico.emailJaExiste(usuario)
        if (emailJaExiste):
            raise ValoresInvalidosException(menssagem=f"O email informado já existe!")
    
    def possuiId(self, id_usuario):
        possuiId = self.usuariosServico.possuiId(id_usuario)
        if (not possuiId):
            raise ValoresInvalidosException(menssagem=f"O id da usuario informado não é válido!")