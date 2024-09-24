def menu():
    while True:
        print("--------------------")
        print("0 - Computador adivinha")
        print("1 - Jogador adivinha")
        print("2 - Sair")
        print("--------------------")

        option = int(input("Escolha a opção: "))

        if option == 0:
            computadorAdvinha()
        elif option == 1:
            jogadorAdvinha()
        elif option == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")
#binary sort nome do algoritmo 
def computadorAdvinha():
    low = 0
    high = 100

    while low <= high:
        num = (low + high) // 2
        answer = input(f"O número que pensou é maior do que {num}? (s/n): ")

        if answer == 's':
            low = num + 1  #como o numero que pensou é maior logo não é esse numero e somamos 1 para evitar o erro
        elif answer == 'n':
            high = num 
        else:
            print("Resposta inválida, por favor responda com 's' para sim ou 'n'.")
        
        if low == high:
            print(f"O número que você pensou é {low}!")
            break

def jogadorAdvinha():
    import random
    numero_secreto = random.randint(0, 100)
    tentativas = 0

    print("Tente adivinhar o número que estou pensando entre 0 e 100!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é maior!")
        elif palpite > numero_secreto:
            print("O número é menor!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

menu() #so chamamos o menu aqui pois ele ainda nao sabe o que é o jogadoradivinha e o computadoradivinha so depois de definir as funcoes 

