conta_normal = False
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Nao é possivel realizar o saque")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucessooooo")
    else:
        print("Saldo insuficiente")

elif conta_especial:
    print("Conta especial selecionada")

else:
    print("Sistema nao reconhece o tipo de conta, contate o seu gerente")
