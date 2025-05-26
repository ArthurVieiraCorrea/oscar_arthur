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
    
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\nERRO: {mensagem}")

    def mostrar_categorias(self, categorias_para_exibir: list):
        if not categorias_para_exibir:
            print("\nNenhuma categoria cadastrada.")
            return

        print("\n--- Listagem de Categorias ---")
        for categoria_info in categorias_para_exibir:
            print(f"Categoria: {categoria_info['nome']}")
            if categoria_info['participantes']:
                print("  Participantes:")
                for participante in categoria_info['participantes']:
                    nome_participante = getattr(participante, 'nome', str(participante))
                    print(f"    - {nome_participante}")
            else:
                print("  Nenhum participante nesta categoria.")
            print("-" * 30)