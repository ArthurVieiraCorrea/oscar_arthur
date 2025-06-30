from DAOs.dao import DAO
from entidade.filme import Filme

class FilmeDAO(DAO):
    def __init__(self):
        super().__init__('filmes.pkl')

    def add(self, filme: Filme):
        if isinstance(filme, Filme):
            super().add(filme.nome, filme)
        else:
            raise TypeError("Objeto não é do tipo Filme")

    def update(self, filme: Filme):
        if isinstance(filme, Filme):
            super().update(filme.nome, filme)
        else:
            raise TypeError("Objeto não é do tipo Filme")

    def get(self, nome: str) -> Filme:
        return super().get(nome)

    def remove(self, nome: str):
        super().remove(nome)