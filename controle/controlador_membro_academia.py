from entidade.membro_academia import MembroAcademia
from limite.tela_membro_academia import TelaMembroAcademia
from datetime import datetime
import PySimpleGUI as sg
from DAOs.membro_academia_dao import MembroAcademiaDAO

class ControladorMembroAcademia:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_membro = TelaMembroAcademia()
        self.__membro_dao = MembroAcademiaDAO()

    def encontrar_membro_por_id(self, id: str):
        return self.__membro_dao.get(id)

    def incluir_membro(self, valores):
        try:
            data_nascimento = datetime.strptime(valores['data_nascimento'], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_membro.mostrar_erro("Data inválida! Use o formato dd/mm/aaaa.")
            return

        if not all([valores['nome'], valores['id'], valores['nacionalidade']]):
            self.__tela_membro.mostrar_erro("Todos os campos devem ser preenchidos!")
            return

        if self.__membro_dao.get(valores['id']):
            self.__tela_membro.mostrar_erro("Já existe um membro com este ID!")
            return

        novo_membro = MembroAcademia(
            id=valores['id'],
            nome=valores['nome'],
            nacionalidade=valores['nacionalidade'],
            data_nascimento=data_nascimento
        )
        self.__membro_dao.add(novo_membro)
        self.__tela_membro.mostrar_mensagem("Sucesso", "Membro cadastrado com sucesso!")

    def editar_membro(self, values):
        id_membro_para_editar = self.__tela_membro.selecionar_membro_por_id()
        membro = self.__membro_dao.get(id_membro_para_editar)
        if not membro:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")
            return

        novo_nome = sg.popup_get_text(f"Novo nome para '{membro.nome}' (deixe vazio para manter):", default_text=membro.nome)
        nova_nacionalidade = sg.popup_get_text(f"Nova nacionalidade para '{membro.nacionalidade}' (deixe vazio para manter):", default_text=membro.nacionalidade)
        nova_data_nascimento_str = sg.popup_get_text(f"Nova Data de Nascimento (dd/mm/aaaa) para '{membro.data_nascimento.strftime('%d/%m/%Y')}' (deixe vazio para manter):", default_text=membro.data_nascimento.strftime('%d/%m/%Y'))

        if novo_nome:
            membro.nome = novo_nome
        if nova_nacionalidade:
            membro.nacionalidade = nova_nacionalidade

        if nova_data_nascimento_str:
            try:
                nova_data_nascimento = datetime.strptime(nova_data_nascimento_str, "%d/%m/%Y").date()
                membro.data_nascimento = nova_data_nascimento
            except ValueError:
                self.__tela_membro.mostrar_erro("Data inválida! Data de nascimento não atualizada.")
                return

        self.__membro_dao.update(membro)
        self.__tela_membro.mostrar_mensagem("Sucesso", "Membro atualizado com sucesso!")


    def excluir_membro(self):
        id_membro = self.__tela_membro.selecionar_membro_por_id()
        membro = self.__membro_dao.get(id_membro)
        if membro:
            self.__membro_dao.remove(id_membro)
            self.__tela_membro.mostrar_mensagem("Sucesso", "Membro removido com sucesso!")
        else:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")

    def listar_membros(self):
        self.__tela_membro.mostrar_membros(self.__membro_dao.get_all())

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
