class TelaAtor:
    def opcoes(self):
        print("\n--- MENU ATOR ---")
        print("1 - Incluir Ator")
        print("2 - Editar Ator")
        print("3 - Ver Ator")
        print("4 - Excluir Ator")
        print("0 - Voltar ao Menu Principal")

        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            return -1

    def pegar_dados_cadastro(self):
        print("\n--- CADASTRAR ATOR ---")
        nome = input("Nome: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade

    def pegar_nome_ator(self, mensagem):
        return input(mensagem + " ")

    def pegar_dados_edicao(self):
        print("\n--- EDITAR ATOR ---")
        novo_nome = input("Novo nome (deixe em branco para manter): ")
        nova_nacionalidade = input("Nova nacionalidade (deixe em branco para manter): ")
        return novo_nome, nova_nacionalidade

    def mostrar_dados_ator(self, dados):
        print("\n--- DADOS DO ATOR ---")
        print(dados)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)