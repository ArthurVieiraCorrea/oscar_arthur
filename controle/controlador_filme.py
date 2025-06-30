from entidade.filme import Filme
from limite.tela_filme import TelaFilme
import PySimpleGUI as sg
from DAOs.filme_dao import FilmeDAO

class ControladorFilme:
    def __init__(self, controlador_sistema, controlador_categoria, controlador_membro):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_categoria = controlador_categoria
        self.__controlador_membro = controlador_membro
        self.__tela_filme = TelaFilme()
        self.__filme_dao = FilmeDAO()

    @property
    def lista_filmes(self):
        return list(self.__filme_dao.get_all())

    def encontrar_filme_por_nome(self, nome: str):
        return self.__filme_dao.get(nome)

    def filme_existe(self, nome_filme: str) -> bool:
        return self.__filme_dao.get(nome_filme) is not None

    def incluir_filme(self, values):
        nome = values.get('nome', '').strip()
        ano = values.get('ano', '').strip()
        nacionalidade = values.get('nacionalidade', '').strip()
        diretor_nome = values.get('diretor', '').strip()

        if not all([nome, ano, nacionalidade, diretor_nome]):
            self.__tela_filme.show_message("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            ano = int(ano)
        except ValueError:
            self.__tela_filme.show_message("Erro", "Ano deve ser um número inteiro!")
            return

        if self.encontrar_filme_por_nome(nome):
            self.__tela_filme.show_message("Erro", "Já existe um filme com este nome!")
            return

        novo_filme = Filme(nome=nome, ano=ano, nacionalidade=nacionalidade, diretor=diretor_nome)
        self.__filme_dao.add(novo_filme)
        self.__tela_filme.show_message("Sucesso", f"Filme '{nome}' cadastrado com sucesso!")

    def editar_filme(self, values):
        nome_para_editar = self.__tela_filme.get_nome_filme()
        filme = self.encontrar_filme_por_nome(nome_para_editar)
        if not filme:
            self.__tela_filme.show_message("Erro", "Filme não encontrado!")
            return

        novo_nome = sg.popup_get_text(f"Novo nome para '{filme.nome}' (deixe vazio para manter):", default_text=filme.nome)
        novo_ano_str = sg.popup_get_text(f"Novo ano para '{filme.ano}' (deixe vazio para manter):", default_text=str(filme.ano))
        nova_nacionalidade = sg.popup_get_text(f"Nova nacionalidade para '{filme.nacionalidade}' (deixe vazio para manter):", default_text=filme.nacionalidade)
        novo_diretor_nome = sg.popup_get_text(f"Novo diretor para '{filme.diretor}' (deixe vazio para manter):", default_text=filme.diretor)

        if novo_nome and novo_nome != filme.nome:
            if self.encontrar_filme_por_nome(novo_nome):
                self.__tela_filme.show_message("Erro", f"Já existe um filme com o novo nome '{novo_nome}'. Edição cancelada.")
                return
            self.__filme_dao.remove(nome_para_editar)
            filme.novo_nome = novo_nome
            self.__filme_dao.add(filme)
            nome_para_editar = novo_nome # Update key for subsequent updates
        else:
            if novo_nome:
                filme.novo_nome = novo_nome

        if novo_ano_str:
            try:
                novo_ano = int(novo_ano_str)
                filme.novo_ano = novo_ano
            except ValueError:
                self.__tela_filme.show_message("Erro", "Ano deve ser um número inteiro! Ano não atualizado.")

        if nova_nacionalidade:
            filme.nova_nacionalidade = nova_nacionalidade

        if novo_diretor_nome:
            filme.novo_diretor = novo_diretor_nome

        self.__filme_dao.update(filme.nome, filme) 
        self.__tela_filme.show_message("Sucesso", "Filme atualizado com sucesso!")


    def excluir_filme(self):
        nome = self.__tela_filme.get_nome_filme()
        filme = self.encontrar_filme_por_nome(nome)
        if not filme:
            self.__tela_filme.show_message("Erro", "Filme não encontrado!")
            return
        if self.__tela_filme.confirmar_acao(f"Deseja realmente excluir '{filme.nome}'?"):
            self.__filme_dao.remove(nome)
            self.__tela_filme.show_message("Sucesso", "Filme removido com sucesso!")

    def adicionar_indicacao(self):
        nome = self.__tela_filme.get_nome_filme()
        filme = self.encontrar_filme_por_nome(nome)
        if not filme:
            self.__tela_filme.show_message("Erro", "Filme não encontrado para indicação!")
            return

        dados = self.__tela_filme.get_dados_indicacao()
        categoria_nome = dados['categoria']
        membro_id = dados['membro_id']

        categoria = self.__controlador_categoria.pegar_categoria_por_nome(categoria_nome)
        membro = self.__controlador_membro.encontrar_membro_por_id(membro_id)

        if not categoria:
            self.__tela_filme.show_message("Erro", "Categoria não encontrada!")
            return
        if not membro:
            self.__tela_filme.show_message("Erro", "Membro da academia não encontrado!")
            return

        if categoria.nome_categoria.lower() == "melhor filme":
            categoria.adicionar_participante(filme)
            self.__controlador_categoria.categorias.remove(categoria) 
            self.__controlador_categoria.categorias.append(categoria) 

        filme.indicacoes.append((categoria, membro))
        self.__filme_dao.update(filme.nome, filme) 
        self.__tela_filme.show_message("Sucesso", f"Filme '{filme.nome}' indicado na categoria '{categoria.nome_categoria}' com sucesso!")

    def listar_filmes(self):
        filmes = self.__filme_dao.get_all()
        if not filmes:
            self.__tela_filme.show_message("Filmes", "Nenhum filme cadastrado.")
            return
        texto = "\n".join([f"Nome: {f.nome} | Ano: {f.ano} | Nacionalidade: {f.nacionalidade} | Diretor: {f.diretor}" for f in filmes])
        self.__tela_filme.show_message("Filmes Cadastrados", texto)

    def listar_indicacoes(self):
        nome = self.__tela_filme.get_nome_filme()
        filme = self.encontrar_filme_por_nome(nome)
        if not filme:
            self.__tela_filme.show_message("Erro", "Filme não encontrado!")
            return
        if not filme.indicacoes:
            self.__tela_filme.show_message("Indicações", f"Nenhuma indicação cadastrada para '{filme.nome}'.")
            return
        texto = "\n".join([f"Categoria: {cat.nome_categoria} | Indicado por: {m.nome} (ID {m.get_id})" for cat, m in filme.indicacoes])
        self.__tela_filme.show_message(f"Indicações de {filme.nome}", texto)

    def abre_tela(self):
        while True:
            event, values = self.__tela_filme.open()

            if event == 'Cadastrar':
                self.incluir_filme(values)
            elif event == 'Editar':
                self.editar_filme(values)
            elif event == 'Excluir':
                self.excluir_filme()
            elif event == 'Listar':
                self.listar_filmes()
            elif event == 'Indicar':
                self.adicionar_indicacao()
            elif event == 'Ver Indicações':
                self.listar_indicacoes()
            elif event == 'Voltar' or event == sg.WIN_CLOSED:
                break
        self.__tela_filme.close()