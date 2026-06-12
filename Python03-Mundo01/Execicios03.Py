import math 
import random 
import pygame
num = float(input("Digite um numero: "))
poni = math.trunc(num)
print(f"A porcao inteira desse numero é: {poni}")
#Atividade01
print("=" * 30)
co = int(input("Digite o lado oposto: "))
ca = int(input("Digite o lado adjacente: "))
hipotenusa = math.sqrt(co ** 2 + ca ** 2)
print(f"A hipotenusa desse triangulo é: {hipotenusa}")
#Atividade02
angulo = int(input("Digite o angulo: "))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f"O seno desse angulo é {seno}, o cosseno é {cosseno} e a tangente é {tangente}")
#Atividade03
part = []
qtd = int(input("Quantas pessoas vão participar do sorteio? "))
for i in range(qtd):
    nome = input(f"Digite o nome do participante {i+1}:")
    part.append(nome)
escolhido = random.choice(part)
print(F"O escolhido foi: {escolhido}")
#Atividade04
part = []
qtd = int(input("Quantas pessoas vão participar do sorteio? "))
for i in range(qtd):
    nome = input(f"Digite o nome do participante {i+1}:")
    part.append(nome)
random.shuffle(part)
print("Ordem sorteada dos participantes:")
for i, nome in enumerate(part, start=1):
    print(f"{i}º lugar: {nome}")
#Atividade05
# inicializa o mixer de áudio
pygame.mixer.init()

# carrega o arquivo mp3
pygame.mixer.music.load("Luiza Martins - Tailândia (Ao Vivo) #NostalgiaPura.mp3")

# toca
pygame.mixer.music.play()

# mantém o programa rodando até a música terminar
while pygame.mixer.music.get_busy():
    pass