import forca
import guess_game

for i in range(1,21):
    print("*",end = "")

print("\n*Escolha o seu jogo*")

for i in range(1,21):
    print("*",end = "")

print("\n1) Forca\n2) Adivinhacao")
jogo = int(input("Digite o jogo: "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogo_forca()
elif(jogo == 2):
    print("Jogando Adivinhacao")
    guess_game.jogar_adivinhacao()