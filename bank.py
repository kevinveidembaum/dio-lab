def obter_string(mensagem: str, nome=False, cpf=False) -> str:
    while True:
        try:
            user = str(input(mensagem)).strip()
            if nome:
                if user.isalpha():
                    return user
                else:
                    print("Digite um nome válido!")

            if cpf:
                if user.isnumeric():
                    return user
                else:
                    print("Informe um CPF válido!")
            
            if not nome and not cpf:
                return user
        except ValueError:
            print("ERRO: Informe uma String Válida!")


def obter_valor(mensagem: str) -> float:
    while True:
            try:
                return float(input(mensagem))                
            except ValueError:
                print("ERRO: Informe um valor numérico Válido!")


def exibir_menu() -> int:
    menu = """
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Cadastrar Usuário
    [5] Criar Conta Corrente
    [6] Ver Usuários Cadastrados
    [7] Ver Contas Cadastradas
    [0] Sair

    ==> """
    while True:
        try:
            escolha = int(input(menu))
            if escolha in [0, 1, 2, 3, 4, 5, 6, 7]:
                return escolha
            else:
                print("ERRO: Selecione um valor presente no menu!")
        except ValueError:
            print("ERRO: Informe um valor Inteiro válido!")
            

def deposito(saldo: float):
    deposito = obter_valor("Quanto gostaria de depositar: ")
    saldo += deposito
    return saldo, deposito


def saque(saldo: float, saques_hoje: int) -> tuple[float, float]:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.00

    saque = obter_valor("Qual o valor da quantia que deseja sacar: ")

    if saques_hoje >= LIMITE_SAQUES:
        print("Você atingiu o limite de saques diários.")
        print("Transação cancelada!")
        return saldo, 0.0
    
    if saque > saldo:
        print("Saldo insuficiente para realizar transação!")
        return saldo, 0.0
    
    if saque > LIMITE_VALOR_SAQUE:
        print("Você ultrapassou o valor limite de saque de R$500,00")
        print("Transação cancelada!")
        return saldo, 0.0

    saldo -= saque
    return saldo, saque


def exibir_extrato(saldo: float, extrato: dict):
    decoracao('Extrato')
    print(f"Seu Saldo atual corresponde a: R${saldo:.2f}")
    print(f"Saques: {extrato['saque']}")
    print(f"Depósitos: {extrato['deposito']}")


def criar_user(lista_users: list):
    usuario = {
        "nome": "",
        "nasc": "",
        "cpf": "",
        "endereco": ""
    }
    decoracao("Cadastrar Usuário")
    nome = obter_string("Digite seu nome: ", True)
    nasc = obter_valor("Digite seu ano de nascimento: ")
    endereco = obter_string("Informe seu endereço: ")
    while True:
            cpf = obter_string("Informe seu CPF: ", False, True)
            if any(user['cpf'] in cpf for user in lista_users):
                print("Já tem um cadastro com esse CPF, tente novamente!")
            else:
                break

    usuario["nome"] = nome
    usuario["nasc"] = nasc
    usuario["cpf"] = cpf
    usuario["endereco"] = endereco

    lista_users.append(usuario)
    decoracao("Usuário Cadastrado com sucesso!", "≃", 35)
            

def listar_usuarios(lista_user: list):
    decoracao("Lista de Usuários")
    if not lista_user:
        print("Não há registro de usuários")
    for user in lista_user:
        print(f"Nome: {user['nome']}, Nascimento: {user['nasc']}, CPF: {user['cpf']}, Endereço: {user['endereco']}")


def listar_contas(lista_conta: list):
    decoracao("Lista de Contas")
    if not lista_conta:
        print("Não há registro de Contas")
    for conta in lista_conta:
        print(f"Proprietário da Conta: {conta['usuario']}, CPF: {conta['cpf_conta']}, Número da conta: {conta['numero']}, Agência: {conta['agencia']}")
        print()


def criar_conta(lista_user: list, lista_conta: list):

    if not lista_user:
        print("Não há nenhum usuário registrado")
        return

    decoracao("Criar Conta Corrente")
    print("Selecione um usuário para criar a conta:")

    for i, user in enumerate(lista_user, start=1):
        print(f"{i} - {user['nome']}")
    
    while True:
        try:
            escolha = int(obter_string("Digite o número correspondente ao usuário: "))
            if 1 <= escolha <= len(lista_user):
                usuario_conta = lista_user[escolha - 1] #Seleciona e armazena quem terá a conta
                break
            else:
                print("Escolha inválida!")
        except ValueError:
            print("ERRO. Digite um valor válido!")
    
    agencia = "0001"
    numero_conta = len(lista_conta) + 1

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario_conta['nome'],
        "cpf_conta": usuario_conta['cpf']
    }

    lista_conta.append(conta)
    decoracao(f"Sua conta criada com sucesso {usuario_conta['nome']}!")
    print(f"Agência: {agencia}, Número da conta: {numero_conta}")


def banco():
    saldo = 0
    extrato = {
        "saque": [],
        "deposito": [] 
    }
    lista_user = []
    lista_conta = []

    while True:
        escolha = exibir_menu()

        if escolha == 1: #Depósito
            decoracao('Depósito')
            saldo, valor_deposito = deposito(saldo)
            extrato['deposito'].append(valor_deposito) #armazena o valor do deposito no extrato
        elif escolha == 2: #Saque
            decoracao('Saque')
            saldo, valor_saque = saque(saldo, len(extrato["saque"]))
            if valor_saque > 0.0:
                extrato['saque'].append(valor_saque) #armazena o valor do saque no extrato
                print(f"Transação realizada com sucesso.")
        elif escolha == 3: #Extrato
            exibir_extrato(saldo, extrato)
        elif escolha == 4: #Criar Usuário
            criar_user(lista_user)
        elif escolha == 5: #Criar Conta Corrente
            criar_conta(lista_user, lista_conta)
        elif escolha == 6: #Listar Usuários Cadastrados
            listar_usuarios(lista_user)
        elif escolha == 7: #Listar Contas Cadastradas
            listar_contas(lista_conta)
        elif escolha == 0:
            decoracao("Programa encerrado com sucesso!", "~", 35)
            break
        else:
            print("Digite um valor válido!")

def decoracao(msg: str, simbolo: str = "-=", largura: int = 25):
    """Função para decorar e destacar mensagens no terminal.
    
    Args:
        msg (str): A mensagem a ser destacada.
        simbolo (str): O símbolo a ser usado na decoração. Padrão é '-='.
        largura (int): A largura total da linha de decoração. Padrão é 25.
    """
    linha = simbolo * ((largura // len(simbolo)) + 1)
    linha = linha[:largura] #Comprimento da linha
    
    print(linha)
    print(f"{msg:^{largura}}")
    print(linha)

def main():
    banco()
    
if __name__ == "__main__":
    main()