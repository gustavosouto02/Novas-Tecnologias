'''
Dada uma lista de palavras, construa um dicionário que mapeia cada palavra para o número de caracteres que ela possui.
'''
palavras = ["python", "java", "c", "javascript", "ruby"]
tamanhos = {palavra: len(palavra) for palavra in palavras}
print(tamanhos)


'''
Agrupe palavras em dicionário onde a chave é a forma canônica (caracteres ordenados) e o valor são os anagramas.
'''
from collections import defaultdict

palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]
anagramas = defaultdict(list)

for palavra in palavras:
    chave = tuple(sorted(palavra.lower()))
    anagramas[chave].append(palavra)

print(dict(anagramas))


'''
Mescle intervalos que se sobrepõem.
'''
def merge_intervals(intervalos):
    if not intervalos:
        return []
    
    intervalos.sort()
    merged = [intervalos[0]]
    
    for current in intervalos[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

intervalos = [(1, 4), (2, 5), (7, 9)]
print(merge_intervals(intervalos))


'''
Conte a frequência de números e filtre os que aparecem pelo menos N vezes.
'''
from collections import Counter

numeros = [1, 2, 3, 4, 2, 3, 1, 2, 4, 2, 5, 6, 2]
contagem = Counter(numeros)
minimo = 3
filtrados = [num for num, count in contagem.items() if count >= minimo]
print(filtrados)


'''
Multiplique dois polinômios representados como dicionários {expoente: coeficiente}.
'''
def multiplicar_polinomios(p1, p2):
    resultado = {}
    for exp1, coef1 in p1.items():
        for exp2, coef2 in p2.items():
            exp = exp1 + exp2
            resultado[exp] = resultado.get(exp, 0) + coef1 * coef2
    return resultado

p1 = {2: 3, 1: 2, 0: 1}  # 3x² + 2x + 1
p2 = {1: 1, 0: 1}        # x + 1
print(multiplicar_polinomios(p1, p2))

'''
Determine se existe um subconjunto cuja soma seja igual ao valor alvo.
'''
def existe_soma_alvo(numeros, alvo):
    possiveis = {0}
    for num in numeros:
        novos = {num + x for x in possiveis}
        if alvo in novos:
            return True
        possiveis.update(novos)
    return False

numeros = [3, 34, 4, 12, 5, 2]
alvo = 9
print(existe_soma_alvo(numeros, alvo))


'''
Implementação do jogo da Forca.
'''
import random

palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
palavra = random.choice(palavras)
tentativas = 6
letras_corretas = set()
letras_erradas = set()

while tentativas > 0:
    palavra_oculta = [letra if letra in letras_corretas else '_' for letra in palavra]
    print(' '.join(palavra_oculta))
    
    if '_' not in palavra_oculta:
        print("Parabéns! Você acertou!")
        break
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já tentou esta letra.")
    elif letra in palavra:
        letras_corretas.add(letra)
    else:
        letras_erradas.add(letra)
        tentativas -= 1
        print(f"Letra errada! Tentativas restantes: {tentativas}")

if tentativas == 0:
    print(f"Game over! A palavra era: {palavra}")


'''
Verifique se os parênteses estão balanceados usando pilha.
'''
def verificar_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0

expressoes = ["(())", "()()(()())", "( ) )"]
for expr in expressoes:
    print(f"{expr}: {'OK' if verificar_parenteses(expr) else 'Erro'}")


'''
Compare duas listas usando operações com conjuntos.
'''
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print("Valores comuns:", set(lista1) & set(lista2))
print("Valores apenas na primeira:", set(lista1) - set(lista2))
print("Valores apenas na segunda:", set(lista2) - set(lista1))
print("Elementos não repetidos:", set(lista1) ^ set(lista2))
print("Primeira lista sem elementos da segunda:", [x for x in lista1 if x not in lista2])


'''
Armazene informações de pessoas em dicionários e listas.
'''
pessoas = []

while True:
    pessoa = {
        'first_name': input("Primeiro nome: "),
        'last_name': input("Sobrenome: "),
        'age': int(input("Idade: ")),
        'city': input("Cidade: ")
    }
    pessoas.append(pessoa)
    
    continuar = input("Cadastrar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nPessoas cadastradas:")
for i, pessoa in enumerate(pessoas, 1):
    print(f"\nPessoa {i}:")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")