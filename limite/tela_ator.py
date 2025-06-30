import PySimpleGUI as sg

class TelaAtor:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Gerenciar Atores', font=("Helvetica", 18), justification='center')],
            [sg.Text('Nome:', size=(12, 1)), sg.InputText(key='nome')],
            [sg.Text('Nacionalidade:', size=(12, 1)), sg.InputText(key='nacionalidade')],
            [sg.Button('Cadastrar'), sg.Button('Listar'), sg.Button('Editar'), sg.Button('Excluir')],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'))]
        ]

        self.__window = sg.Window('Atores', layout)

    def open(self):
        return self.__window.read()

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

    def get_dados_ator(self):
        event, values = self.__window.read()
        return values.get('nome', '').strip(), values.get('nacionalidade', '').strip()
