import random  # Importando a biblioteca para escolher a palavra aleatoriamente

palavras = ["banana", "melancia", "amora", "abacaxi", "uva"]  # Lista de palavras
palavras = random.choice(palavras)  # Escolhendo uma palavra aleatória

resultado = ["_" for _ in palavras]  # Lista para armazenar os acertos

boneco = [" O ", " O\n/", " O\n/|", " O\n/|\\", " O\n/|\\\n/", " O\n/|\\\n/ \\"]  # Desenho do boneco
erros = 0  # Contador de erros

while True:
    print(" ".join(resultado))  # Exibir progresso da palavra
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavras:
        for i, letra in enumerate(palavras):
            if letra == palpite:
                resultado[i] = letra  # Substitui o "_" pela letra correta
    else:
        print("Letra errada!")
        if erros < len(boneco):  # Evita erro de índice
            print(boneco[erros])  # Mostra a parte do boneco
            erros += 1
            
        if erros == len(boneco):  # Se o boneco for completo, o jogador perde
            print("Você perdeu! A palavra era:", palavras)
            break  # O `break` estava no lugar errado antes

    if "_" not in resultado:  # Se não há mais "_" no resultado, o jogador venceu
        print(palavras)
        print("Você ganhou!")
        break
