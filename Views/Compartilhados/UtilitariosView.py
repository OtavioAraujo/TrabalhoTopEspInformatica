from Views.Compartilhados.Estilos import Estilos


class utilitariosView:

    def __init__(self):
        self.estilos = Estilos()

    def imprimirAtributo(self, chave, valor, final):
        e = self.estilos
        print(f'{e.atributoChave(f"{chave}:")} {e.atributoValor(valor if valor != None else "Desconhecido"):>5}', end=final)
    
    def receberValor(self, chave, tipo, obrigatorio=False, validos=None, larguraInt=23, casasDec=2):
        while True:
            try:
                valor = input(f'{chave.capitalize()}: ').strip()
                if obrigatorio and valor == "":
                    print(f'O {chave.lower()} deve ser informado.')  
                    continue            
                if tipo == float and len(valor) > larguraInt:
                    print(f'O {chave.lower()} deve ter no máximo {larguraInt - casasDec} casas inteiras e {casasDec} casas decimais.')  
                    continue
                if tipo == float and valor[::-1].find('.') > casasDec:
                    print(f'O {chave.lower()} deve ter no máximo {casasDec} casas decimais.')  
                    continue  
                valor = None if valor == "" else tipo(valor)
                if validos != None and not validos(valor):
                    raise Exception()                                    
                return valor                
            except:
                print(f'O {chave.lower()} informado está inválido. Por favor digite novamente.')
                continue       