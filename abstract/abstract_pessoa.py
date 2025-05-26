from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, nacionalidade: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    
    @property
    def nome (self):
        return self.__nome
    
    @nome.setter
    def novo_nome (self, novo_nome:str):
        self.__nome = novo_nome

    @property
    def nacionalidade (self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nova_nacionalidade (self,nova_nacionalidade:str):
        self.__nacionalidade = nova_nacionalidade

    @abstractmethod
    def mostrar_dados (self):
        pass
