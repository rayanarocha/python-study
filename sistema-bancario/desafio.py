menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor para depósito: "))
        if(deposito <= 0) :
            print("Digite um valor positivo e diferente de zero.")
        else:
            saldo+=deposito
            print(saldo)
    elif opcao == "s":
        saque = float(input("Digite um valor para saque: "))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Número máximo de saques excedido.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Valor informado inválido.")
    elif opcao == "e":
        print("\n============EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida. Por favor, digite novamente a opção desejada.")