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
            deposito = float(input("Quanto gostaria de depositar: "))
            saldo += deposito
            extrato['deposito'].append(deposito)
        elif escolha == 2: #Saque
            decoracao('Saque')
            saque = float(input("Qual o valor da quantia que deseja sacar: "))
            if saque > saldo:
                print("Saldo insuficiente para realizar transação!")
            elif len(extrato["saque"]) == LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
                print("Transação cancelada!")
            elif saque > LIMITE_VALOR_SAQUE:
                print("Você ultrapassou o valor limite de saque de R$500,00")
                print("Transação cancelada!")
            else:
                extrato['saque'].append(saque)
                saldo -= saque
                print(f"Transação realizada com sucesso.")
        elif escolha == 3: #Extrato
            decoracao('Extrato')
            print(f"Seu Saldo atual corresponde a: R${saldo:.2f}")
            print("Saques: " + ", ".join([f"R$ {x:.2f}" for x in extrato["saque"]]))
            print("Depósitos: " + ", ".join([f"R$ {x:.2f}" for x in extrato["deposito"]]))
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