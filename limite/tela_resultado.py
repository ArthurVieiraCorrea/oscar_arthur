class TelaResultado:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n--- MENU RESULTADOS ---")
        print("1 - Ver vencedor por categoria")
        print("2 - Ver top 3 filmes mais premiados")
        print("3 - Ver vencedor por nacionalidade")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 3.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_categoria(self):
        categoria = input("\nDigite o nome da categoria: ").strip()
        while not categoria:
            print("Nome da categoria não pode ser vazio!")
            categoria = input("Digite o nome da categoria: ").strip()
        return categoria

    def pegar_nacionalidade(self):
        nacionalidade = input("\nDigite a nacionalidade: ").strip()
        while not nacionalidade:
            print("Nacionalidade não pode ser vazia!")
            nacionalidade = input("Digite a nacionalidade: ").strip()
        return nacionalidade

    def mostrar_vencedor_categoria(self, resultado):
        print("\n=== VENCEDOR DA CATEGORIA ===")
        print(resultado)

    def mostrar_top3_filmes(self, resultado):
        print("\n=== TOP 3 FILMES MAIS PREMIADOS ===")
        print(resultado)

    def mostrar_vencedor_nacionalidade(self, resultado):
        print("\n=== VENCEDOR POR NACIONALIDADE ===")
        print(resultado)

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem):
        print(f"\nERRO: {mensagem}")