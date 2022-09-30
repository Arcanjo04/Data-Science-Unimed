opcao = int(input("Informe uma opcao: [1] sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))

elif opcao == 2:
    print("Exibir o extrato")
else:
    sys.exit("Opcao invalida1")