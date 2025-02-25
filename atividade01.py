'''Escreva um aplicativo que insere um número consistindo em cinco dígitos
do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
usuário digitar o número 42339, o programa deve imprimir:
4 2 3 3 9.'''
'''
def separar_digitos():
    num = input("Digite um numero de cinco digitos: ")

    if len(num) == 5 and num.isdigit():
        print(" ".join(num)) # printa um espaço
        
    else:
        print("Erro: Insira um numero valido com exatamente 5 digitos.")
    
separar_digitos()'''

'''
O quadrado de um número natural n é dado pela soma dos n primeiros
números ímpares consecutivos. 1 =2 1, 2 =2 1 + 3, 3 =2 1 + 3 + 5
Dado um número n, calcule seu quadrado usando a soma de ímpares ao
invés de produto.'''

'''def quadrado_soma(n):
    soma = 0
    impar = 1
    for _ in range(n):
        soma += impar
        impar += 2
    return soma

while True:
    try:
        n = int(input("Digite um numero natural: \n"))
        if n >= 0:
            print(f"O quadrado de {n} é igual a {quadrado_soma(n)}")
            break
        else:
            print("Erro: Insira um número natural.")
    except ValueError:
        print("Erro: Insira um valor numérico")

'''
'''
3. Defina uma função recursiva para calcular a soma de dois naturais usando
as funções suc(n) e pred(n) que devolvem, respectivamente, o sucessor e o
predecessor de um natural n.'''

'''def suc(n):
    return n + 1

def pred(n):
    return n - 1 if n > 0 else 0

def soma_recursiva(a, b):
    if b == 0:
        return a
    return soma_recursiva(suc(a), pred(b))

while True:
    try:
            
        if __name__ == "__main__":
            a = int(input("Digite o primeiro numero natural: "))
            b = int(input("Digite o segundo numero natural: "))

            if a < 0 or b < 0:
                print("Ambos os números devem ser naturais.")
            else:
                print(f"A soma de {a} e {b} é {soma_recursiva(a, b)}")
                break
    except ValueError:
        print("Erro: Insira um valor numérico.")
'''

'''def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    hanoi(n - 1, auxiliar, destino, origem)

if __name__ == "__main__":
    n = int(input("Digite o número de discos: "))
    hanoi(n, 'A', 'C', 'B')'''
