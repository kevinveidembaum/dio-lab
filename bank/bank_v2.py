from abc import abstractmethod
from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


    def __str__(self) -> str:
        return f'Nome: {self._nome}, CPF: {self._cpf}, Data de Nascimento: {self._data_nascimento}'


class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str, contas: list) -> None:
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = contas

    
    def __str__(self) -> str:
        return super().__str__() + f', Endereço: {self._endereco}, Contas: {self._contas}'
    

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass
    

    def adicionar_conta(conta: Conta):
        pass
    

class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico) -> None:
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self.historico = historico


    def __str__(self) -> str:
        return f'Saldo: {self._saldo}, Agência: {self._agencia}, Cliente: {self._cliente._nome}'


    def saldo(self) -> float:
        return self._saldo


    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        pass


    def sacar(valor: float) -> bool:
        pass


    def depositar(valor: float) -> bool:
        pass


class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)


class Transacao:
    @abstractmethod
    def registrar(conta: Conta):
        pass


class Historico:
    def __init__(self) -> None:
        pass


    #atributo transaçoes do tipo Transacao


    def adicionar_transacao(transacao: Transacao):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor


    def registrar(conta: Conta): #Implementar funcao de registrar
        pass


class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor


    def registrar(conta: Conta): #Implementar funcao de registrar
        pass



birth_date = date(1990, 12, 4)

c = Cliente('1234', 'Kev', birth_date, 'qwer', [1, 2])
conta = Conta(1200, 123, 'itau', c, 0)
print(conta.__str__())
print(conta.saldo())