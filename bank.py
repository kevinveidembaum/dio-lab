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
    [0] Sair

    ==> """
    while True:
        try:
            escolha = int(input(menu))
            if escolha in [1, 2, 3, 0]:
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

def banco():
    saldo = 0
    extrato = {
        "saque": [],
        "deposito": [] 
    }

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
        elif escolha == 0:
            print('~'*30)
            print("Programa encerrado com sucesso!")
            break
        else:
            print("Digite um valor válido!")

def decoracao(msg):
    tam = len(msg) + 4
    print("-="*tam)
    print(f"{msg:^25}")
    print("-="*tam)

def main():
    banco()
    
if __name__ == "__main__":
    main()