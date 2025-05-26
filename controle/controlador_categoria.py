from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria()
        self.__categorias = []

    @property
    def categorias(self):
        return self.__categorias

    def pegar_categoria_por_nome(self, nome_categoria: str):
        for categoria in self.__categorias:
            if categoria.nome_categoria.lower() == nome_categoria.lower():
                return categoria
        return None

    def incluir_categoria(self):
        nome = self.__tela_categoria.pegar_nome_categoria("Adicionar")
        if self.pegar_categoria_por_nome(nome) is None:
            nova_categoria = Categoria(nome)
            self.__categorias.append(nova_categoria)
            self.__tela_categoria.mostrar_mensagem(f"Categoria '{nome}' adicionada com sucesso!")
        else:
            self.__tela_categoria.mostrar_erro(f"Categoria '{nome}' já existe!")

    def excluir_categoria(self):
        nome = self.__tela_categoria.pegar_nome_categoria("Remover")
        categoria = self.pegar_categoria_por_nome(nome)
        if categoria:
            self.__categorias.remove(categoria)
            self.__tela_categoria.mostrar_mensagem(f"Categoria '{nome}' removida com sucesso!")
        else:
            self.__tela_categoria.mostrar_erro(f"Categoria '{nome}' não encontrada!")

    def listar_categorias(self):
        self.__tela_categoria.mostrar_categorias(self.__categorias)

    def abre_tela(self):
        while True:
            opcao = self.__tela_categoria.mostrar_opcoes()
            
            if opcao == 1:
                self.incluir_categoria()
            elif opcao == 2:
                self.excluir_categoria()
            elif opcao == 3:
                self.listar_categorias()
            elif opcao == 0:
                self.__tela_categoria.mostrar_mensagem("Retornando ao menu principal...")
                break