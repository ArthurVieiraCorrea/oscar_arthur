from entidade.membro_academia import MembroAcademia
from limite.tela_membro_academia import TelaMembroAcademia
from datetime import datetime
import PySimpleGUI as sg

class ControladorMembroAcademia:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_membro = TelaMembroAcademia()
        self.__lista_membros = []

    def encontrar_membro_por_id(self, id: str):
        for membro in self.__lista_membros:
            if membro.get_id == id:
                return membro
        return None

    def incluir_membro(self, valores):
        try:
            data_nascimento = datetime.strptime(valores['data_nascimento'], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_membro.mostrar_erro("Data inválida! Use o formato dd/mm/aaaa.")
            return

        if not all([valores['nome'], valores['id'], valores['nacionalidade']]):
            self.__tela_membro.mostrar_erro("Todos os campos devem ser preenchidos!")
            return

        if self.encontrar_membro_por_id(valores['id']):
            self.__tela_membro.mostrar_erro("Já existe um membro com este ID!")
            return

        novo_membro = MembroAcademia(
            id=valores['id'],
            nome=valores['nome'],
            nacionalidade=valores['nacionalidade'],
            data_nascimento=data_nascimento
        )
        self.__lista_membros.append(novo_membro)
        self.__tela_membro.mostrar_mensagem("Sucesso", "Membro cadastrado com sucesso!")

    def editar_membro(self, valores):
        id_membro = self.__tela_membro.selecionar_membro_por_id()
        membro = self.encontrar_membro_por_id(id_membro)
        if not membro:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")
            return

        try:
            data_nascimento = datetime.strptime(valores['data_nascimento'], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_membro.mostrar_erro("Data inválida! Use o formato dd/mm/aaaa.")
            return

        membro.nome = valores['nome']
        membro.nacionalidade = valores['nacionalidade']
        membro.data_nascimento = data_nascimento
        self.__tela_membro.mostrar_mensagem("Sucesso", "Membro atualizado com sucesso!")

    def excluir_membro(self):
        id_membro = self.__tela_membro.selecionar_membro_por_id()
        membro = self.encontrar_membro_por_id(id_membro)
        if membro:
            self.__lista_membros.remove(membro)
            self.__tela_membro.mostrar_mensagem("Sucesso", "Membro removido com sucesso!")
        else:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")

    def listar_membros(self):
        self.__tela_membro.mostrar_membros(self.__lista_membros)

    def abre_tela(self):
        while True:
            event, values = self.__tela_membro.open()

            if event == 'Cadastrar':
                self.incluir_membro(values)
            elif event == 'Editar':
                self.editar_membro(values)
            elif event == 'Excluir':
                self.excluir_membro()
            elif event == 'Listar':
                self.listar_membros()
            elif event in (sg.WIN_CLOSED, 'Voltar'):
                break

        self.__tela_membro.close()
