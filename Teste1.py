# A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), 
# que indicam, respectivamente, a distância entre os Palantír, 
# o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
#DistanciaTotal = float(input("Qual distancia entre os Palantir: "))
#D_Sauron = float(input("Qual diametro do Palantir de Sauron: "))
#D_Saruman = float(input("Qual diametro do Palantir de de Saruman: "))

#icm = (float(DistanciaTotal / (D_Sauron + D_Saruman)):2f)

#print(f'o icm de {icm:,.2f}')


DistanciaTotal, D_Sauron, D_Saruman = list(map(int, input().split(" ")))

def icm():
    return DistanciaTotal / (D_Sauron + D_Saruman)

print(f'{DistanciaTotal/(D_Sauron+D_Saruman):.2f}')