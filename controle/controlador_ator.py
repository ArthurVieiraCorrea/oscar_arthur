from entidade.ator import Ator
from limite.tela_ator import TelaAtor

class ControladorAtor:
    def __init__(self, tela_ator):
        self.__lista_atores = []
        self.__tela_ator = tela_ator 

    @property
    def lista_atores(self):
        return list(self.__lista_atores)
    
    def criar_ator(self, nome: str, nacionalidade: str):
        if any(ator.nome.lower() == nome.lower() for ator in self.__lista_atores):
            print(f"Erro: Já existe um ator com o nome '{nome}'.")
            return
        novo_ator = Ator(nome, nacionalidade)
        self.__lista_atores.append(novo_ator)
        print(f"Ator '{nome}' criado com sucesso.")

    def excluir_ator(self, nome: str):
        ator_para_excluir = None
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                ator_para_excluir = ator
                break
        
        if ator_para_excluir:
            self.__lista_atores.remove(ator_para_excluir)
            print(f"Ator '{nome}' removido com sucesso.")
        else:
            print(f"Erro: Ator '{nome}' não encontrado.")

    def editar(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                novo_nome, nova_nacionalidade = self.__tela_ator.pegar_dados_edicao()
                
                if novo_nome: 
                    ator.nome = novo_nome 
                if nova_nacionalidade: 
                    ator.nacionalidade = nova_nacionalidade 
                
                print(f"Dados do ator '{nome}' atualizados com sucesso.")
                return
        print(f"Erro: Ator '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for ator in self.__lista_atores:
            if ator.nome.lower() == nome.lower():
                return ator.mostrar_dados()
        return f"Erro: Ator '{nome}' não encontrado."
    
    def ator_existe(self, nome_ator: str) -> bool:
        """Verifica se um ator com o nome especificado existe."""
        return any(ator.nome.lower() == nome_ator.lower() for ator in self.__lista_atores)

    def abre_tela(self):
        while True:
            opcao = self.__tela_ator.opcoes()

            if opcao == 1:
                nome, nacionalidade = self.__tela_ator.pegar_dados_cadastro() 
                self.criar_ator(nome, nacionalidade)
            elif opcao == 2:
                nome_para_editar = self.__tela_ator.pegar_nome_ator("Digite o nome do ator para editar:") 
                self.editar(nome_para_editar)
            elif opcao == 3:
                nome_para_ver = self.__tela_ator.pegar_nome_ator("Digite o nome do ator para ver:") 
                dados = self.get_dados(nome_para_ver)
                self.__tela_ator.mostrar_dados_ator(dados) 
            elif opcao == 4:
                nome_para_excluir = self.__tela_ator.pegar_nome_ator("Digite o nome do ator para excluir:") 
                self.excluir_ator(nome_para_excluir)
            elif opcao == 0:
                break
            else:
                self.__tela_ator.mostrar_mensagem("Opção inválida.")

