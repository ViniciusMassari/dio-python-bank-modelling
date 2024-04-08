from abc import ABC, abstractmethod
from conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self,conta:Conta):
        pass

class Deposito(Transacao):
    __valor:float

class Saque(Transacao):
    __valor:float


