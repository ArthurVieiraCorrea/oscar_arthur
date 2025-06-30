from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria

class Voto:
    def __init__(self, votante: MembroAcademia, categoria_votada: Categoria, votado: str):
        if not isinstance(votante, MembroAcademia):
            raise TypeError("O votante deve ser um objeto da classe MembroAcademia.")
        if not isinstance(categoria_votada, Categoria):
            raise TypeError("A categoria votada deve ser um objeto da classe Categoria.")
        if not isinstance(votado, str):
            raise TypeError("O votado deve ser uma string com o nome do indicado.")

        self.__votante = votante
        self.__categoria_votada = categoria_votada
        self.__votado = votado

    @property
    def votante(self):
        return self.__votante
    
    @votante.setter
    def novo_votante (self, novo_votante: MembroAcademia):
        if isinstance (novo_votante, MembroAcademia):
            self.__votante = novo_votante

    @property
    def categoria_votada(self):
        return self.__categoria_votada

    @categoria_votada.setter
    def novo_categoria (self, novo_categoria: Categoria):
        if isinstance (novo_categoria, Categoria):
            self.categoria_votada = novo_categoria

    @property
    def votado(self):
        return self.__votado
    
    @votado.setter
    def novo_votado (self, novo_votado: str):
        if isinstance (novo_votado, str):
            self.__votado = novo_votado

    def __repr__(self):
        return (f"Voto(votante={self.votante.nome}, "
                f"categoria='{self.categoria_votada.nome}', "
                f"votado='{self.votado}')")