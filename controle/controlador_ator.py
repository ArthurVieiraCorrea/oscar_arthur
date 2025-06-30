from entidade.ator import Ator
from limite.tela_ator import TelaAtor
import PySimpleGUI as sg
from DAOs.ator_dao import AtorDAO

class ControladorAtor:
    def __init__(self, tela_ator):
        self.__ator_dao = AtorDAO()
        self.__tela_ator = tela_ator

    @property
    def lista_atores(self):
        return list(self.__ator_dao.get_all())

    def criar_ator(self, nome: str, nacionalidade: str):
        if self.__ator_dao.get(nome):
            self.__tela_ator.show_message("Erro", f"Já existe um ator com o nome '{nome}'.")
            return
        novo_ator = Ator(nome, nacionalidade)
        self.__ator_dao.add(novo_ator)
        self.__tela_ator.show_message("Sucesso", f"Ator '{nome}' criado com sucesso.")

    def excluir_ator(self, nome: str):
        ator_para_excluir = self.__ator_dao.get(nome)

        if ator_para_excluir:
            self.__ator_dao.remove(nome)
            self.__tela_ator.show_message("Sucesso", f"Ator '{nome}' removido com sucesso.")
        else:
            self.__tela_ator.show_message("Erro", f"Ator '{nome}' não encontrado.")

    def editar(self, nome: str, novo_nome: str, nova_nacionalidade: str):
        ator = self.__ator_dao.get(nome)
        if ator:
            if novo_nome and novo_nome.lower() != nome.lower() and self.__ator_dao.get(novo_nome):
                self.__tela_ator.show_message("Erro", f"Já existe um ator com o novo nome '{novo_nome}'. Edição cancelada.")
                return

            if novo_nome and novo_nome.lower() != nome.lower():
                self.__ator_dao.remove(nome)
                ator.nome = novo_nome
                self.__ator_dao.add(ator)
            else:
                if novo_nome:
                    ator.nome = novo_nome
                
            if nova_nacionalidade:
                ator.nacionalidade = nova_nacionalidade
            
            self.__ator_dao.update(ator.nome, ator)
            self.__tela_ator.show_message("Sucesso", f"Dados do ator '{nome}' atualizados.")
            return
        self.__tela_ator.show_message("Erro", f"Ator '{nome}' não encontrado.")


    def get_dados(self, nome: str):
        ator = self.__ator_dao.get(nome)
        if ator:
            return ator.mostrar_dados()
        return f"Erro: Ator '{nome}' não encontrado."

    def ator_existe(self, nome_ator: str) -> bool:
        return self.__ator_dao.get(nome_ator) is not None

    def abre_tela(self):
        while True:
            evento, valores = self.__tela_ator.open()

            match evento:
                case 'Cadastrar':
                    nome = valores.get('nome', '').strip()
                    nacionalidade = valores.get('nacionalidade', '').strip()
                    if nome and nacionalidade:
                        self.criar_ator(nome, nacionalidade)
                    else:
                        self.__tela_ator.show_message("Erro", "Preencha todos os campos.")
                case 'Editar':
                    nome = valores.get('nome', '').strip()
                    if not nome:
                        self.__tela_ator.show_message("Erro", "Digite o nome do ator a ser editado.")
                        continue
                    
                    ator_existente = self.__ator_dao.get(nome)
                    if not ator_existente:
                        self.__tela_ator.show_message("Erro", f"Ator '{nome}' não encontrado para edição.")
                        continue

                    novo_nome = sg.popup_get_text("Novo nome (deixe vazio para manter):", default_text=ator_existente.nome)
                    nova_nacionalidade = sg.popup_get_text("Nova nacionalidade (deixe vazio para manter):", default_text=ator_existente.nacionalidade)
                    self.editar(nome, novo_nome, nova_nacionalidade)
                case 'Listar':
                    if not self.__ator_dao.get_all():
                        self.__tela_ator.show_message("Lista de Atores", "Nenhum ator cadastrado.")
                    else:
                        dados = '\n'.join([a.mostrar_dados() for a in self.__ator_dao.get_all()])
                        self.__tela_ator.show_message("Atores", dados)
                case 'Excluir':
                    nome = valores.get('nome', '').strip()
                    if nome:
                        self.excluir_ator(nome)
                    else:
                        self.__tela_ator.show_message("Erro", "Digite o nome do ator para excluir.")
                case 'Voltar' | sg.WIN_CLOSED:
                    break

        self.__tela_ator.close()
