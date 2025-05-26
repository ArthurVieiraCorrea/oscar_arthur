from entidade.ator import Ator
from limite.tela_ator import TelaAtor

class ControleAtor:
    def __init__(self, tela_ator):
        self.__lista_atores = []
        self.__tela_ator = tela_ator  

    def criar_ator(self, nome: str, nacionalidade: str):
        if any(ator.nome == nome for ator in self.__lista_atores):
            print(f"Erro: Já existe um ator com o nome '{nome}'.")
            return
        novo_ator = Ator(nome, nacionalidade)
        self.__lista_atores.append(novo_ator)
        print(f"Ator '{nome}' criado com sucesso.")

    def excluir_ator(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome == nome:
                self.__lista_atores.remove(ator)
                print(f"Ator '{nome}' removido com sucesso.")
                return
        print(f"Erro: Ator '{nome}' não encontrado.")

    def editar(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome == nome:
                novo_nome, nova_nacionalidade = self.__tela_ator.pegar_dados_edicao()
                ator.novo_nome = novo_nome
                ator.nova_nacionalidade = nova_nacionalidade
                print(f"Dados do ator '{nome}' atualizados com sucesso.")
                return
        print(f"Erro: Ator '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome == nome:
                return ator.mostrar_dados()
        return f"Erro: Ator '{nome}' não encontrado."
    
    def abre_tela(self):
        while True:
            opcao = self.__tela_ator.opcoes()

            if opcao == 1:
                self.criar_ator()
            elif opcao == 2:
                self.editar_ator()
            elif opcao == 3:
                self.ver_ator()
            elif opcao == 4:
                self.excluir_ator()
            elif opcao == 0:
                break
            else:
                self.__tela_ator.mostrar_mensagem("Opção inválida.")