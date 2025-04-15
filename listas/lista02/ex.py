'''
 Crie um programa que some todos os números pares entre 1 e n , onde n é fornecido pelo
usuário.
''' 
n = int(input("Digite um número N: "))
soma = sum(num for num in range(2, n+1, 2))
print(f"A soma dos números pares entre 1 e {n} é {soma}")

'''Escreva um aplicativo que solicita ao usuário que insira o tamanho do lado de um quadrado e,
então, exibe um quadrado vazio desse tamanho com asteriscos. Seu programa deve trabalhar
com quadrados de todos os comprimentos de lado possíveis entre 1 e 20.'''

n = int(input("Digite o tamanho do lado do quadrado (1 a 20): "))
while n < 1 or n >20:
    n = int(input("Tamanho inválido. Digite novamente (1 a 20): "))
for i in range(n):  
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''Crie um jogo simples de adivinhação em que o programa escolhe um número aleatório entre 1
e 100 e o usuário tem que adivinhar.'''

import random
n = random.randint(1, 100)
tentativas = 0      
while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1
    if palpite < n:
        print("Tente um número maior.")
    elif palpite > n:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {n} em {tentativas} tentativas.")
        break

''' Verifique se uma string é um palíndromo, ignorando espaços, pontuações e diferenças entre
maiúsculas e minúsculas'''

texto = input("Digite um texto: ")

# Remove caracteres não alfanuméricos e converte para minúsculas
limpo = ''.join(c for c in texto if c.isalnum()).lower()

# Verifica se é palíndromo
print("É palíndromo!" if limpo == limpo[::-1] else "Não é palíndromo.")

'''Crie um programa que verifique se duas palavras ou frases são anagramas, ou seja, se
possuem os mesmos caracteres (ignorando espaços e maiúsculas/minúsculas'''

def isAnagram(a, b):
    a = a.sorted(a.lower()).replace(" ", "")
    b = b.sorted(b.lower()).replace(" ", "")
    return a == b
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")
print("As frases são anagramas!" if isAnagram(frase1, frase2) else "As frases não são anagramas.")

'''Implemente o algoritmo da sequência de Collatz. Dado um número inteiro positivo, se ele for
par, divida-o por 2; se for ímpar, multiplique-o por 3 e some 1. Repita o processo até que o
número se torne 1. Exiba a sequência completa e o número de passos necessários.'''

n = int(input("Digite um número positivo: "))
sequencia = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else n * 3 + 1
    sequencia.append(n)
print(f"Sequência: {sequencia}")
print(f"Passos: {len(sequencia)-1}")

''' Implemente o Crivo de Eratóstenes (faça uma pesquisa) para gerar todos os números primos
até um número N fornecido pelo usuário'''

n = int(input("Digite um número N: "))
primos = [True] * (n+1)
primos[0] = primos[1] = False
for i in range(2, int(n**0.5)+1):
    if primos[i]:
        for j in range(i*i, n+1, i):
            primos[j] = False
print([i for i, val in enumerate(primos) if val])

'''A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Os dois primeiros termos são iguais a 1, e
a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥
3, exiba o n-ésimo termo da série de Fibonacci. Não use recursivo.)'''

n = int(input("Digite n (≥3): "))
a, b = 1, 1
for _ in range(n-2):
    a, b = b, a + b
print(f"O {n}º termo é {b}")

'''Um número de Armstrong é aquele que é igual à soma de seus dígitos elevados à potência do
número de dígitos. Por exemplo, 153 é um número de Armstrong, pois .
Crie um programa que imprima todos os números de Armstrong em um intervalo definido pelo
usuário.'''

inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

for num in range(inicio, fim+1):
    digitos = list(map(int, str(num)))
    potencia = len(digitos)
    soma = sum(d ** potencia for d in digitos)
    if soma == num:
        print(num)


'''Crie um programa que leia uma lista de palavras e um termo a ser buscado. Utilize um
laço for para realizar uma busca linear na lista. Se a palavra for encontrada, imprima o índice
em que ela está; caso contrário, informe que a palavra não foi encontrada.
N N'''
palavras = input("Digite palavras separadas por espaço: ").split()
busca = input("Termo a buscar: ")

encontrado = -1
for i, palavra in enumerate(palavras):
    if palavra == busca:
        encontrado = i
        break

print(f"Encontrado no índice {encontrado}" if encontrado != -1 else "Não encontrado")