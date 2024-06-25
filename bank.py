def banco():
    menu = """
        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Sair

    ==> """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques, numero_depositos = 0, 0
    LIMITE_SAQUES = 3


    while True:
        while True:
            try:
                escolha = int(input(menu))
                break
            except ValueError:
                print("ERRO: Informe um valor inteiro Válido!")


        if escolha == 1:
            print("Depósito")
            deposito = float(input("Quanto gostaria de depositar: "))
            saldo += deposito
            numero_depositos += 1
        elif escolha == 2:
            print("Saque")
            saque = float(input("Qual o valor da quantia que deseja sacar: "))
            if saque > saldo:
                print("Saldo insuficiente para realizar transação!")
            elif numero_saques == LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
                print("Transação cancelada!")
            elif saque > 500.00:
                print("Você ultrapassou o valor limite de saque de R$500,00")
                print("Transação cancelada!")
            else:
                saldo -= saque
                numero_saques += 1
                print(f"Transação realizada com sucesso.")
        elif escolha == 3:
            print("Extrato")
            print(f"Seu Saldo atual corresponde a: R${saldo:.2f}")
            print(f"Número de Saques: {numero_saques}")
            print(f"Número de depósitos: {numero_depositos}")
        elif escolha == 0:
            print("Programa encerrado com sucesso!")
            break
        else:
            print("Digite um valor válido!")



def main():
    banco()
    
if __name__ == "__main__":
    main()