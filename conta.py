from transacoes import Transacao
from cliente import Cliente

class Historico:
    def adicionar_transacao(self,transacao:Transacao):
        pass

class Conta:
    __saldo: float
    __numero: int
    __agencia:str
    __cliente: Cliente
    __historico: Historico

    def saldo(self) -> float:
        return self.__saldo
    def nova_conta(self,cliente:Cliente, numero:int):
        pass
    def sacar(self, valor:float) -> bool:
        return True
    def depositar(self, valor:float) -> bool:
        return True

class ContaCorrent(Conta):
    __limite: float
    __limite_saques:int