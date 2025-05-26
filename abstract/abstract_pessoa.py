from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, nacionalidade: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    
    @property
    def nome (self):
        return self.__nome
    
    @nome.setter 
    def nome (self, novo_nome:str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome não pode ser vazio e deve ser uma string.")
        self.__nome = novo_nome

    @property
    def nacionalidade (self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade (self, nova_nacionalidade:str):
        if not isinstance(nova_nacionalidade, str) or not nova_nacionalidade.strip():
            raise ValueError("Nacionalidade não pode ser vazia e deve ser uma string.")
        self.__nacionalidade = nova_nacionalidade

    @abstractmethod
    def mostrar_dados (self):
        pass

