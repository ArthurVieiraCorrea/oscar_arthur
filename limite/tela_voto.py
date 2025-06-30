import PySimpleGUI as sg

class TelaVoto:
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Gerenciar Votação', font=("Helvetica", 18), justification='center', size=(40, 1))],
            [sg.HorizontalSeparator()],
            [sg.Text('ID do Membro Votante:', size=(20, 1)), sg.InputText(key='votante_id')],
            [sg.Text('Nome da Categoria:', size=(20, 1)), sg.InputText(key='categoria_nome')],
            [sg.HorizontalSeparator()],
            [sg.Button('Registrar Voto', size=(15,1)), sg.Button('Alterar Voto', size=(15,1))],
            [sg.Button('Remover Voto', size=(15,1)), sg.Button('Finalizar Votação', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Listar Votos', size=(20,1), key='-LISTAR_VOTOS-')],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'), size=(20,1))]
        ]

        self.__window = sg.Window('Votação', layout, element_justification='c')

    def open(self):
        if self.__window is None:
            self.init_components()
        event, values = self.__window.read()
        return event, values

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def show_message(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error("Erro", mensagem)

    def confirmar_voto(self, votante_nome: str, categoria_nome: str, votado_nome: str) -> bool:
        return sg.popup_yes_no(f"Confirma o voto de {votante_nome} para a categoria '{categoria_nome}' no item: {votado_nome}?") == 'Yes'

    def confirmar_finalizacao(self) -> bool:
        return sg.popup_yes_no("Tem certeza que deseja finalizar a votação?") == 'Yes'

    def mostrar_resultado_votacao(self, resultados: dict):
        if not resultados:
            self.show_message("Resultados da Votação", "Nenhum voto registrado para exibir resultados.")
            return

        resultado_str = "=== RESULTADO DA VOTAÇÃO ===\n\n"
        for categoria, votados in resultados.items():
            resultado_str += f"--- {categoria.upper()} ---\n"
            for nome, votos in votados.items():
                resultado_str += f"{nome}: {votos} voto(s)\n"
            resultado_str += "\n"

        sg.popup_scrolled("Resultados da Votação", resultado_str, size=(60, 20))

    def mostrar_filmes_disponiveis(self, filmes: list):
        if not filmes:
            self.show_message("Filmes Disponíveis", "Nenhum filme disponível para votação.")
            return
        filmes_str = "\n".join([f"- {f.nome} (Ano: {f.ano}) - Diretor: {f.diretor}" for f in filmes])
        sg.popup_scrolled("Filmes Disponíveis", filmes_str, size=(50,15))

    def mostrar_atores_disponiveis(self, atores: list):
        if not atores:
            self.show_message("Atores Disponíveis", "Nenhum ator disponível para votação.")
            return
        atores_str = "\n".join([f"- {a.nome} (Nacionalidade: {a.nacionalidade})" for a in atores])
        sg.popup_scrolled("Atores Disponíveis", atores_str, size=(50,15))


    def mostrar_diretores_disponiveis(self, diretores: list):
        if not diretores:
            self.show_message("Diretores Disponíveis", "Nenhum diretor disponível para votação.")
            return
        diretores_str = "\n".join([f"- {d.nome} (Nacionalidade: {d.nacionalidade})" for d in diretores])
        sg.popup_scrolled("Diretores Disponíveis", diretores_str, size=(50,15))

    def pegar_nome_votado_popup(self, tipo_item: str):
        return sg.popup_get_text(f"Digite o nome do {tipo_item} votado:")

    def mostrar_votos_registrados(self, votos: list):
        if not votos:
            self.show_message("Votos Registrados", "Nenhum voto registrado ainda.")
            return

        votos_str = "=== VOTOS REGISTRADOS ===\n\n"
        for voto in votos:
            votos_str += f"Votante: {voto.votante.nome} (ID: {voto.votante.get_id})\n"
            votos_str += f"Categoria: {voto.categoria_votada.nome_categoria}\n"
            votos_str += f"Votado: {voto.votado}\n"
            votos_str += "-------------------------\n"

        sg.popup_scrolled("Votos Registrados", votos_str, size=(70, 25))