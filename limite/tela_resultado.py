import PySimpleGUI as sg

class TelaResultado:
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Resultados do Oscar', font=("Helvetica", 18), justification='center', size=(40, 1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Ver Vencedor por Categoria', size=(30, 2), key='-VENCEDOR_CATEGORIA-')],
            [sg.Text('Nome da Categoria:', size=(20, 1)), sg.InputText(key='categoria_input')],
            [sg.HorizontalSeparator()],
            [sg.Button('Ver Top 3 Filmes Mais Premiados', size=(30, 2), key='-TOP3_FILMES-')],
            [sg.HorizontalSeparator()],
            [sg.Button('Ver Vencedor por Nacionalidade', size=(30, 2), key='-VENCEDOR_NACIONALIDADE-')],
            [sg.Text('Nacionalidade:', size=(20, 1)), sg.InputText(key='nacionalidade_input')],
            [sg.HorizontalSeparator()],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'), size=(20, 1))]
        ]

        self.__window = sg.Window('Resultados', layout, element_justification='c')

    def open(self):
        if self.__window is None:
            self.init_components()
        event, values = self.__window.read()
        return event, values

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error("Erro", mensagem)

    def pegar_categoria(self):
        pass

    def pegar_nacionalidade(self):
        pass

    def mostrar_vencedor_categoria(self, resultado: str):
        sg.popup_scrolled("Vencedor da Categoria", resultado, size=(60, 10))

    def mostrar_top3_filmes(self, resultado: str):
        sg.popup_scrolled("Top 3 Filmes Mais Premiados", resultado, size=(60, 15))

    def mostrar_vencedor_nacionalidade(self, resultado: str):
        sg.popup_scrolled("Vencedor por Nacionalidade", resultado, size=(60, 10))