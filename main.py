from controle.controlador_sistema import ControladorSistema
from entidade.ator import Ator
from entidade.diretor import Diretor
from entidade.filme import Filme
from entidade.membro_academia import MembroAcademia
from DAOs.ator_dao import AtorDAO
from DAOs.diretor_dao import DiretorDAO
from DAOs.filme_dao import FilmeDAO
from DAOs.membro_academia_dao import MembroAcademiaDAO
from datetime import date 

def inicializar_dados_exemplo():
    print("Inicializando dados de exemplo...")

    ator_dao = AtorDAO()
    diretor_dao = DiretorDAO()
    filme_dao = FilmeDAO()
    membro_dao = MembroAcademiaDAO()

    # --- Atores ---
    ator1 = Ator("Tom Hanks", "Americano")
    ator2 = Ator("Meryl Streep", "Americana")
    ator3 = Ator("Brad Pitt", "Americano")
    ator4 = Ator("Viola Davis", "Americana")

    if not ator_dao.get(ator1.nome):
        ator_dao.add(ator1)
    if not ator_dao.get(ator2.nome):
        ator_dao.add(ator2)
    if not ator_dao.get(ator3.nome):
        ator_dao.add(ator3)
    if not ator_dao.get(ator4.nome):
        ator_dao.add(ator4)
    print(f"Atores salvos: {len(ator_dao.get_all())}")

    # --- Diretores ---
    diretor1 = Diretor("Steven Spielberg", "Americano")
    diretor2 = Diretor("Greta Gerwig", "Americana")
    diretor3 = Diretor("Quentin Tarantino", "Americano")

    if not diretor_dao.get(diretor1.nome):
        diretor_dao.add(diretor1)
    if not diretor_dao.get(diretor2.nome):
        diretor_dao.add(diretor2)
    if not diretor_dao.get(diretor3.nome):
        diretor_dao.add(diretor3)
    print(f"Diretores salvos: {len(diretor_dao.get_all())}")

    # --- Membros da Academia ---
    membro1 = MembroAcademia("1", "Ana Silva", "Brasil", date(1980, 5, 15))
    membro2 = MembroAcademia("2", "Carlos Souza", "Portugal", date(1975, 11, 22))
    membro3 = MembroAcademia("3", "Beatriz Costa", "Brasil", date(1990, 3, 10))

    if not membro_dao.get(membro1.get_id):
        membro_dao.add(membro1)
    if not membro_dao.get(membro2.get_id):
        membro_dao.add(membro2)
    if not membro_dao.get(membro3.get_id):
        membro_dao.add(membro3)
    print(f"Membros da Academia salvos: {len(membro_dao.get_all())}")

    # --- Filmes ---
    filme1 = Filme("Forrest Gump", 1994, "Americano", "Robert Zemeckis") 
    filme2 = Filme("Barbie", 2023, "Americana", "Greta Gerwig")
    filme3 = Filme("Pulp Fiction", 1994, "Americano", "Quentin Tarantino")

    if not filme_dao.get(filme1.nome):
        filme_dao.add(filme1)
    if not filme_dao.get(filme2.nome):
        filme_dao.add(filme2)
    if not filme_dao.get(filme3.nome):
        filme_dao.add(filme3)
    print(f"Filmes salvos: {len(filme_dao.get_all())}")

    print("Dados de exemplo inicializados com sucesso!")

if __name__ == "__main__":
    inicializar_dados_exemplo()
    
    ControladorSistema().abre_tela()
    