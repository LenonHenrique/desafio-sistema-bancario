menu = """
Sistema Bancário Inicial

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite a opção desejada => """

saldo = 0
limite = 500
extrato = ""
quantidade_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0 :
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f} realizado.\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = quantidade_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\nOperação inválida! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação inválida! O valor do saque excedeu o limite diário.")
        
        elif excedeu_saque:
            print("Operação inválida! Número de saques diários excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} realizado.\n"
            quantidade_saque += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação disposta no menu.")