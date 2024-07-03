from abc import ABC, abstractmethod
from datetime import date, datetime

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}'


class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str) -> None:
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):  # tipo Conta, e tipo Transacao
        transacao.registrar(conta)

    def adicionar_conta(self, conta):  # tipo Conta
        self.contas.append(conta)


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

    def sacar(self, valor_saque: float) -> bool:
        excedeu_saque = valor_saque > self._saldo

        if excedeu_saque:
            print("Saldo insuficiente para realizar transação!")
            return False
        elif valor_saque > 0:
            self._saldo -= valor_saque
            print("Transação de Saque realizada com sucesso!")
            return True
        else:
            print("Operação falhou! Valor inválido para Saque!")

        return False

    def depositar(self, valor_deposito: float) -> bool:
        if valor_deposito > 0:
            self._saldo += valor_deposito
            print("Transação Depósito realizada com sucesso!")
            return True
        else:
            print("Insira um valor válido!")
            return False

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
    def historico(self):
        return self._historico


class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, limite: float = 500, limites_saque: int = 5) -> None:
        super().__init__(cliente, numero)
        self.limite = limite
        self.limites_saque = limites_saque

    def sacar(self, valor_saque: float):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_saques = numero_saques >= self.limites_saque
        excedeu_limite = valor_saque > self.limite

        if excedeu_saques:
            print("Você atingiu o limite de saques diários.")
            print("Transação cancelada!")

        elif excedeu_limite:
            print(f"Você ultrapassou o valor limite de saque de R${self.limite:.2f}")
            print("Transação cancelada!")

        else:
            return super().sacar(valor_saque)

        return False

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


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
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


birth_date = date(1990, 12, 4)

c = Cliente('1234', 'Kev', birth_date, 'rua jjj')
conta = Conta(c, 123)
conta.depositar(0)
conta.sacar(100)
conta.sacar(0)
