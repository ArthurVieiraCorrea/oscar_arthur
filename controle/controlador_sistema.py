from controle.controlador_categoria import ControladorCategoria
from controle.controlador_membro_academia import ControladorMembroAcademia
from controle.controlador_filme import ControladorFilme
from controle.controlador_diretor import ControladorDiretor
from controle.controlador_ator import ControladorAtor
from controle.controlador_voto import ControladorVoto
from controle.controlador_resultado import ControladorResultado
from limite.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        # Inicializa controladores principais
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_membro_academia = ControladorMembroAcademia(self)
        self.__controlador_filme = ControladorFilme(self, 
                                                  self.__controlador_categoria,
                                                  self.__controlador_membro_academia)
        self.__controlador_diretor = ControladorDiretor(self)
        self.__controlador_ator = ControladorAtor(self)
        
        # Controladores dependentes (recebem outros controladores)
        self.__controlador_voto = ControladorVoto(self,
                                                self.__controlador_membro_academia,
                                                self.__controlador_categoria)
        
        self.__controlador_resultado = ControladorResultado(self,
                                                          self.__controlador_voto)
        
        self.__tela_sistema = TelaSistema()

    def abre_tela_categoria(self):
        self.__controlador_categoria.abre_tela()

    def abre_tela_membro_academia(self):
        self.__controlador_membro_academia.abre_tela()

    def abre_tela_filme(self):
        self.__controlador_filme.abre_tela()

    def abre_tela_diretor(self):
        self.__controlador_diretor.abre_tela()

    def abre_tela_ator(self):
        self.__controlador_ator.abre_tela()

    def abre_tela_voto(self):
        self.__controlador_voto.abre_tela()

    def abre_tela_resultado(self):
        self.__controlador_resultado.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.mostrar_opcoes()
            
            if opcao == 1:
                self.abre_tela_ator()
            elif opcao == 2:
                self.abre_tela_diretor()
            elif opcao == 3:
                self.abre_tela_filme()
            elif opcao == 4:
                self.abre_tela_membro_academia()
            elif opcao == 5:
                self.abre_tela_voto()
            elif opcao == 6:
                self.abre_tela_categoria()
            elif opcao == 7:
                self.abre_tela_resultado()
            elif opcao == 0:
                self.__tela_sistema.mostrar_mensagem("Encerrando sistema...")
                exit(0)
            else:
                self.__tela_sistema.mostrar_erro("Opção inválida!")