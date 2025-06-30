from DAOs.dao import DAO
from entidade.membro_academia import MembroAcademia

class MembroAcademiaDAO(DAO):
    def __init__(self):
        super().__init__('membros_academia.pkl')

    def add(self, membro: MembroAcademia):
        if isinstance(membro, MembroAcademia):
            super().add(membro.get_id, membro)
        else:
            raise TypeError("Objeto não é do tipo MembroAcademia")

    def update(self, membro: MembroAcademia):
        if isinstance(membro, MembroAcademia):
            super().update(membro.get_id, membro)
        else:
            raise TypeError("Objeto não é do tipo MembroAcademia")

    def get(self, id: str) -> MembroAcademia:
        return super().get(id)

    def remove(self, id: str):
        super().remove(id)