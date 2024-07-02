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


birth_date = date(1990, 12, 4)

c = Cliente('1234', 'Kev', birth_date, 'qwer', [1, 2])
print(c.__str__())