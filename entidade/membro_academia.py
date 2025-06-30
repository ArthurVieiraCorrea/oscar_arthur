from datetime import date
from abstract.abstract_pessoa import Pessoa

class MembroAcademia(Pessoa):
    def __init__(self, id: str, nome: str, data_nascimento: date, nacionalidade: str):
        super().__init__(nome, nacionalidade)
        self.__id = id
        self.__data_nascimento = data_nascimento

    @property
    def get_id(self):
        return self.__id

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self.__data_nascimento = nova_data_nascimento

    def mostrar_dados(self):
        return f"Membro: {self.nome} - ID: {self.get_id} - Nacionalidade: {self.nacionalidade} - Data de nascimento: {self.data_nascimento}"
