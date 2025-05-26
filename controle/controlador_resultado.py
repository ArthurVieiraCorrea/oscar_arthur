from collections import Counter, defaultdict
from entidade.voto import Voto
from entidade.categoria import Categoria
from limite.tela_resultado import TelaResultado

class ControladorResultado:
    def __init__(self, controlador_sistema, controlador_voto):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_voto = controlador_voto
        self.__tela_resultado = TelaResultado()

    def vencedor_categoria(self):
        nome_categoria = self.__tela_resultado.pegar_categoria()

        categorias_votadas = {v.categoria_votada for v in self.__controlador_voto.votos}
        categoria = next((c for c in categorias_votadas if c.nome_categoria.lower() == nome_categoria.lower()), None)
        
        if not categoria:
            self.__tela_resultado.mostrar_erro(f"Nenhum voto registrado para a categoria '{nome_categoria}'.")
            return
            
        votos_categoria = [v.votado for v in self.__controlador_voto.votos if v.categoria_votada == categoria]
        vencedor = Counter(votos_categoria).most_common(1)[0]
        
        resultado = (f"Vencedor da categoria '{categoria.nome_categoria}':\n"
                    f"{vencedor[0]} com {vencedor[1]} voto(s)")
        self.__tela_resultado.mostrar_vencedor_categoria(resultado)

    def top3_filmes_mais_premiados(self):
        todos_votos = [v.votado for v in self.__controlador_voto.listar_votos()]
        
        if not todos_votos:
            self.__tela_resultado.mostrar_erro("Nenhum voto registrado ainda.")
            return
            
        ranking = Counter(todos_votos).most_common(3)
        resultado = "Top 3 Filmes Mais Premiados:\n"
        for i, (filme, votos) in enumerate(ranking, start=1):
            resultado += f"{i}. {filme} - {votos} voto(s)\n"
            
        self.__tela_resultado.mostrar_top3_filmes(resultado.strip())

    def vencedor_nacionalidade(self):
        nacionalidade = self.__tela_resultado.pegar_nacionalidade()
        votos_nacionalidade = defaultdict(int)
        
        for voto in self.__controlador_voto.votos:
            if voto.votante.nacionalidade.lower() == nacionalidade.lower():
                votos_nacionalidade[voto.votado] += 1

        if not votos_nacionalidade:
            self.__tela_resultado.mostrar_erro(f"Nenhum voto registrado por membros da nacionalidade '{nacionalidade}'.")
            return
            
        vencedor = max(votos_nacionalidade.items(), key=lambda x: x[1])
        resultado = (f"concorrente mais votado por membros da nacionalidade '{nacionalidade}':\n"
                    f"{vencedor[0]} com {vencedor[1]} voto(s)")
        self.__tela_resultado.mostrar_vencedor_nacionalidade(resultado)

    def abre_tela(self):
        while True:
            opcao = self.__tela_resultado.mostrar_opcoes()
            
            if opcao == 1:
                self.vencedor_categoria()
            elif opcao == 2:
                self.top3_filmes_mais_premiados()
            elif opcao == 3:
                self.vencedor_nacionalidade()
            elif opcao == 0:
                self.__tela_resultado.mostrar_mensagem("Retornando ao menu principal...")
                break