from entidade.diretor import Diretor
from limite.tela_diretor import TelaDiretor

class ControleDiretor:
    def __init__(self, tela_diretor):
        self.__lista_diretores = []
        self.__tela_diretor = tela_diretor  

    def criar_diretor(self, nome: str, nacionalidade: str):
        if any(diretor.nome == nome for diretor in self.__lista_diretores):
            print(f"Erro: Já existe um diretor com o nome '{nome}'.")
            return
        novo_diretor = Diretor(nome, nacionalidade)
        self.__lista_diretores.append(novo_diretor)
        print(f"Diretor '{nome}' criado com sucesso.")

    def excluir_diretor(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome == nome:
                self.__lista_adiretores.remove(diretor)
                print(f"diretor '{nome}' removido com sucesso.")
                return
        print(f"Erro: diretor '{nome}' não encontrado.")

    def editar(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome == nome:
                novo_nome, nova_nacionalidade = self.__tela_diretor.pegar_dados_edicao()
                diretor.novo_nome = novo_nome
                diretor.nova_nacionalidade = nova_nacionalidade
                print(f"Dados do diretor '{nome}' atualizados com sucesso.")
                return
        print(f"Erro: diretor '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome == nome:
                return diretor.mostrar_dados()
        return f"Erro: diretor '{nome}' não encontrado."
    
    def abre_tela(self):
        while True:
            opcao = self.__tela_diretor.opcoes()

            if opcao == 1:
                self.criar_diretor()
            elif opcao == 2:
                self.editar_diretor()
            elif opcao == 3:
                self.ver_diretor()
            elif opcao == 4:
                self.excluir_diretor()
            elif opcao == 0:
                break
            else:
                self.__tela_diretor.mostrar_mensagem("Opção inválida.")