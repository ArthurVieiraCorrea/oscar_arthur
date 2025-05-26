from datetime import datetime

class TelaMembroAcademia:
    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print("\n--- MENU MEMBROS DA ACADEMIA ---")
        print("1 - Cadastrar Membro")
        print("2 - Editar Membro")
        print("3 - Excluir Membro")
        print("4 - Listar Membros")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 4:
                    return opcao
                print("Opção inválida. Digite um número entre 0 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_dados_membro(self, operacao: str = "cadastro"):
        print(f"\n--- {operacao.upper()} MEMBRO ---")
        dados = {}
        
        dados['nome'] = input("Nome: ").strip()
        while not dados['nome']:
            print("Nome não pode ser vazio!")
            dados['nome'] = input("Nome: ").strip()
            
        dados['id'] = input("ID: ").strip()
        while not dados['id']:
            print("ID não pode ser vazio!")
            dados['id'] = input("ID: ").strip()
            
        dados['nacionalidade'] = input("Nacionalidade: ").strip()
        while not dados['nacionalidade']:
            print("Nacionalidade não pode ser vazia!")
            dados['nacionalidade'] = input("Nacionalidade: ").strip()
            
        while True:
            data_str = input("Data de Nascimento (dd/mm/aaaa): ").strip()
            try:
                dados['data_nascimento'] = datetime.strptime(data_str, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato de data inválido! Use dd/mm/aaaa.")
                
        return dados

    def selecionar_membro_por_id(self):
        id_membro = input("\nDigite o ID do membro: ").strip()
        while not id_membro:
            print("ID não pode ser vazio!")
            id_membro = input("Digite o ID do membro: ").strip()
        return id_membro

    def mostrar_membros(self, membros: list):
        print("\n--- LISTA DE MEMBROS ---")
        if not membros:
            print("Nenhum membro cadastrado.")
        else:
            for membro in membros:
                print(f"ID: {membro.get_id} | Nome: {membro.nome} | Nacionalidade: {membro.nacionalidade} | Nascimento: {membro.data_nascimento.strftime('%d/%m/%Y')}")

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n{mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\nERRO: {mensagem}")