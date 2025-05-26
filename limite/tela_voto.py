class TelaVoto:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n--- MENU VOTAÇÃO ---")
        print("1 - Registrar Voto")
        print("2 - Alterar Voto")
        print("3 - Remover Voto")
        print("4 - Finalizar Votação")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 4:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_dados_voto(self):
        print("\n--- REGISTRAR VOTO ---")
        dados = {}
        
        dados['votante_id'] = input("ID do membro votante: ").strip()
        while not dados['votante_id']:
            print("ID não pode ser vazio!")
            dados['votante_id'] = input("ID do membro votante: ").strip()
            
        dados['categoria_nome'] = input("Nome da categoria: ").strip()
        while not dados['categoria_nome']:
            print("Categoria não pode ser vazia!")
            dados['categoria_nome'] = input("Nome da categoria: ").strip()
            
        dados['votado'] = input("Nome do votado: ").strip()
        while not dados['votado']:
            print("Nome do votado não pode ser vazio!")
            dados['votado'] = input("Nome do votado: ").strip()
            
        return dados

    def confirmar_finalizacao(self):
        resposta = input("\nTem certeza que deseja finalizar a votação? (s/n): ").lower().strip()
        return resposta == 's'

    def mostrar_resultado_votacao(self, resultados):
        print("\n=== RESULTADO DA VOTAÇÃO ===")
        for categoria, votados in resultados.items():
            print(f"\n--- {categoria.upper()} ---")
            for nome, votos in votados.items():
                print(f"{nome}: {votos} voto(s)")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem):
        print(f"\nERRO: {mensagem}")