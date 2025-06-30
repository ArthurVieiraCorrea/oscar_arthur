import PySimpleGUI as sg

class TelaMembroAcademia:
    def __init__(self):
        self.__window = None

    def open(self):
        if self.__window is None:
            self.init_components()
        return self.__window.read()

    def close(self):
        if self.__window:
            self.__window.close()
            self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Gerenciar Membros da Academia', font=("Helvetica", 18), justification='center')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(key='nome')],
            [sg.Text('ID:', size=(15, 1)), sg.InputText(key='id')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText(key='nacionalidade')],
            [sg.Text('Data de Nascimento (dd/mm/aaaa):', size=(25, 1)), sg.InputText(key='data_nascimento')],
            [sg.Button('Cadastrar'), sg.Button('Editar'), sg.Button('Excluir'), sg.Button('Listar')],
            [sg.Button('Voltar', button_color=('white', 'firebrick3'))]
        ]
        self.__window = sg.Window('Membros da Academia', layout)

    def get_campos(self):
        values = self.__window.read(timeout=1)[1]
        return values

    def mostrar_erro(self, mensagem: str):
        sg.popup_error("Erro", mensagem)

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

    def selecionar_membro_por_id(self):
        return sg.popup_get_text("Digite o ID do membro:")

    def mostrar_membros(self, membros: list):
        if not membros:
            self.mostrar_mensagem("Membros", "Nenhum membro cadastrado.")
            return
        texto = ""
        for m in membros:
            texto += f"ID: {m.get_id} | Nome: {m.nome} | Nacionalidade: {m.nacionalidade} | Nasc.: {m.data_nascimento.strftime('%d/%m/%Y')}\n"
        self.mostrar_mensagem("Membros Cadastrados", texto)
