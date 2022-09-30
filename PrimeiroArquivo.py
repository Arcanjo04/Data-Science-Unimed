saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("realizando saque!")

if saldo < saque:
    print("saldo insuficiente!")