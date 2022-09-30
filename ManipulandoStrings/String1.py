nome = "Jose Mario"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "Ola mundo"

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "React"

print("####"+menu+"#####")
print(menu.center(15))
print(menu.center(15, "#"))

for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))