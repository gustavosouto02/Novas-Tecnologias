frase = input("Digite uma frase: ").lower()

palavras = frase.rsplit(sep = " ")
'''
mapa = {}
for palavra in palavras:
    if palavra in mapa:
        mapa[palavra] = mapa.get(palavra, 0)+len(palavra)
    else:
        mapa[palavra] = len(palavra)

print(mapa)

'''
mapa = {}
mapa = {palavra:len(palavra) for palavra in palavras if palavra not in mapa }
print(mapa)

'''Questão 1 da listas'''