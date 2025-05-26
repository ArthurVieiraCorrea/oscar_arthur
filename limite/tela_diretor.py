class TelaDiretor:
    def opcoes(self):
        print("\n--- MENU DIRETOR ---")
        print("1 - Incluir Diretor")
        print("2 - Editar Diretor")
        print("3 - Ver Diretor")
        print("4 - Excluir Diretor")
        print("0 - Voltar ao Menu Principal")

        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            return -1

    def pegar_dados_cadastro(self):
        print("\n--- CADASTRAR DIRETOR ---")
        nome = input("Nome: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade

    def pegar_nome_diretor(self, mensagem):
        return input(mensagem + " ")

    def pegar_dados_edicao(self):
        print("\n--- EDITAR DIRETOR ---")
        novo_nome = input("Novo nome (deixe em branco para manter): ")
        nova_nacionalidade = input("Nova nacionalidade (deixe em branco para manter): ")
        return novo_nome, nova_nacionalidade

    def mostrar_dados_diretor(self, dados):
        print("\n--- DADOS DO DIRETOR ---")
        print(dados)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

