from datetime import date


class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date ) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f'Nome: {self._cpf}, CPF: {self._cpf}, Data de Nascimento: {self._data_nascimento}'



p = PessoaFisica('1234', 'Kev', 123)
print(p.__str__())