from entidade.voto import Voto
from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria
from limite.tela_voto import TelaVoto
import PySimpleGUI as sg
from DAOs.voto_dao import VotoDAO
from DAOs.membro_academia_dao import MembroAcademiaDAO
from DAOs.categoria_dao import CategoriaDAO

class ControladorVoto:
    def __init__(self, controlador_sistema, controlador_membro, controlador_categoria):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_membro = controlador_membro
        self.__controlador_categoria = controlador_categoria
        self.__tela_voto = TelaVoto()
        self.__voto_dao = VotoDAO()
        self.__votacao_aberta = True

    @property
    def votos(self):
        return list(self.__voto_dao.get_all())

    def encontrar_voto(self, votante: MembroAcademia, categoria: Categoria):
        key = (votante.get_id, categoria.nome_categoria.lower())
        return self.__voto_dao.get(key)

    def registrar_voto(self, values):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        votante_id = values['votante_id'].strip()
        categoria_nome_input = values['categoria_nome'].strip()

        if not all([votante_id, categoria_nome_input]):
            self.__tela_voto.mostrar_erro("ID do Membro Votante e Nome da Categoria são obrigatórios!")
            return

        votante = self.__controlador_membro.encontrar_membro_por_id(votante_id)
        if not votante:
            self.__tela_voto.mostrar_erro("Membro não encontrado!")
            return

        categoria = self.__controlador_categoria.pegar_categoria_por_nome(categoria_nome_input)
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return

        if self.encontrar_voto(votante, categoria):
            self.__tela_voto.mostrar_erro(f"O membro '{votante.nome}' já votou na categoria '{categoria.nome_categoria}'. Use 'Alterar Voto' para modificar.")
            return

        votado = None
        nome_categoria_lower = categoria.nome_categoria.lower()

        if nome_categoria_lower == "melhor ator":
            atores_disponiveis = self.__controlador_sistema.controlador_ator.lista_atores
            self.__tela_voto.mostrar_atores_disponiveis(atores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("ator")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Voto cancelado. Nome do ator não fornecido.")
                return
            if not self.__controlador_sistema.controlador_ator.ator_existe(votado):
                self.__tela_voto.mostrar_erro("Ator inválido! Verifique o nome.")
                return

        elif nome_categoria_lower == "melhor diretor":
            diretores_disponiveis = self.__controlador_sistema.controlador_diretor.lista_diretores
            self.__tela_voto.mostrar_diretores_disponiveis(diretores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("diretor")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Voto cancelado. Nome do diretor não fornecido.")
                return
            if not self.__controlador_sistema.controlador_diretor.diretor_existe(votado):
                self.__tela_voto.mostrar_erro("Diretor inválido! Verifique o nome.")
                return

        elif nome_categoria_lower == "melhor filme":
            filmes_disponiveis = self.__controlador_sistema.controlador_filme.lista_filmes
            self.__tela_voto.mostrar_filmes_disponiveis(filmes_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("filme")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Voto cancelado. Nome do filme não fornecido.")
                return
            if not self.__controlador_sistema.controlador_filme.filme_existe(votado):
                self.__tela_voto.mostrar_erro("Filme inválido! Verifique o nome.")
                return
        else:
            votado = values['votado_nome'].strip()
            if not votado:
                self.__tela_voto.show_message("Aviso", "Voto cancelado. Nome do item não fornecido.")
                return


        if not votado:
            self.__tela_voto.mostrar_erro("Não foi possível obter o item votado. Verifique a categoria e o nome.")
            return

        if not self.__tela_voto.confirmar_voto(votante.nome, categoria.nome_categoria, votado):
            self.__tela_voto.show_message("Voto", "Voto cancelado.")
            return

        novo_voto = Voto(votante, categoria, votado)
        self.__voto_dao.add((votante.get_id, categoria.nome_categoria.lower()), novo_voto)
        self.__tela_voto.show_message("Sucesso", "Voto registrado com sucesso!")


    def alterar_voto(self, values):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        votante_id = values['votante_id'].strip()
        categoria_nome_input = values['categoria_nome'].strip()

        if not all([votante_id, categoria_nome_input]):
            self.__tela_voto.mostrar_erro("ID do votante e nome da categoria são obrigatórios para alterar voto!")
            return

        votante = self.__controlador_membro.encontrar_membro_por_id(votante_id)
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(categoria_nome_input)

        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return

        voto = self.encontrar_voto(votante, categoria)
        if not voto:
            self.__tela_voto.mostrar_erro("Voto não encontrado para alteração!")
            return

        votado = None
        nome_categoria_lower = categoria.nome_categoria.lower()

        if nome_categoria_lower == "melhor ator":
            atores_disponiveis = self.__controlador_sistema.controlador_ator.lista_atores
            self.__tela_voto.mostrar_atores_disponiveis(atores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("ator")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Alteração de voto cancelada. Nome do ator não fornecido.")
                return
            if not self.__controlador_sistema.controlador_ator.ator_existe(votado):
                self.__tela_voto.mostrar_erro("Ator inválido! Verifique o nome.")
                return

        elif nome_categoria_lower == "melhor diretor":
            diretores_disponiveis = self.__controlador_sistema.controlador_diretor.lista_diretores
            self.__tela_voto.mostrar_diretores_disponiveis(diretores_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("diretor")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Alteração de voto cancelada. Nome do diretor não fornecido.")
                return
            if not self.__controlador_sistema.controlador_diretor.diretor_existe(votado):
                self.__tela_voto.mostrar_erro("Diretor inválido! Verifique o nome.")
                return

        elif nome_categoria_lower == "melhor filme":
            filmes_disponiveis = self.__controlador_sistema.controlador_filme.lista_filmes
            self.__tela_voto.mostrar_filmes_disponiveis(filmes_disponiveis)
            votado = self.__tela_voto.pegar_nome_votado_popup("filme")
            if not votado:
                self.__tela_voto.show_message("Aviso", "Alteração de voto cancelada. Nome do filme não fornecido.")
                return
            if not self.__controlador_sistema.controlador_filme.filme_existe(votado):
                self.__tela_voto.mostrar_erro("Filme inválido! Verifique o nome.")
                return
        else:
            votado = values['votado_nome'].strip()
            if not votado:
                self.__tela_voto.show_message("Aviso", "Alteração de voto cancelada. Nome do item não fornecido.")
                return

        if not votado:
            self.__tela_voto.mostrar_erro("Não foi possível obter o novo item votado.")
            return

        if not self.__tela_voto.confirmar_voto(votante.nome, categoria.nome_categoria, votado):
            self.__tela_voto.show_message("Voto", "Alteração de voto cancelada.")
            return

        voto.votado = votado
        self.__voto_dao.update((votante.get_id, categoria.nome_categoria.lower()), voto)
        self.__tela_voto.show_message("Sucesso", f"Voto atualizado: {votante.nome} agora votou em {votado} para '{categoria.nome_categoria}'")


    def remover_voto(self, values):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        votante_id = values['votante_id'].strip()
        categoria_nome_input = values['categoria_nome'].strip()

        if not all([votante_id, categoria_nome_input]):
            self.__tela_voto.mostrar_erro("ID do votante e nome da categoria são obrigatórios para remover voto!")
            return

        votante = self.__controlador_membro.encontrar_membro_por_id(votante_id)
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(categoria_nome_input)

        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return

        voto = self.encontrar_voto(votante, categoria)
        if voto:
            if sg.popup_yes_no(f"Deseja realmente remover o voto de {votante.nome} para a categoria '{categoria.nome_categoria}'?") == 'Yes':
                self.__voto_dao.remove((votante.get_id, categoria.nome_categoria.lower()))
                self.__tela_voto.show_message("Sucesso", f"Voto de {votante.nome} para categoria '{categoria.nome_categoria}' foi removido.")
            else:
                self.__tela_voto.show_message("Remoção de Voto", "Remoção de voto cancelada.")
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
            self.__tela_voto.show_message("Votação", "Votação encerrada com sucesso!")

    def __calcular_resultados(self):
        resultados = {}
        for voto in self.__voto_dao.get_all():
            categoria_key = voto.categoria_votada.nome_categoria.title()

            votado = voto.votado

            if categoria_key not in resultados:
                resultados[categoria_key] = {}

            if votado not in resultados[categoria_key]:
                resultados[categoria_key][votado] = 0

            resultados[categoria_key][votado] += 1

        return resultados

    def listar_votos(self):
        self.__tela_voto.mostrar_votos_registrados(self.__voto_dao.get_all())

    def abre_tela(self):
        while True:
            event, values = self.__tela_voto.open()

            if event == 'Registrar Voto':
                self.registrar_voto(values)
            elif event == 'Alterar Voto':
                self.alterar_voto(values)
            elif event == 'Remover Voto':
                self.remover_voto(values)
            elif event == 'Finalizar Votação':
                self.finalizar_votacao()
            elif event == '-LISTAR_VOTOS-':
                self.listar_votos()
            elif event == 'Voltar' or event == sg.WIN_CLOSED:
                break

        self.__tela_voto.close()