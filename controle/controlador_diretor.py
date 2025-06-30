from entidade.diretor import Diretor
from limite.tela_diretor import TelaDiretor
import PySimpleGUI as sg

class ControladorDiretor:
    def __init__(self, tela_diretor):
        self.__lista_diretores = []
        self.__tela_diretor = tela_diretor

    @property
    def lista_diretores(self):
        return list(self.__lista_diretores)

    def criar_diretor(self, nome: str, nacionalidade: str):
        if any(diretor.nome.lower() == nome.lower() for diretor in self.__lista_diretores):
            self.__tela_diretor.show_message("Erro", f"Já existe um diretor com o nome '{nome}'.")
            return
        novo_diretor = Diretor(nome, nacionalidade)
        self.__lista_diretores.append(novo_diretor)
        self.__tela_diretor.show_message("Sucesso", f"Diretor '{nome}' criado com sucesso.")

    def excluir_diretor(self, nome: str):
        diretor_para_excluir = None
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                diretor_para_excluir = diretor
                break

        if diretor_para_excluir:
            self.__lista_diretores.remove(diretor_para_excluir)
            self.__tela_diretor.show_message("Sucesso", f"Diretor '{nome}' removido com sucesso.")
        else:
            self.__tela_diretor.show_message("Erro", f"Diretor '{nome}' não encontrado.")

    def editar(self, nome: str, novo_nome: str, nova_nacionalidade: str):
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                if novo_nome:
                    diretor.nome = novo_nome
                if nova_nacionalidade:
                    diretor.nacionalidade = nova_nacionalidade
                self.__tela_diretor.show_message("Sucesso", f"Dados do diretor '{nome}' atualizados com sucesso.")
                return
        self.__tela_diretor.show_message("Erro", f"Diretor '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                return diretor.mostrar_dados()
        return f"Erro: Diretor '{nome}' não encontrado."

    def diretor_existe(self, nome_diretor: str) -> bool:
        return any(diretor.nome.lower() == nome_diretor.lower() for diretor in self.__lista_diretores)

    def encontrar_diretor_por_nome(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                return diretor
        return None

    def abre_tela(self):
        while True:
            evento, valores = self.__tela_diretor.open()

            match evento:
                case 'Cadastrar':
                    nome = valores.get('nome', '').strip()
                    nacionalidade = valores.get('nacionalidade', '').strip()
                    if nome and nacionalidade:
                        self.criar_diretor(nome, nacionalidade)
                    else:
                        self.__tela_diretor.show_message("Erro", "Preencha todos os campos.")
                case 'Editar':
                    nome = valores.get('nome', '').strip()
                    if not nome:
                        self.__tela_diretor.show_message("Erro", "Digite o nome do diretor para editar.")
                        continue
                    novo_nome = sg.popup_get_text("Novo nome (deixe vazio para manter):")
                    nova_nacionalidade = sg.popup_get_text("Nova nacionalidade (deixe vazio para manter):")
                    self.editar(nome, novo_nome, nova_nacionalidade)
                case 'Listar':
                    if not self.__lista_diretores:
                        self.__tela_diretor.show_message("Lista de Diretores", "Nenhum diretor cadastrado.")
                    else:
                        dados = '\n'.join([d.mostrar_dados() for d in self.__lista_diretores])
                        self.__tela_diretor.show_message("Diretores", dados)
                case 'Excluir':
                    nome = valores.get('nome', '').strip()
                    if nome:
                        self.excluir_diretor(nome)
                    else:
                        self.__tela_diretor.show_message("Erro", "Digite o nome do diretor para excluir.")
                case 'Voltar' | sg.WIN_CLOSED:
                    break

        self.__tela_diretor.close()