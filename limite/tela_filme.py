import PySimpleGUI as sg

class TelaFilme:
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Gerenciar Filmes', font=("Helvetica", 18), justification='center')],
            [sg.Text('Nome:', size=(12, 1)), sg.InputText(key='nome')],
            [sg.Text('Ano:', size=(12, 1)), sg.InputText(key='ano')],
            [sg.Text('Nacionalidade:', size=(12, 1)), sg.InputText(key='nacionalidade')],
            [sg.Text('Diretor:', size=(12, 1)), sg.InputText(key='diretor')],
            [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Listar')],
            [sg.Button('Indicar'), sg.Button('Ver Indicações')],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'))]
        ]

        self.__window = sg.Window('Filmes', layout, element_justification='c')

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

    def confirmar_acao(self, mensagem: str) -> bool:
        return sg.popup_yes_no(mensagem) == 'Yes'

    def get_dados_filme(self):
        pass

    def get_nome_filme(self):
        return sg.popup_get_text("Digite o nome do filme:")

    def get_dados_indicacao(self):
        categoria = sg.popup_get_text("Digite o nome da categoria:")
        membro_id = sg.popup_get_text("Digite o ID do membro da academia:")
        return {'categoria': categoria.strip(), 'membro_id': membro_id.strip()}