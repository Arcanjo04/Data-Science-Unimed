texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# utilizando a funcao interavel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")
else:
    print()
    print("Execute no final do laçoQuem nasce para vencer não desanima diante das lutas")    

# utilizando a funcao build-in range
for numero in range(0, 51, 5):
    print(numero, end = " ")