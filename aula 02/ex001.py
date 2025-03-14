#Algoritmo para coletar informações

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
massa = float(input('Digite seu peso: '))
            
print(f'\nNome: {nome}\nIdade: {idade}\nIMC: {massa/altura**2:.2f}')
