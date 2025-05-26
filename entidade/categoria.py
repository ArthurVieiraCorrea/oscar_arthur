
class Categoria:
    def __init__(self, nome_categoria: str):
        self.__nome_categoria = nome_categoria
        self.__participantes = [] 
        print(f"DEBUG Categoria: Objeto Categoria '{nome_categoria}' inicializado com __participantes.")

    @property
    def nome_categoria(self):
        return self.__nome_categoria

    @property
    def participantes(self):
        return list(self.__participantes) 

    def adicionar_participante(self, participante):
        """
        Adiciona um participante à categoria, se ainda não estiver presente.
        """
        if participante not in self.__participantes:
            self.__participantes.append(participante)
            # print(f"DEBUG: Adicionado {participante.nome if hasattr(participante, 'nome') else participante} à categoria {self.__nome_categoria}")

    def remover_participante(self, participante):
        """
        Remove um participante da categoria, se estiver presente.
        """
        if participante in self.__participantes:
            self.__participantes.remove(participante)
            # print(f"DEBUG: Removido {participante.nome if hasattr(participante, 'nome') else participante} da categoria {self.__nome_categoria}")

    def __str__(self):
        return f"Categoria: {self.__nome_categoria}"

