# texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")
else:
    print()
    print("Execute no final do laçoQuem nasce para vencer não desanima diante das lutas")    