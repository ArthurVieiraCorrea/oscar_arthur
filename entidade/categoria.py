class Categoria:
    def __init__(self, nome_categoria: str):
        self.__nome_categoria = nome_categoria
        self.__participantes = [] 

    @property
    def nome_categoria(self):
        return self.__nome_categoria

    @property
    def participantes(self):
        return list(self.__participantes) 

    def adicionar_participante(self, participante):
        if participante not in self.__participantes:
            self.__participantes.append(participante)

    def remover_participante(self, participante):
        if participante in self.__participantes:
            self.__participantes.remove(participante)

    def __str__(self):
        return f"Categoria: {self.__nome_categoria}"

