MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode retirar CNH")
else:
    print("CNH nao autorizada!")


if idade >= MAIOR_IDADE:
    print("Maior idade autorizado")
elif idade == IDADE_ESPECIAL:
    print("Aula teoricas autorizadas.")
else:
    print("Aulas praticas nao autorizadas")