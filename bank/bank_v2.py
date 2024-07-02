from abc import ABC, abstractmethod
from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


    def __str__(self) -> str:
        return f'Nome: {self._nome}, CPF: {self._cpf}, Data de Nascimento: {self._data_nascimento}'


class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str) -> None:
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = []
    

    def realizar_transacao(self, conta, transacao): #tipo Conta, e tipo Transacao
        transacao.registrar(conta)
    

    def adicionar_conta(self, conta): #tipo Conta
        self._contas.append(conta)
    

class Conta:
    def __init__(self, cliente: Cliente, numero: int) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(cliente, numero)


    def sacar(valor: float) -> bool:
        pass


    def depositar(valor: float) -> bool:
        pass


    @property
    def cliente(self):
        return self._cliente


    @property
    def saldo(self) -> float:
        return self._saldo


    @property
    def numero(self):
        return self._numero
    

    @property
    def agencia(self):
        return self._agencia
    

    @property
    def historic(self):
        return self._historico


class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, limite:float = 500, limites_saque:int = 5) -> None:
        super().__init__(cliente, numero)
        self._limite = limite
        self._limites_saque = limites_saque


    def sacar(self, valor:float):
        pass


    def __str__(self) -> str:
        pass


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Historico:
    def __init__(self) -> None:
        self._transacoes = []


    @property
    def transacoes(self):
        return self._transacoes


    def adicionar_transacao(self, transacao: Transacao):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(conta: Conta): #Implementar funcao de registrar
        pass


class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    
    @property
    def valor(self):
        return self._valor
    

    def registrar(conta: Conta): #Implementar funcao de registrar
        pass



birth_date = date(1990, 12, 4)

c = Cliente('1234', 'Kev', birth_date, 'rua jjj')
conta = Conta(c, 123)
