from entidade.membro_academia import MembroAcademia
from limite.tela_membro_academia import TelaMembroAcademia
from datetime import datetime

class ControladorMembroAcademia:
    def __init__(self):
        self.lista_membros = []
        self.tela_membro = TelaMembroAcademia()

    def get_dados(self, membro_academia: MembroAcademia):
        return membro_academia.mostrar_dados()

    def editar(self, membro_academia: MembroAcademia):
        novos_dados = self.tela_membro.pegar_dados_membro()

        if 'nome' in novos_dados:
            membro_academia.novo_nome = novos_dados['nome']
        if 'nacionalidade' in novos_dados:
            membro_academia.nova_nacionalidade = novos_dados['nacionalidade']
        if 'data_nascimento' in novos_dados:
            try:
                data_nasc = datetime.strptime(novos_dados['data_nascimento'], "%d/%m/%Y").date()
                membro_academia.nova_data_nascimento = data_nasc
            except ValueError:
                self.tela_membro.mostrar_mensagem("Data inválida. Use o formato dd/mm/aaaa.")

    def incluir(self, nome: str, nacionalidade: str, id: str, data_nascimento: str):
        try:
            data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            novo_membro = MembroAcademia(id=id, nome=nome, nacionalidade=nacionalidade, data_nascimento=data_nasc)
            self.lista_membros.append(novo_membro)
            self.tela_membro.mostrar_mensagem("Membro da academia incluído com sucesso.")
        except ValueError:
            self.tela_membro.mostrar_mensagem("Erro ao converter data. Use o formato dd/mm/aaaa.")

    def excluir(self, id: str):
        for membro in self.lista_membros:
            if membro.get_id == id:
                self.lista_membros.remove(membro)
                self.tela_membro.mostrar_mensagem("Membro removido com sucesso.")
                return
        self.tela_membro.mostrar_mensagem("Membro não encontrado.")