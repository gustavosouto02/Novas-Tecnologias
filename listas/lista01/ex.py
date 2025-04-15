'''
Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*).
'''

def desenhar_caixa(largura=5, altura=4):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('*' * largura)
        else:
            print('*' + ' ' * (largura - 2) + '*')

print("Caixa:")
desenhar_caixa()

def desenhar_oval(raio_vertical=3, raio_horizontal=2):
    for y in range(-raio_vertical, raio_vertical + 1):
        linha = []
        for x in range(-raio_horizontal, raio_horizontal + 1):
            if (x**2)/(raio_horizontal**2) + (y**2)/(raio_vertical**2) <= 1:
                linha.append('*')
            else:
                linha.append(' ')
        print(''.join(linha))

print("\nOval:")
desenhar_oval()

def desenhar_seta(tamanho=3):
    # Ponta da seta
    print(' ' * tamanho + '*')
    
    # Corpo da seta
    for i in range(1, tamanho + 1):
        print(' ' * (tamanho - i) + '*' * (2 * i + 1))
    
    # Haste da seta
    for _ in range(tamanho):
        print(' ' * tamanho + '*')

print("\nSeta:")
desenhar_seta()

def desenhar_losango(tamanho=3):
    for i in list(range(tamanho)) + list(range(tamanho - 2, -1, -1)):
        print(' ' * (tamanho - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i != 0 else ''))

print("\nLosango:")
desenhar_losango()

'''
Escreva um aplicativo que insere um número de cinco dígitos, separa os dígitos e imprime com três espaços entre eles.
'''
numero = input("Digite um número de 5 dígitos: ")
print("   ".join(numero))


'''
Faça um programa que calcule a distância entre dois pontos no plano cartesiano.
'''
import math

x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distância: {distancia:.2f}")


'''
Crie um programa que conte quantas vogais aparecem em uma frase (case-insensitive).
'''
frase = input("Digite uma frase: ").lower()
vogais = sum(1 for letra in frase if letra in 'aeiou')
print(f"Total de vogais: {vogais}")


'''
Criptografe e descriptografe um número de 4 dígitos conforme o esquema descrito.
'''
# Criptografia
numero = input("Digite um número de 4 dígitos para criptografar: ")
criptografado = [(int(digito) + 7) % 10 for digito in numero]
criptografado = f"{criptografado[2]}{criptografado[3]}{criptografado[0]}{criptografado[1]}"
print(f"Número criptografado: {criptografado}")

# Descriptografia
criptografado = input("\nDigite um número de 4 dígitos criptografado: ")
original = [(int(digito) - 7) % 10 for digito in criptografado]
original = f"{original[2]}{original[3]}{original[0]}{original[1]}"
print(f"Número original: {original}")