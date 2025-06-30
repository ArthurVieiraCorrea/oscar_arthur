from entidade.diretor import Diretor
from limite.tela_diretor import TelaDiretor
import PySimpleGUI as sg
from DAOs.diretor_dao import DiretorDAO

class ControladorDiretor:
    def __init__(self, tela_diretor):
        self.__diretor_dao = DiretorDAO()
        self.__tela_diretor = tela_diretor

    @property
    def lista_diretores(self):
        return list(self.__diretor_dao.get_all())

    def criar_diretor(self, nome: str, nacionalidade: str):
        if self.__diretor_dao.get(nome):
            self.__tela_diretor.show_message("Erro", f"Já existe um diretor com o nome '{nome}'.")
            return
        novo_diretor = Diretor(nome, nacionalidade)
        self.__diretor_dao.add(novo_diretor)
        self.__tela_diretor.show_message("Sucesso", f"Diretor '{nome}' criado com sucesso.")

    def excluir_diretor(self, nome: str):
        diretor_para_excluir = self.__diretor_dao.get(nome)

        if diretor_para_excluir:
            self.__diretor_dao.remove(nome)
            self.__tela_diretor.show_message("Sucesso", f"Diretor '{nome}' removido com sucesso.")
        else:
            self.__tela_diretor.show_message("Erro", f"Diretor '{nome}' não encontrado.")

    def editar(self, nome: str, novo_nome: str, nova_nacionalidade: str):
        diretor = self.__diretor_dao.get(nome)
        if diretor:
            if novo_nome and novo_nome.lower() != nome.lower() and self.__diretor_dao.get(novo_nome):
                self.__tela_diretor.show_message("Erro", f"Já existe um diretor com o novo nome '{novo_nome}'. Edição cancelada.")
                return

            if novo_nome and novo_nome.lower() != nome.lower():
                self.__diretor_dao.remove(nome)
                diretor.nome = novo_nome
                self.__diretor_dao.add(diretor)
            else:
                if novo_nome:
                    diretor.nome = novo_nome
                
            if nova_nacionalidade:
                diretor.nacionalidade = nova_nacionalidade
            
            self.__diretor_dao.update(diretor.nome, diretor)
            self.__tela_diretor.show_message("Sucesso", f"Dados do diretor '{nome}' atualizados com sucesso.")
            return
        self.__tela_diretor.show_message("Erro", f"Diretor '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        diretor = self.__diretor_dao.get(nome)
        if diretor:
            return diretor.mostrar_dados()
        return f"Erro: Diretor '{nome}' não encontrado."

    def diretor_existe(self, nome_diretor: str) -> bool:
        return self.__diretor_dao.get(nome_diretor) is not None

    def encontrar_diretor_por_nome(self, nome: str):
        return self.__diretor_dao.get(nome)

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
                    
                    diretor_existente = self.__diretor_dao.get(nome)
                    if not diretor_existente:
                        self.__tela_diretor.show_message("Erro", f"Diretor '{nome}' não encontrado para edição.")
                        continue

                    novo_nome = sg.popup_get_text("Novo nome (deixe vazio para manter):", default_text=diretor_existente.nome)
                    nova_nacionalidade = sg.popup_get_text("Nova nacionalidade (deixe vazio para manter):", default_text=diretor_existente.nacionalidade)
                    self.editar(nome, novo_nome, nova_nacionalidade)
                case 'Listar':
                    if not self.__diretor_dao.get_all():
                        self.__tela_diretor.show_message("Lista de Diretores", "Nenhum diretor cadastrado.")
                    else:
                        dados = '\n'.join([d.mostrar_dados() for d in self.__diretor_dao.get_all()])
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