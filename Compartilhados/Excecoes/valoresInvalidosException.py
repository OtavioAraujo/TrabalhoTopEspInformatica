class ValoresInvalidosException(Exception):
    def __init__(self, menssagem="Alguns valores informados são inválidos!"):
        self.message = menssagem
        super().__init__(self.message)