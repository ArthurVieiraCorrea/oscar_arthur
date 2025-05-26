from datetime import datetime
from entidade.membro_academia import MembroAcademia
from limite.tela_membro_academia import TelaMembroAcademia

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

    def incluir_membro(self):
        dados = self.__tela_membro.pegar_dados_membro("cadastro")
        
        if self.encontrar_membro_por_id(dados['id']):
            self.__tela_membro.mostrar_erro("Já existe um membro com este ID!")
            return
            
        novo_membro = MembroAcademia(
            id=dados['id'],
            nome=dados['nome'],
            nacionalidade=dados['nacionalidade'],
            data_nascimento=dados['data_nascimento']
        )
        self.__lista_membros.append(novo_membro)
        self.__tela_membro.mostrar_mensagem("Membro cadastrado com sucesso!")

    def editar_membro(self):
        id_membro = self.__tela_membro.selecionar_membro_por_id()
        membro = self.encontrar_membro_por_id(id_membro)
        
        if not membro:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")
            return
            
        novos_dados = self.__tela_membro.pegar_dados_membro("edição")
        
        membro.nome = novos_dados['nome']
        membro.nacionalidade = novos_dados['nacionalidade']
        membro.data_nascimento = novos_dados['data_nascimento']
        
        self.__tela_membro.mostrar_mensagem("Membro atualizado com sucesso!")

    def excluir_membro(self):
        id_membro = self.__tela_membro.selecionar_membro_por_id()
        membro = self.encontrar_membro_por_id(id_membro)
        
        if membro:
            self.__lista_membros.remove(membro)
            self.__tela_membro.mostrar_mensagem("Membro removido com sucesso!")
        else:
            self.__tela_membro.mostrar_erro("Membro não encontrado!")

    def listar_membros(self):
        self.__tela_membro.mostrar_membros(self.__lista_membros)

    def abre_tela(self):
        while True:
            opcao = self.__tela_membro.mostrar_opcoes()
            
            if opcao == 1:
                self.incluir_membro()
            elif opcao == 2:
                self.editar_membro()
            elif opcao == 3:
                self.excluir_membro()
            elif opcao == 4:
                self.listar_membros()
            elif opcao == 0:
                self.__tela_membro.mostrar_mensagem("Retornando ao menu principal...")
                break