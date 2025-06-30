import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Menu do Sistema', font=("Helvetica", 20), justification='center', size=(30, 1))],
            [sg.Button('1 - Atores', size=(30, 1))],
            [sg.Button('2 - Diretores', size=(30, 1))],
            [sg.Button('3 - Filmes', size=(30, 1))],
            [sg.Button('4 - Membros da Academia', size=(30, 1))],
            [sg.Button('5 - Votação', size=(30, 1))],
            [sg.Button('6 - Categorias', size=(30, 1))],
            [sg.Button('7 - Resultados', size=(30, 1))],
            [sg.Button('0 - Sair', button_color=('white', 'firebrick3'), size=(30, 1))]
        ]

        self.__window = sg.Window('Oscar - Menu Principal', layout, element_justification='c')

    def open(self):
        return self.__window.read()

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)
