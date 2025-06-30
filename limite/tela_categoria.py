import PySimpleGUI as sg

class TelaCategoria:
    def __init__(self):
        self.__window = None

    def init_components(self, categorias_para_exibir: list = None):
        sg.ChangeLookAndFeel('Reddit')

        category_list_column = [
            [sg.Text('Categorias Cadastradas', font=("Helvetica", 14), justification='center')],
            [sg.Listbox(values=[cat['nome'] for cat in categorias_para_exibir] if categorias_para_exibir else [],
                        size=(40, 10), enable_events=True, key='-CATEGORY LIST-')],
            [sg.Text('Participantes:', font=("Helvetica", 12))],
            [sg.Multiline(size=(40, 5), key='-PARTICIPANTS DISPLAY-', disabled=True, background_color='lightgray')]
        ]

        layout = [
            [sg.Text('Gerenciar Categorias', font=("Helvetica", 20), justification='center', size=(40, 1))],
            [sg.HorizontalSeparator()],
            [sg.Text('Nome da Categoria:', size=(18, 1)), sg.InputText(key='nome_categoria')],
            [sg.Button('Adicionar Categoria', size=(20, 1)), sg.Button('Remover Categoria', size=(20, 1))],
            [sg.HorizontalSeparator()],
            [sg.Column(category_list_column)],
            [sg.Button('Listar Categorias', size=(40, 1), key='-LIST CATEGORIES-')],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'), size=(40, 1))]
        ]

        self.__window = sg.Window('Categorias', layout, element_justification='c', resizable=True)

    def open(self, categorias_para_exibir: list = None):
        if self.__window is None:
            self.init_components(categorias_para_exibir)
        event, values = self.__window.read()
        return event, values

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def show_message(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

    def show_error(self, mensagem: str):
        sg.popup_error("Erro", mensagem)

    def get_nome_categoria(self):
        pass

    def update_category_list(self, categorias_para_exibir: list):
        if self.__window:
            self.__window['-CATEGORY LIST-'].update(values=[cat['nome'] for cat in categorias_para_exibir])

    def update_participants_display(self, participants_text: str):
        if self.__window:
            self.__window['-PARTICIPANTS DISPLAY-'].update(participants_text)