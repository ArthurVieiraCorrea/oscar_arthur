from entidade.ator import Ator
from limite.tela_ator import TelaAtor
import PySimpleGUI as sg

class ControladorAtor:
    def __init__(self, tela_ator):
        self.__lista_atores = []
        self.__tela_ator = tela_ator 

    @property
    def lista_atores(self):
        return list(self.__lista_atores)

    def criar_ator(self, nome: str, nacionalidade: str):
        if any(ator.nome.lower() == nome.lower() for ator in self.__lista_atores):
            self.__tela_ator.show_message("Erro", f"Já existe um ator com o nome '{nome}'.")
            return
        novo_ator = Ator(nome, nacionalidade)
        self.__lista_atores.append(novo_ator)
        self.__tela_ator.show_message("Sucesso", f"Ator '{nome}' criado com sucesso.")

    def excluir_ator(self, nome: str):
        ator_para_excluir = None
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                ator_para_excluir = ator
                break
        
        if ator_para_excluir:
            self.__lista_atores.remove(ator_para_excluir)
            self.__tela_ator.show_message("Sucesso", f"Ator '{nome}' removido com sucesso.")
        else:
            self.__tela_ator.show_message("Erro", f"Ator '{nome}' não encontrado.")

    def editar(self, nome: str, novo_nome: str, nova_nacionalidade: str):
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                if novo_nome:
                    ator.nome = novo_nome
                if nova_nacionalidade:
                    ator.nacionalidade = nova_nacionalidade
                self.__tela_ator.show_message("Sucesso", f"Dados do ator '{nome}' atualizados.")
                return
        self.__tela_ator.show_message("Erro", f"Ator '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                return ator.mostrar_dados()
        return f"Erro: Ator '{nome}' não encontrado."

    def ator_existe(self, nome_ator: str) -> bool:
        return any(ator.nome.lower() == nome_ator.lower() for ator in self.__lista_atores)

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
                    novo_nome = sg.popup_get_text("Novo nome (deixe vazio para manter):")
                    nova_nacionalidade = sg.popup_get_text("Nova nacionalidade (deixe vazio para manter):")
                    self.editar(nome, novo_nome, nova_nacionalidade)
                case 'Listar':
                    if not self.__lista_atores:
                        self.__tela_ator.show_message("Lista de Atores", "Nenhum ator cadastrado.")
                    else:
                        dados = '\n'.join([a.mostrar_dados() for a in self.__lista_atores])
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
