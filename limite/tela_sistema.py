class TelaSistema:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Atores")
        print("2 - Diretores")
        print("3 - Filmes")
        print("4 - Membros da Academia")
        print("5 - Votação")
        print("6 - Categorias")
        print("7 - Resultados")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 7:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 7.")
            except ValueError:
                print("Por favor, insira um número válido.")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\nERRO: {mensagem}")

    def pegar_input(self, mensagem: str):
        return input(mensagem).strip()