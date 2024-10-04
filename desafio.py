menu = ("""
    ======MENU======
    [1]Sacar
    [2]Depositar
    [3]Extrato
    [0]Sair
    ==================
    ->""")

saldo = 1000
limite = 500
extrato = ""
SAQUE_DIARIO = 3
saques_feitos = 0

while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        saque = float(input("Digite o valor do saque: "))
        if (saque) <= (saldo) and  (saque) <= (limite) and (saque) > 0 and saques_feitos < SAQUE_DIARIO:
            print (f"Quantia de R${saque} sacado com sucesso.")
            saldo -= (saque)
            saques_feitos += 1
            extrato += f"Saque de: R${saque:,.2f}\n"
        elif (saque) > (saldo):
            print(f"Valor de R${saque} excede seu saldo na conta.")
        elif (saque)  > (limite):
            print(f"Valor de R${saque} excede seu limite por saques.")
        elif saques_feitos >= SAQUE_DIARIO:
            print("Limites de saques diários atingido.")
        else:
            print("Digite um valor válido.")
    elif opcao == 2:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            print(f"Depósito no valor de R${deposito} foi efetuado com sucesso.")
            saldo += (deposito)
            extrato += f"Depósito de: R${deposito:,.2f}\n"
        else:
            print("Deposite um valor válido.")
    elif opcao == 3:
        print("=========================================\n")
        print("Não ouveram movimentações na sua conta" if not extrato else extrato)
        print(f"\nseu saldo é de R${saldo:,.2f}")
        print("=========================================\n")
    elif opcao == 0:
        break
    else:
        print("Operação não reconhecida, tente novamente.")
