'''formatar datas'''

def formatar_data(dia, mes, ano):
    return f"{dia:02}/{mes:02}/{ano}"

print(formatar_data(dia=5, mes=3, ano=2023))  # 05/03/2023
print(formatar_data(ano=2023, mes=12, dia=1))  # 01/12/2023
print(formatar_data(ano=2023, mes=1, dia=15))  # 15/01/2023

'''Operações'''
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else 'Divisão por zero'

def aplicar_operacao(num1, num2=None, operacao=None):
    if operacao:
        return operacao(num1, num2) if num2 is not None else operacao(num1)
    return None

print(aplicar_operacao(5, 3, soma))          # 8
print(aplicar_operacao(5, 3, subtracao))     # 2
print(aplicar_operacao(5, 3, multiplicacao)) # 15
print(aplicar_operacao(5, 0, divisao))       # Divisão por zero

'''funções recursivas'''
#a
def resto_divisao(a, b):
    if a < b:
        return a
    return resto_divisao(a - b, b)

print(resto_divisao(10, 3))  # 1

#b
def quociente_divisao(a, b):
    if a < b:
        return 0
    return 1 + quociente_divisao(a - b, b)

print(quociente_divisao(10, 3))  # 3

#c
def produto(a, b):
    if b == 0:
        return 0
    return a + produto(a, b - 1)

print(produto(5, 3))  # 15

#d
def suc(n):
    return n + 1

def pred(n):
    return n - 1 if n > 0 else 0

def soma(a, b):
    if b == 0:
        return a
    return soma(suc(a), pred(b))

print(soma(5, 3))  # 8

''' função recursiva para calcular o n-ésimo termo de uma sequência definida'''

memo = {}

def sequencia(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = sequencia(n - 1) + 2 * sequencia(n - 2)
    return memo[n]

# Testando
print(sequencia(5))  # 5

# Lambda encapsulando a função
sequencia_lambda = lambda n: sequencia(n)
print(sequencia_lambda(5))  # 5


'''Tools'''
import re
from collections import Counter

def limpar_texto(texto):

    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.lower()

def tokenizar(texto):
    return texto.split()

def frequencia_palavras(texto):
    palavras = tokenizar(limpar_texto(texto))
    return Counter(palavras)

def palavras_comuns(texto, n):
    frequencias = frequencia_palavras(texto)
    return frequencias.most_common(n)

def main():
    texto = "Aqui está um exemplo de texto. Este texto é um exemplo de texto."
    palavras_frequentes = palavras_comuns(texto, 5)

    for palavra, contagem in palavras_frequentes:
        print(f"{palavra}: {contagem}")

if __name__ == "__main__":
    main()


'''ler dados csv'''

import csv

def ler_csv(caminho):

    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return [linha for linha in leitor]

def total_vendas_por_produto(dados):

    total_por_produto = {}
    for venda in dados:
        produto = venda['produto']
        valor = float(venda['valor']) * int(venda['quantidade'])
        total_por_produto[produto] = total_por_produto.get(produto, 0) + valor
    return total_por_produto

'''estatistica'''
import re
import csv
from collections import Counter

def limpar_texto(texto):

    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.lower()

def tokenizar(texto):
    return texto.split()

def frequencia_palavras(texto):
    palavras = tokenizar(limpar_texto(texto))
    return Counter(palavras)

def palavras_comuns(texto, n):
    frequencias = frequencia_palavras(texto)
    return frequencias.most_common(n)

def ler_csv(caminho):

    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return [linha for linha in leitor]

def total_vendas_por_produto(dados):
    total_por_produto = {}
    for venda in dados:
        produto = venda['produto']
        valor = float(venda['valor']) * int(venda['quantidade'])
        total_por_produto[produto] = total_por_produto.get(produto, 0) + valor
    return total_por_produto

def main():
    texto = "Aqui está um exemplo de texto. Este texto é um exemplo de texto."
    print("Palavras mais frequentes no texto:")
    palavras_frequentes = palavras_comuns(texto, 5)
    for palavra, contagem in palavras_frequentes:
        print(f"{palavra}: {contagem}")

    print("\nTotal de vendas por produto:")
    try:
        dados_csv = ler_csv('vendas.csv')
        totais = total_vendas_por_produto(dados_csv)
        for produto, total in totais.items():
            print(f"{produto}: R$ {total:.2f}")
    except FileNotFoundError:
        print("Arquivo 'vendas.csv' não encontrado. Pulei a análise de vendas.")

if __name__ == "__main__":
    main()

'''introspecao'''
def mostrar_info(obj):
    print(f"Nome: {type(obj).__name__}")
    print(f"ID: {id(obj)}")
    print(f"Tipo: {type(obj)}")
    print(f"Docstring: {getattr(obj, '__doc__', 'Sem docstring')}")
    print("Métodos e Atributos:")
    print(dir(obj))


''' interpretador que avalie expressões aritméticas simples '''

import re

operadores = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 'Divisão por zero'
}

def avaliar(expressao):
    expressao = expressao.replace(" ", "")
    
    def eval_expr(expr):
        if '(' in expr:
            last_open = expr.rfind('(')
            last_close = expr.find(')', last_open)
            inner_result = eval_expr(expr[last_open + 1:last_close])
            expr = expr[:last_open] + str(inner_result) + expr[last_close + 1:]
            return eval_expr(expr)  

        for op in ('*', '/'):
            parts = re.split(r'(\*|/)', expr)
            while len(parts) > 1:
                for i in range(1, len(parts), 2):
                    if parts[i] == op:
                        left = float(parts[i - 1])
                        right = float(parts[i + 1])
                        result = operadores[op](left, right)
                        parts = parts[:i - 1] + [result] + parts[i + 2:]
                        break
                else:
                    break

        parts = re.split(r'(\+|-)', expr)
        result = float(parts[0])
        for i in range(1, len(parts), 2):
            op = parts[i]
            right = float(parts[i + 1])
            result = operadores[op](result, right)

        return result

    return eval_expr(expressao)

print(avaliar("3 + 5"))               # 8
print(avaliar("10 + 2 * 6"))          # 22
print(avaliar("100 * 2 + 12"))        # 212
print(avaliar("100 * (2 + 12)"))      # 1400
print(avaliar("100 * (2 + 12) / 14")) # 100.0
print(avaliar("3 + 5 * (2 - 1)"))     # 8
print(avaliar("10 / 2 + 3 * 4"))      # 16.0


'''simulador de jogo de dados'''

import random

eventos = {}

def registrar_evento(nome, callback):
    if nome not in eventos:
        eventos[nome] = []
    eventos[nome].append(callback)

def disparar_evento(nome, *args, **kwargs):
    if nome in eventos:
        for callback in eventos[nome]:
            callback(*args, **kwargs)

def evento(nome):
    def decorator(func):
        registrar_evento(nome, func)
        return func
    return decorator

def lançar_dado():
    return random.randint(1, 6)

@evento("sorte")
def evento_sorte():
    print("Você lançou um 6! Você ganhou um prêmio!")

@evento("azar")
def evento_azar():
    print("Você lançou um 1! Tente novamente!")

def main():
    resultado = lançar_dado()
    print(f"Resultado do dado: {resultado}")
    if resultado == 6:
        disparar_evento("sorte")
    elif resultado == 1:
        disparar_evento("azar")

if __name__ == "__main__":
    main()
