p1 = {2: 3, 1: 2, 0: 1}  # 3x^2 + 2x + 1
p2 = {1: 1, 0: 4}  # x + 4

# Multiplicação dos polinômios
p_result = {}
for exp1, coef1 in p1.items():
    for exp2, coef2 in p2.items():
        p_result[exp1 + exp2] = p_result.get(exp1 + exp2, 0) + coef1 * coef2

# Exibir P1
for chave, valor in p1.items():
    print(f"{valor}x^{chave}", end=" ")
    if chave != 0:
        print("+", end=" ")
print()

# Exibir P2
for chave, valor in p2.items():
    print(f"{valor}x^{chave}", end=" ")
    if chave != 0:
        print("+", end=" ")
print()

# Exibir resultado
for chave, valor in sorted(p_result.items(), reverse=True):
    print(f"{valor}x^{chave}", end=" ")
    if chave != 0:
        print("+", end=" ")
print()
