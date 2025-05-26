from entidade.voto import Voto
from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria
from limite.tela_voto import TelaVoto

class ControladorVoto:
    def __init__(self, controlador_sistema, controlador_membro, controlador_categoria):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_membro = controlador_membro
        self.__controlador_categoria = controlador_categoria
        self.__tela_voto = TelaVoto()
        self.__votos = []
        self.__votacao_aberta = True

    def encontrar_voto(self, votante: MembroAcademia, categoria: Categoria):
        for voto in self.__votos:
            if voto.votante == votante and voto.categoria_votada == categoria:
                return voto
        return None

    def registrar_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        dados = self.__tela_voto.pegar_dados_voto()
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        
        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
            
        voto_existente = self.encontrar_voto(votante, categoria)
        if voto_existente:
            self.__tela_voto.mostrar_erro(f"Este membro já votou na categoria {categoria.nome_categoria}!")
            return
            
        novo_voto = Voto(votante, categoria, dados['votado'])
        self.__votos.append(novo_voto)
        self.__tela_voto.mostrar_mensagem(
            f"Voto registrado: {votante.nome} votou em {dados['votado']} para '{categoria.nome_categoria}'")

    def alterar_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        dados = self.__tela_voto.pegar_dados_voto()
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        
        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
            
        voto = self.encontrar_voto(votante, categoria)
        if voto:
            voto.novo_votado = dados['votado']
            self.__tela_voto.mostrar_mensagem(
                f"Voto atualizado: {votante.nome} agora votou em {dados['votado']} para '{categoria.nome_categoria}'")
        else:
            self.__tela_voto.mostrar_erro("Voto não encontrado para alteração!")

    def remover_voto(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação está encerrada!")
            return

        dados = self.__tela_voto.pegar_dados_voto()
        
        votante = self.__controlador_membro.encontrar_membro_por_id(dados['votante_id'])
        categoria = self.__controlador_categoria.pegar_categoria_por_nome(dados['categoria_nome'])
        
        if not votante:
            self.__tela_voto.mostrar_erro("Membro votante não encontrado!")
            return
        if not categoria:
            self.__tela_voto.mostrar_erro("Categoria não encontrada!")
            return
            
        voto = self.encontrar_voto(votante, categoria)
        if voto:
            self.__votos.remove(voto)
            self.__tela_voto.mostrar_mensagem(
                f"Voto de {votante.nome} para categoria '{categoria.nome_categoria}' foi removido")
        else:
            self.__tela_voto.mostrar_erro("Voto não encontrado para remoção!")

    def finalizar_votacao(self):
        if not self.__votacao_aberta:
            self.__tela_voto.mostrar_erro("A votação já está encerrada!")
            return

        if self.__tela_voto.confirmar_finalizacao():
            self.__votacao_aberta = False
            resultados = self.__calcular_resultados()
            self.__tela_voto.mostrar_resultado_votacao(resultados)
            self.__tela_voto.mostrar_mensagem("Votação encerrada com sucesso!")

    def __calcular_resultados(self):
        resultados = {}
        for voto in self.__votos:
            categoria = voto.categoria_votada.nome_categoria
            votado = voto.votado
            
            if categoria not in resultados:
                resultados[categoria] = {}
                
            if votado not in resultados[categoria]:
                resultados[categoria][votado] = 0
                
            resultados[categoria][votado] += 1
            
        return resultados

    def abre_tela(self):
        while True:
            opcao = self.__tela_voto.mostrar_opcoes()
            
            if opcao == 1:
                self.registrar_voto()
            elif opcao == 2:
                self.alterar_voto()
            elif opcao == 3:
                self.remover_voto()
            elif opcao == 4:
                self.finalizar_votacao()
            elif opcao == 0:
                self.__tela_voto.mostrar_mensagem("Retornando ao menu principal...")
                break