from entidade.filme import Filme
from entidade.categoria import Categoria
from entidade.membro_academia import MembroAcademia
from limite.tela_filme import TelaFilme

class ControladorFilme:
    def __init__(self, controlador_sistema, controlador_categoria, controlador_membro):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_categoria = controlador_categoria
        self.__controlador_membro = controlador_membro
        self.__tela_filme = TelaFilme()
        self.__lista_filmes = []

    @property 
    def lista_filmes(self):
        """Retorna a lista completa de filmes no sistema."""
        return list(self.__lista_filmes) 

    def encontrar_filme_por_nome(self, nome: str):
        for filme in self.__lista_filmes:
            if filme.nome.lower() == nome.lower():
                return filme
        return None

    def incluir_filme(self):
        dados = self.__tela_filme.pegar_dados_filme("cadastro")
        
        if self.encontrar_filme_por_nome(dados['nome']):
            self.__tela_filme.mostrar_erro("Já existe um filme com este nome!")
            return
            
        novo_filme = Filme(
            nome=dados['nome'],
            ano=dados['ano'],
            nacionalidade=dados['nacionalidade'],
            diretor=dados['diretor']
        )
        self.__lista_filmes.append(novo_filme)
        self.__tela_filme.mostrar_mensagem("Filme cadastrado com sucesso!")

    def editar_filme(self):
        nome = self.__tela_filme.selecionar_filme_por_nome()
        filme = self.encontrar_filme_por_nome(nome)
        
        if not filme:
            self.__tela_filme.mostrar_erro("Filme não encontrado!")
            return
            
        novos_dados = self.__tela_filme.pegar_dados_filme("edição")
        
        if novos_dados['nome']:
            filme.nome = novos_dados['nome']
        if novos_dados['ano']:
            filme.ano = novos_dados['ano']
        if novos_dados['nacionalidade']:
            filme.nacionalidade = novos_dados['nacionalidade']
        if novos_dados['diretor']:
            filme.diretor = novos_dados['diretor']
        
        self.__tela_filme.mostrar_mensagem("Filme atualizado com sucesso!")

    def excluir_filme(self):
        nome = self.__tela_filme.selecionar_filme_por_nome()
        filme = self.encontrar_filme_por_nome(nome)
        
        if filme:
            if self.__tela_filme.confirmar_acao(f"Tem certeza que deseja excluir o filme '{filme.nome}'?"):
                self.__lista_filmes.remove(filme)
                self.__tela_filme.mostrar_mensagem("Filme removido com sucesso!")
        else:
            self.__tela_filme.mostrar_erro("Filme não encontrado!")

    def adicionar_indicacao(self):
        nome = self.__tela_filme.selecionar_filme_por_nome()
        filme = self.encontrar_filme_por_nome(nome)
        
        if not filme:
            self.__tela_filme.mostrar_erro("Filme não encontrado!")
            return
            
        dados_indicacao = self.__tela_filme.pegar_dados_indicacao()
        
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados_indicacao['categoria'])
        membro = self.__controlador_membro.encontrar_membro_por_id(dados_indicacao['membro_id'])
        
        if not categoria:
            self.__tela_filme.mostrar_erro("Categoria não encontrada!")
            return
        if not membro:
            self.__tela_filme.mostrar_erro("Membro da academia não encontrado!")
            return
            
        filme.indicacoes.append((categoria, membro))
        self.__tela_filme.mostrar_mensagem("Indicação adicionada com sucesso!")

    def listar_filmes(self):
        self.__tela_filme.mostrar_filmes(self.__lista_filmes)

    def listar_indicacoes(self):
        nome = self.__tela_filme.selecionar_filme_por_nome()
        filme = self.encontrar_filme_por_nome(nome)
        
        if filme:
            self.__tela_filme.mostrar_indicacoes(filme)
        else:
            self.__tela_filme.mostrar_erro("Filme não encontrado!")

    def filme_existe(self, nome_filme: str) -> bool:
        return any(filme.nome.lower() == nome_filme.lower() 
             for filme in self.__lista_filmes)

    def abre_tela(self):
        while True:
            opcao = self.__tela_filme.mostrar_opcoes()
            
            if opcao == 1:
                self.incluir_filme()
            elif opcao == 2:
                self.editar_filme()
            elif opcao == 3:
                self.excluir_filme()
            elif opcao == 4:
                self.listar_filmes()
            elif opcao == 5:
                self.adicionar_indicacao()
            elif opcao == 6:
                self.listar_indicacoes()
            elif opcao == 0:
                self.__tela_filme.mostrar_mensagem("Retornando ao menu principal...")
                break
