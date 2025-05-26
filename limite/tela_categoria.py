class TelaCategoria:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n--- MENU CATEGORIAS ---")
        print("1 - Adicionar Categoria")
        print("2 - Remover Categoria")
        print("3 - Listar Categorias")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 3.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_nome_categoria(self, operacao: str):
        print(f"\n--- {operacao.upper()} CATEGORIA ---")
        nome = input("Nome da categoria: ").strip()
        while not nome:
            print("Nome não pode ser vazio!")
            nome = input("Nome da categoria: ").strip()
        return nome

    def mostrar_categorias(self, categorias: list):
        print("\n--- CATEGORIAS CADASTRADAS ---")
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        else:
            for i, categoria in enumerate(categorias, 1):
                print(f"{i}. {categoria.nome_categoria}")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\nERRO: {mensagem}")