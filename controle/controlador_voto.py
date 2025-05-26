from entidade.voto import Voto
from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria
from limite.tela_voto import TelaVoto

class ControladorVoto:
    def __init__(self, controlador_sistema, controlador_membro, controlador_categoria):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_membro = controlador_membro
        self.__controlador_categoria = controlador_categoria
        self.__tela_voto = TelaVoto()
        self.__votos = []
        self.__votacao_aberta = True

    @property
    def votos(self):
        """Retorna a lista de todos os votos registrados."""
        return list(self.__votos) 

    def encontrar_voto(self, votante: MembroAcademia, categoria: Categoria):
        for voto in self.__votos:
            if voto.votante == votante and voto.categoria_votada == categoria:
                return voto
        return None

    def registrar_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return
        
        dados = self.__tela_voto.pegar_dados_voto() 
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        if not votante:
            self.__tela_voto.mostrar_erro("Membro não encontrado!")
            return
        
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
        
        votado = None 
        
        nome_categoria_lower = categoria.nome_categoria.lower()

        if nome_categoria_lower == "melhor ator":
            atores_disponiveis = self.__controlador_sistema.controlador_ator.lista_atores
            self.__tela_voto.mostrar_atores_disponiveis(atores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado("ator")
            while not self.__controlador_sistema.controlador_ator.ator_existe(votado):
                self.__tela_voto.mostrar_erro("Ator inválido! Digite novamente.")
                votado = self.__tela_voto.pegar_nome_votado("ator")
        
        elif nome_categoria_lower == "melhor diretor":
            diretores_disponiveis = self.__controlador_sistema.controlador_diretor.lista_diretores
            self.__tela_voto.mostrar_diretores_disponiveis(diretores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado("diretor")
            while not self.__controlador_sistema.controlador_diretor.diretor_existe(votado):
                self.__tela_voto.mostrar_erro("Diretor inválido! Digite novamente.")
                votado = self.__tela_voto.pegar_nome_votado("diretor")
        
        else:
            filmes_disponiveis = self.__controlador_sistema.controlador_filme.lista_filmes
            self.__tela_voto.mostrar_filmes_disponiveis(filmes_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado("filme")
            while not self.__controlador_sistema.controlador_filme.filme_existe(votado):
                self.__tela_voto.mostrar_erro("Filme inválido! Digite novamente.")
                votado = self.__tela_voto.pegar_nome_votado("filme")

        if not votado:
            self.__tela_voto.mostrar_erro("Não foi possível obter o item votado.")
            return

        if not self.__tela_voto.confirmar_voto(votante, categoria, votado):
            self.__tela_voto.mostrar_mensagem("Voto cancelado.")
            return

        novo_voto = Voto(votante, categoria, votado)
        self.__votos.append(novo_voto)
        self.__tela_voto.mostrar_mensagem("Voto registrado com sucesso!")

    def alterar_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        dados = self.__tela_voto.pegar_dados_voto()
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        
        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
            
        voto = self.encontrar_voto(votante, categoria)
        if voto:
            voto.novo_votado = dados['votado'] 
            self.__tela_voto.mostrar_mensagem(
                f"Voto atualizado: {votante.nome} agora votou em {dados['votado']} para '{categoria.nome_categoria}'")
        else:
            self.__tela_voto.mostrar_erro("Voto não encontrado para alteração!")

    def remover_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        dados = self.__tela_voto.pegar_dados_voto()
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        
        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
            
        voto = self.encontrar_voto(votante, categoria)
        if voto:
            self.__votos.remove(voto)
            self.__tela_voto.mostrar_mensagem(
                f"Voto de {votante.nome} para categoria '{categoria.nome_categoria}' foi removido")
        else:
            self.__tela_voto.mostrar_erro("Voto não encontrado para remoção!")

    def finalizar_votacao(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação já está encerrada!")
            return

        if self.__tela_voto.confirmar_finalizacao():
            self.__votacao_aberta = False
            resultados = self.__calcular_resultados()
            self.__tela_voto.mostrar_resultado_votacao(resultados)
            self.__tela_voto.mostrar_mensagem("Votação encerrada com sucesso!")

    def __calcular_resultados(self):
        resultados = {}
        for voto in self.__votos:
            categoria = voto.categoria_votada.nome_categoria
            votado = voto.votado
            
            if categoria not in resultados:
                resultados[categoria] = {}
                
            if votado not in resultados[categoria]:
                resultados[categoria][votado] = 0
                
            resultados[categoria][votado] += 1
            
        return resultados

    def listar_votos(self):
        return self.__votos

    def abre_tela(self):
        while True:
            opcao = self.__tela_voto.mostrar_opcoes()
            
            if opcao == 1:
                self.registrar_voto()
            elif opcao == 2:
                self.alterar_voto()
            elif opcao == 3:
                self.remover_voto()
            elif opcao == 4:
                self.finalizar_votacao()
            elif opcao == 0:
                self.__tela_voto.mostrar_mensagem("Retornando ao menu principal...")
                break
