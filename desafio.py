menu = """
================ M.E.N.U ================
      ESCOLHA UMA DAS OPÇÕES ABAIXO

>>[d] Depositar
>>[s] Sacar
>>[e] Extrato
>>[q] Sair

=========================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Ops!!! Operação falhou! O valor informado NÃO é válido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Ops!!! Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Ops!!! Operação falhou! O valor do saque excede o limite.")
            print(f'\nSeu limite por saque é de R${limite:.2f}')

        elif excedeu_saques:
            print("Ops!!! Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações até o momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente uma operação do menu.")
