from entidade.diretor import Diretor
from limite.tela_diretor import TelaDiretor

class ControladorDiretor:
    def __init__(self, tela_diretor):
        self.__lista_diretores = []
        self.__tela_diretor = tela_diretor 

    @property
    def lista_diretores(self):
        return list(self.__lista_diretores) 
    
    def criar_diretor(self, nome: str, nacionalidade: str):
        if any(diretor.nome.lower() == nome.lower() for diretor in self.__lista_diretores):
            print(f"Erro: Já existe um diretor com o nome '{nome}'.")
            return
        novo_diretor = Diretor(nome, nacionalidade) 
        self.__lista_diretores.append(novo_diretor)
        print(f"Diretor '{nome}' criado com sucesso.")

    def excluir_diretor(self, nome: str):
        diretor_para_excluir = None
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                diretor_para_excluir = diretor
                break
        
        if diretor_para_excluir:
            self.__lista_diretores.remove(diretor_para_excluir)
            print(f"Diretor '{nome}' removido com sucesso.")
        else:
            print(f"Erro: Diretor '{nome}' não encontrado.")

    def editar(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():
                novo_nome, nova_nacionalidade = self.__tela_diretor.pegar_dados_edicao()
                
                if novo_nome: 
                    diretor.nome = novo_nome 
                if nova_nacionalidade: 
                    diretor.nacionalidade = nova_nacionalidade 
                
                print(f"Dados do diretor '{nome}' atualizados com sucesso.")
                return
        print(f"Erro: Diretor '{nome}' não encontrado.")

    def get_dados(self, nome: str):
        for diretor in self.__lista_diretores:
            if diretor.nome.lower() == nome.lower():

                return diretor.mostrar_dados()
        return f"Erro: Diretor '{nome}' não encontrado."
    
    def abre_tela(self):
        while True:
            opcao = self.__tela_diretor.opcoes()

            if opcao == 1:
                nome, nacionalidade = self.__tela_diretor.pegar_dados_cadastro() 
                self.criar_diretor(nome, nacionalidade)
            elif opcao == 2:
                nome_para_editar = self.__tela_diretor.pegar_nome_diretor("Digite o nome do diretor para editar:") 
                self.editar(nome_para_editar)
            elif opcao == 3:
                nome_para_ver = self.__tela_diretor.pegar_nome_diretor("Digite o nome do diretor para ver:") 
                dados = self.get_dados(nome_para_ver)
                self.__tela_diretor.mostrar_dados_diretor(dados) 
            elif opcao == 4:
                nome_para_excluir = self.__tela_diretor.pegar_nome_diretor("Digite o nome do diretor para excluir:") 
                self.excluir_diretor(nome_para_excluir)
            elif opcao == 0:
                break
            else:
                self.__tela_diretor.mostrar_mensagem("Opção inválida.")

