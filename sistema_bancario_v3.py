import textwrap

def menu():
    menu = """
    Sistema Bancário Inicial

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    Digite a opção desejada => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f"Deposito de R$ {valor:.2f} realizado.\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                    
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, quantidade_saque, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = quantidade_saque >= LIMITE_SAQUES
            
    if excedeu_saldo:
        print("\n Operação inválida! Você não possui saldo suficiente.")
            
    elif excedeu_limite:
        print("\n Operação inválida! O valor do saque excedeu o limite diário.")
            
    elif excedeu_saque:
        print("\n Operação inválida! Número de saques diários excedidos.")
            
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f} realizado.\n"
        quantidade_saque += 1
        print(f"\nSaque de R${valor:.2f} realizado com sucesso.")

    else:
        print("\n Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf,usuarios)
    
    if usuario:
        print("\nJá existe um usuário cadastrado com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, número - bairro - cidade / sigla do estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\nUsuário cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = print("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta:": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado na base de dados, processo encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main(): 
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saque = 0
    usuarios = []
    contas = []
    #numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
            
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor= valor,
                extrato=extrato,
                limite=limite,
                quantidade_saque=quantidade_saque,
                LIMITE_SAQUES=LIMITE_SAQUES
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuario(usuarios)
            
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                #numero_conta += 1
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação disposta no menu.")


main()