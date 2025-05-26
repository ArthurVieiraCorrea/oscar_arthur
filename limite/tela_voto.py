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
            
        return dados

    def pegar_nome_votado(self, tipo_item: str):
        return input(f"Nome do {tipo_item} votado: ").strip()

    def confirmar_voto(self, votante, categoria, votado):
        print(f"\nConfirma o voto de {votante.nome} para a categoria '{categoria.nome_categoria}' no item: {votado}?")
        resposta = input("Digite 's' para confirmar ou qualquer outra coisa para cancelar: ").lower().strip()
        return resposta == 's'

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
    
    def mostrar_filmes_disponiveis(self, filmes: list):
        if not filmes:
            print("\nNenhum filme disponível para votação.")
            return

        print("\n--- Filmes Disponíveis ---")
        for filme in filmes:
            diretor_nome = filme.diretor.nome if hasattr(filme.diretor, 'nome') else str(filme.diretor)
            print(f"- {filme.nome} (Ano: {filme.ano}) - Diretor: {diretor_nome}")
        print("-" * 30)

    def mostrar_atores_disponiveis(self, atores: list):
        if not atores:
            print("\nNenhum ator disponível para votação.")
            return

        print("\n--- Atores Disponíveis ---")
        for ator in atores:
            print(f"- {ator.nome} (Nacionalidade: {ator.nacionalidade})")
        print("-" * 30)

    def mostrar_diretores_disponiveis(self, diretores: list):
        if not diretores:
            print("\nNenhum diretor disponível para votação.")
            return

        print("\n--- Diretores Disponíveis ---")
        for diretor in diretores:
            print(f"- {diretor.nome} (Nacionalidade: {diretor.nacionalidade})")
        print("-" * 30)