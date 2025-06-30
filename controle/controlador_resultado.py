from collections import Counter, defaultdict
from entidade.voto import Voto
from entidade.categoria import Categoria
from limite.tela_resultado import TelaResultado
import PySimpleGUI as sg
from DAOs.voto_dao import VotoDAO

class ControladorResultado:
    def __init__(self, controlador_sistema, controlador_voto):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_voto = controlador_voto
        self.__tela_resultado = TelaResultado()

    def vencedor_categoria(self, categoria_nome_input: str):
        nome_categoria = categoria_nome_input.strip()
        if not nome_categoria:
            self.__tela_resultado.mostrar_erro("O nome da categoria não pode ser vazio!")
            return

        categorias_votadas = {v.categoria_votada for v in self.__controlador_voto.votos}
        categoria = next((c for c in categorias_votadas if c.nome_categoria.lower() == nome_categoria.lower()), None)

        if not categoria:
            self.__tela_resultado.mostrar_erro(f"Nenhum voto registrado para a categoria '{nome_categoria}'.")
            return

        votos_categoria = [v.votado for v in self.__controlador_voto.votos if v.categoria_votada == categoria]

        if not votos_categoria:
            self.__tela_resultado.mostrar_erro(f"Nenhum voto registrado para a categoria '{nome_categoria}'.")
            return

        vencedor_info = Counter(votos_categoria).most_common(1)

        if not vencedor_info:
            self.__tela_resultado.mostrar_erro(f"Não foi possível determinar o vencedor para a categoria '{nome_categoria}'.")
            return

        vencedor_nome, vencedor_votos = vencedor_info[0]

        resultado = (f"Vencedor da categoria '{categoria.nome_categoria}':\n"
                    f"{vencedor_nome} com {vencedor_votos} voto(s)")
        self.__tela_resultado.mostrar_vencedor_categoria(resultado)

    def top3_filmes_mais_premiados(self):
        filme_votos = [v.votado for v in self.__controlador_voto.listar_votos()
                       if v.categoria_votada.nome_categoria.lower() == "melhor filme"]

        if not filme_votos:
            self.__tela_resultado.mostrar_erro("Nenhum voto registrado para filmes ainda.")
            return

        ranking = Counter(filme_votos).most_common(3)
        if not ranking:
            self.__tela_resultado.mostrar_erro("Não foi possível determinar o top 3 filmes.")
            return

        resultado_str = "Top 3 Filmes Mais Premiados:\n"
        for i, (filme, votos) in enumerate(ranking, start=1):
            resultado_str += f"{i}. {filme} - {votos} voto(s)\n"

        self.__tela_resultado.mostrar_top3_filmes(resultado_str.strip())

    def vencedor_nacionalidade(self, nacionalidade_input: str):
        nacionalidade = nacionalidade_input.strip()
        if not nacionalidade:
            self.__tela_resultado.mostrar_erro("A nacionalidade não pode ser vazia!")
            return

        votos_nacionalidade = defaultdict(int)

        for voto in self.__controlador_voto.votos:
            if voto.votante.nacionalidade.lower() == nacionalidade.lower():
                votos_nacionalidade[voto.votado] += 1

        if not votos_nacionalidade:
            self.__tela_resultado.mostrar_erro(f"Nenhum voto registrado por membros da nacionalidade '{nacionalidade}'.")
            return

        vencedor_nome, vencedor_votos = max(votos_nacionalidade.items(), key=lambda x: x[1])
        resultado = (f"Concorrente mais votado por membros da nacionalidade '{nacionalidade}':\n"
                    f"{vencedor_nome} com {vencedor_votos} voto(s)")
        self.__tela_resultado.mostrar_vencedor_nacionalidade(resultado)

    def abre_tela(self):
        while True:
            event, values = self.__tela_resultado.open()

            if event == '-VENCEDOR_CATEGORIA-':
                self.vencedor_categoria(values['categoria_input'])
            elif event == '-TOP3_FILMES-':
                self.top3_filmes_mais_premiados()
            elif event == '-VENCEDOR_NACIONALIDADE-':
                self.vencedor_nacionalidade(values['nacionalidade_input'])
            elif event == 'Voltar' or event == sg.WIN_CLOSED:
                self.__tela_resultado.mostrar_mensagem("Retornando ao menu principal...", "")
                break

        self.__tela_resultado.close()