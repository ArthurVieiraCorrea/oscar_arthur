from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
import PySimpleGUI as sg

class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria()
        self.__categorias = []
        self.__inicializar_categorias_fixas()

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

    def incluir_categoria(self, nome: str):
        nomes_fixos_lower = ["melhor ator", "melhor diretor", "melhor filme"]

        if nome.lower() in nomes_fixos_lower:
            self.__tela_categoria.show_error(f"A categoria '{nome}' é fixa e não pode ser adicionada.")
            return

        if self.pegar_categoria_por_nome(nome):
            self.__tela_categoria.show_error(f"A categoria '{nome}' já existe!")
            return

        nova_categoria = Categoria(nome)
        self.__categorias.append(nova_categoria)
        self.__tela_categoria.show_message("Sucesso", f"Categoria '{nome}' adicionada com sucesso!")
        self.listar_categorias(update_ui=True)

    def excluir_categoria(self, nome: str):
        nomes_fixos_lower = ["melhor ator", "melhor diretor", "melhor filme"]

        if nome.lower() in nomes_fixos_lower:
            self.__tela_categoria.show_error(f"A categoria '{nome}' é fixa e não pode ser removida.")
            return

        categoria = self.pegar_categoria_por_nome(nome)
        if categoria:
            self.__categorias.remove(categoria)
            self.__tela_categoria.show_message("Sucesso", f"Categoria '{nome}' removida com sucesso!")
            self.listar_categorias(update_ui=True)
        else:
            self.__tela_categoria.show_error(f"Categoria '{nome}' não encontrada!")

    def listar_categorias(self, update_ui: bool = False):
        categorias_para_exibir = self.get_categories_for_display()
        if update_ui:
            self.__tela_categoria.update_category_list(categorias_para_exibir)

    def abre_tela(self):
        self.listar_categorias(update_ui=True)
        while True:
            event, values = self.__tela_categoria.open(self.get_categories_for_display())

            if event == sg.WIN_CLOSED or event == 'Voltar':
                self.__tela_categoria.close()
                break
            elif event == 'Adicionar Categoria':
                nome_categoria = values['nome_categoria'].strip()
                if nome_categoria:
                    self.incluir_categoria(nome_categoria)
                else:
                    self.__tela_categoria.show_error("O nome da categoria não pode ser vazio.")
            elif event == 'Remover Categoria':
                nome_categoria = values['nome_categoria'].strip()
                if nome_categoria:
                    self.excluir_categoria(nome_categoria)
                else:
                    self.__tela_categoria.show_error("O nome da categoria não pode ser vazio.")
            elif event == '-LIST CATEGORIES-':
                self.listar_categorias(update_ui=True)
            elif event == '-CATEGORY LIST-':
                selected_category_name = values['-CATEGORY LIST-'][0] if values['-CATEGORY LIST-'] else None
                if selected_category_name:
                    selected_category_data = next((cat for cat in self.get_categories_for_display() if cat['nome'] == selected_category_name), None)
                    if selected_category_data:
                        participants_text = "\n".join(selected_category_data['participantes']) if selected_category_data['participantes'] else "Nenhum participante."
                        self.__tela_categoria.update_participants_display(participants_text)

    def get_categories_for_display(self):
        categorias_para_exibir = []
        for categoria in self.__categorias:
            nome_categoria_lower = categoria.nome_categoria.lower()
            participantes = []

            if nome_categoria_lower == "melhor ator":
                try:
                    if hasattr(self.__controlador_sistema, 'controlador_ator') and \
                       hasattr(self.__controlador_sistema.controlador_ator, 'lista_atores'):
                        participantes = [a.nome for a in self.__controlador_sistema.controlador_ator.lista_atores]
                except AttributeError:
                    participantes = ["(Erro ao carregar dados de Ator)"]

            elif nome_categoria_lower == "melhor diretor":
                try:
                    if hasattr(self.__controlador_sistema, 'controlador_diretor') and \
                       hasattr(self.__controlador_sistema.controlador_diretor, 'lista_diretores'):
                        participantes = [d.nome for d in self.__controlador_sistema.controlador_diretor.lista_diretores]
                except AttributeError:
                    participantes = ["(Erro ao carregar dados de Diretor)"]

            else:
                if hasattr(categoria, 'participantes'):
                    participantes = [p.nome for p in categoria.participantes] if categoria.participantes else []

            categorias_para_exibir.append({
                "nome": categoria.nome_categoria,
                "participantes": participantes
            })
        return categorias_para_exibir