from entidade.categoria import Categoria
from entidade.membro_academia import MembroAcademia

class Filme:
    def __init__(self, nome: str, ano: str, nacionalidade: str, diretor: str):
        self.__nome = nome
        self.__ano = ano
        self.__nacionalidade = nacionalidade
        self.__diretor = diretor
        self.__indicacoes = []

    @property
    def nome (self):
        return self.__nome
    
    @nome.setter
    def novo_nome (self, novo_nome: str):
        if isinstance (novo_nome, str):
            self.__nome = novo_nome

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def novo_ano (self,novo_ano):
       if isinstance (novo_ano, int):
        self.__ano = novo_ano

    @property
    def nacionalidade (self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nova_nacionalidade(self, nova_nacionalidade: str):
        if isinstance (nova_nacionalidade, str):
            self.__nacionalidade = nova_nacionalidade

    @property
    def diretor (self):
        return self.__diretor
    
    @diretor.setter
    def novo_diretor (self, novo_diretor: str):
        if isinstance (novo_diretor, str):
            self.__diretor = novo_diretor

    @property
    def indicacoes(self):
        return self.__indicacoes

    @indicacoes.setter
    def indicacoes(self, nova_lista: list):
        if isinstance(nova_lista, list):
            for item in nova_lista:
                if (not isinstance(item, tuple) or len(item) != 2 or
                    not isinstance(item[0], Categoria) or
                    not isinstance(item[1], MembroAcademia)):
                    raise ValueError("Todos os itens devem ser tuplas (Categoria, MembroAcademia).")
            self.__indicacoes = nova_lista
        else:
            raise ValueError("A nova lista de indicações deve ser uma lista de tuplas.")

    def mostrar_dados (self):
        return f"Filme: {self.nome} - Ano: {self.ano} - Nacionalidade: {self.nacionalidade} - Diretor: {self.diretor} - indicações {self.indicacoes} "
