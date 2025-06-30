from DAOs.dao import DAO
from entidade.categoria import Categoria

class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            super().add(categoria.nome_categoria, categoria)
        else:
            raise TypeError("Objeto não é do tipo Categoria")

    def update(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            super().update(categoria.nome_categoria, categoria)
        else:
            raise TypeError("Objeto não é do tipo Categoria")

    def get(self, nome_categoria: str) -> Categoria:
        return super().get(nome_categoria)

    def remove(self, nome_categoria: str):
        super().remove(nome_categoria)
