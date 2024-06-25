def deposito(saldo: float):
    deposito = float(input("Quanto gostaria de depositar: "))
    saldo += deposito
    return saldo, deposito

def saque(saldo: float):
    saque = float(input("Qual o valor da quantia que deseja sacar: "))
    saldo -= saque
    return saque, saldo





def banco():
    menu = """
        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Sair

    ==> """

    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.00
    saldo = 0
    extrato = {
        "saque": [],
        "deposito": [] 
    }


    while True:
        while True:
            try:
                escolha = int(input(menu))
                break
            except ValueError:
                print("ERRO: Informe um valor inteiro Válido!")


        if escolha == 1: #Depósito
            decoracao('Depósito')
            action_depositar = deposito(saldo)
            valor_deposito = action_depositar[1] #Pega o valor deposito da funcao deposito()
            saldo = action_depositar[0] #Pega o valor do saldo da funcao deposito()
            extrato['deposito'].append(valor_deposito) #armazena o valor do deposito no extrato
        elif escolha == 2: #Saque
            decoracao('Saque')
            action_sacar = saque(saldo)
            valor_saque = action_sacar[0] #Pega o valor do saque da funcao saque()

            insuficiente_saldo = valor_saque > saldo 

            limite_saque_dia = len(extrato["saque"]) == LIMITE_SAQUES

            valor_limite_saque = valor_saque > LIMITE_VALOR_SAQUE

            if insuficiente_saldo:
                print("Saldo insuficiente para realizar transação!")
            elif limite_saque_dia:
                print("Você atingiu o limite de saques diários.")
                print("Transação cancelada!")
            elif valor_limite_saque:
                print("Você ultrapassou o valor limite de saque de R$500,00")
                print("Transação cancelada!")
            else:
                saldo = action_sacar[1] #Pega o valor do saldo da funcao saque()
                extrato['saque'].append(valor_saque) #armazena o valor do saque no extrato
                print(f"Transação realizada com sucesso.")
        elif escolha == 3: #Extrato
            decoracao('Extrato')
            print(f"Seu Saldo atual corresponde a: R${saldo:.2f}")
            print(f"Saques: {extrato['saque']}")
            print(f"Depósitos: {extrato['deposito']}")
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