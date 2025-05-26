class Categoria:
    def __init__(self, nome_categoria: str):
        self.__nome_categoria = nome_categoria

    @property
    def nome_categoria(self):
        return self.__nome_categoria

    @nome_categoria.setter
    def nome_categoria(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome_categoria = novo_nome