from DAOs.dao import DAO
from entidade.voto import Voto

class VotoDAO(DAO):
    def __init__(self):
        super().__init__('votos.pkl')

    def add(self, key: tuple, voto: Voto):
        if isinstance(voto, Voto) and isinstance(key, tuple) and len(key) == 2:
            super().add(key, voto)
        else:
            raise TypeError("Objeto não é do tipo Voto ou a chave está incorreta.")

    def update(self, key: tuple, voto: Voto):
        if isinstance(voto, Voto) and isinstance(key, tuple) and len(key) == 2:
            super().update(key, voto)
        else:
            raise TypeError("Objeto não é do tipo Voto ou a chave está incorreta.")

    def get(self, key: tuple) -> Voto:
        return super().get(key)

    def remove(self, key: tuple):
        super().remove(key)