class TelaFilme:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n--- MENU FILMES ---")
        print("1 - Cadastrar Filme")
        print("2 - Editar Filme")
        print("3 - Excluir Filme")
        print("4 - Listar Filmes")
        print("5 - Adicionar Indicação")
        print("6 - Listar Indicações")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 6:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 6.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_dados_filme(self, operacao: str = "cadastro"):
        print(f"\n--- {operacao.upper()} FILME ---")
        dados = {}
        
        dados['nome'] = input("Nome do filme: ").strip()
        while not dados['nome']:
            print("Nome não pode ser vazio!")
            dados['nome'] = input("Nome do filme: ").strip()
            
        while True:
            try:
                dados['ano'] = int(input("Ano de lançamento: "))
                break
            except ValueError:
                print("Ano deve ser um número inteiro!")
                
        dados['nacionalidade'] = input("Nacionalidade: ").strip()
        while not dados['nacionalidade']:
            print("Nacionalidade não pode ser vazia!")
            dados['nacionalidade'] = input("Nacionalidade: ").strip()
            
        dados['diretor'] = input("Diretor: ").strip()
        while not dados['diretor']:
            print("Diretor não pode ser vazio!")
            dados['diretor'] = input("Diretor: ").strip()
            
        return dados

    def selecionar_filme_por_nome(self):
        nome = input("\nDigite o nome do filme: ").strip()
        while not nome:
            print("Nome não pode ser vazio!")
            nome = input("Digite o nome do filme: ").strip()
        return nome

    def pegar_dados_indicacao(self):
        print("\n--- ADICIONAR INDICAÇÃO ---")
        indicacao = {}
        
        indicacao['categoria'] = input("Nome da categoria: ").strip()
        while not indicacao['categoria']:
            print("Categoria não pode ser vazia!")
            indicacao['categoria'] = input("Nome da categoria: ").strip()
            
        indicacao['membro_id'] = input("ID do membro da academia: ").strip()
        while not indicacao['membro_id']:
            print("ID do membro não pode ser vazio!")
            indicacao['membro_id'] = input("ID do membro da academia: ").strip()
            
        return indicacao

    def mostrar_filmes(self, filmes: list):
        print("\n--- LISTA DE FILMES ---")
        if not filmes:
            print("Nenhum filme cadastrado.")
        else:
            for filme in filmes:
                print(f"Nome: {filme.nome} | Ano: {filme.ano} | Nacionalidade: {filme.nacionalidade} | Diretor: {filme.diretor}")

    def mostrar_indicacoes(self, filme):
        print(f"\n--- INDICAÇÕES DO FILME {filme.nome.upper()} ---")
        if not filme.indicacoes:
            print("Nenhuma indicação cadastrada.")
        else:
            for categoria, membro in filme.indicacoes:
                print(f"Categoria: {categoria.nome_categoria} | Indicado por: {membro.nome} (ID: {membro.get_id})")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\nERRO: {mensagem}")

    def confirmar_acao(self, mensagem: str):
        resposta = input(f"{mensagem} (s/n): ").lower().strip()
        return resposta == 's'