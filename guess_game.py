import random

def jogar_adivinhacao():

    for i in range(1,21):
        print("*",end = "")

    print("\nJogo da adivinhacao")

    for i in range(1,21):
        print("*",end = "")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    print("\nNivel de dificuldade: \n1)Facil \n2)Medio\n3)Dificil\n")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        exit()

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!!!!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.\n")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")
