MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode retirar CNH")
else:
    print("CNH nao autorizada!")