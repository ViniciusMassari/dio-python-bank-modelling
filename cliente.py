from conta import Conta
from datetime import datetime
from transacoes import Transacao
class Cliente:
    __endereco:str
    __contas: list

    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        pass
    def adicionar_conta(self, conta:Conta):
        pass

class PessoaFisica(Cliente):
    __cpf:str
    __nome:str
    __data_nascimento: datetime