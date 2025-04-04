def soma (a,b=100):
    '''Função para calcular soma'''
    return a+b
print(soma.__doc__) # doc para printar o que está "comentado" na função
print(soma(b=2, a=10))