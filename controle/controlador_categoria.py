from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        print("DEBUG: Iniciando ControladorCategoria.__init__")
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria()
        self.__categorias = []
        self.__inicializar_categorias_fixas()
        print("DEBUG: ControladorCategoria.__init__ concluído.")

    @property
    def categorias(self):
        return self.__categorias

    def pegar_categoria_por_nome(self, nome_categoria: str):
        for categoria in self.__categorias:
            if categoria.nome_categoria.lower() == nome_categoria.lower():
                return categoria
        return None
    
    def __inicializar_categorias_fixas(self):
        nomes_fixos = ["Melhor Ator", "Melhor Diretor", "Melhor Filme"]
        for nome in nomes_fixos:
            if not self.pegar_categoria_por_nome(nome):
                self.__categorias.append(Categoria(nome))
        print("Categorias fixas inicializadas: Melhor Ator, Melhor Diretor, Melhor Filme.")

    def incluir_categoria(self):
        nome = self.__tela_categoria.pegar_nome_categoria("Adicionar")
        nomes_fixos_lower = ["melhor ator", "melhor diretor", "melhor filme"]
        
        if nome.lower() in nomes_fixos_lower:
            self.__tela_categoria.mostrar_erro(f"A categoria '{nome}' é uma categoria fixa e não pode ser adicionada manualmente.")
            return

        if self.pegar_categoria_por_nome(nome) is None:
            nova_categoria = Categoria(nome)
            self.__categorias.append(nova_categoria)
            self.__tela_categoria.mostrar_mensagem(f"Categoria '{nome}' adicionada com sucesso!")
        else:
            self.__tela_categoria.mostrar_erro(f"Categoria '{nome}' já existe!")

    def excluir_categoria(self):
        nome = self.__tela_categoria.pegar_nome_categoria("Remover")
        nomes_fixos_lower = ["melhor ator", "melhor diretor", "melhor filme"]

        if nome.lower() in nomes_fixos_lower:
            self.__tela_categoria.mostrar_erro(f"A categoria '{nome}' é uma categoria fixa e não pode ser removida.")
            return
            
        categoria = self.pegar_categoria_por_nome(nome)
        if categoria:
            self.__categorias.remove(categoria)
            self.__tela_categoria.mostrar_mensagem(f"Categoria '{nome}' removida com sucesso!")
        else:
            self.__tela_categoria.mostrar_erro(f"Categoria '{nome}' não encontrada!")

    def listar_categorias(self):
        categorias_para_exibir = []
        for categoria in self.__categorias:
            nome_categoria_lower = categoria.nome_categoria.lower()
            
            if nome_categoria_lower == "melhor ator":        
                try:
                    atores = self.__controlador_sistema.controlador_ator.lista_atores
                    categorias_para_exibir.append({
                        "nome": categoria.nome_categoria,
                        "participantes": atores 
                    })
                    
                except AttributeError as e:
                    
                    categorias_para_exibir.append({
                        "nome": categoria.nome_categoria,
                        "participantes": ["(Erro ao carregar dados de Ator)"]
                    })
            elif nome_categoria_lower == "melhor diretor":
                
                try:
                    
                    diretores = self.__controlador_sistema.controlador_diretor.lista_diretores
                    categorias_para_exibir.append({
                        "nome": categoria.nome_categoria,
                        "participantes": diretores
                    })
                    
                except AttributeError as e:
                    
                    categorias_para_exibir.append({
                        "nome": categoria.nome_categoria,
                        "participantes": ["(Erro ao carregar dados de Diretor)"]
                    })
            else:
                
                categorias_para_exibir.append({
                    "nome": categoria.nome_categoria,
                    "participantes": categoria.participantes
                })
        
        self.__tela_categoria.mostrar_categorias(categorias_para_exibir)
        

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

