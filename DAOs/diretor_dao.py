from DAOs.dao import DAO
from entidade.diretor import Diretor

class DiretorDAO(DAO):
    def __init__(self):
        super().__init__('diretores.pkl')

    def add(self, diretor: Diretor):
        if isinstance(diretor, Diretor):
            super().add(diretor.nome, diretor)
        else:
            raise TypeError("Objeto não é do tipo Diretor")

    def update(self, diretor: Diretor):
        if isinstance(diretor, Diretor):
            super().update(diretor.nome, diretor)
        else:
            raise TypeError("Objeto não é do tipo Diretor")

    def get(self, nome: str) -> Diretor:
        return super().get(nome)

    def remove(self, nome: str):
        super().remove(nome)