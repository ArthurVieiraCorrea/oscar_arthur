from DAOs.dao import DAO
from entidade.ator import Ator

class AtorDAO(DAO):
    def __init__(self):
        super().__init__('atores.pkl')

    def add(self, ator: Ator):
        if isinstance(ator, Ator):
            super().add(ator.nome, ator)
        else:
            raise TypeError("Objeto não é do tipo Ator")

    def update(self, ator: Ator):
        if isinstance(ator, Ator):
            super().update(ator.nome, ator)
        else:
            raise TypeError("Objeto não é do tipo Ator")

    def get(self, nome: str) -> Ator:
        return super().get(nome)

    def remove(self, nome: str):
        super().remove(nome)