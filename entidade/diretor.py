from abstract.abstract_pessoa import Pessoa

class Diretor(Pessoa):
    def __init__(self, nome: str, nacionalidade: str):
        super().__init__(nome, nacionalidade)

    def mostrar_dados (self):
        return f"Diretor: {self.nome} - Nacionalidade: {self.nacionalidade}"
