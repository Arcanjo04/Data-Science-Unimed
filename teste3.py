tempo, velocidade = list(map(int,input().split()))
quantidade_litros = (tempo * velocidade) / 12
print(f"{quantidade_litros:.3f}")