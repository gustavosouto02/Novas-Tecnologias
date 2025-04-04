intervalos = [(1, 4), (2, 5), (7, 9), (8, 10), (12, 15), (14, 20)]

intervalos.sort()
novo_intervalo = [intervalos[0]]

for inicio, fim in intervalos[1:]:
    ultimo_inicio, ultimo_fim = novo_intervalo[-1]
    
    if inicio<=ultimo_fim:
        novo_intervalo[-1] = (ultimo_inicio, max(ultimo_fim, fim))
    else:
        novo_intervalo.append((inicio, fim))
  
print(intervalos)      
print(novo_intervalo)

'''questao 3'''