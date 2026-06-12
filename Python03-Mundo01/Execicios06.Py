print("="*30)
cidade = input("Digite um nome de cidade: ").strip()

if cidade.title().startswith("Santo"):
    print("A cidade começa com 'Santo' ")
else:
    print("A cidade não começa com 'Santo' ")

#Atividadde02
print("="*30)
nome = input("Digite o seu nome completo:").strip()

if nome.title().startswith("Silva"):
    print("O seu nome contem 'Silva' ")
else:
    print("O seu nome não contem 'Silva' ")

#Atividade03
print("="*30) 
partes = nome.title().split()
primeiro = partes[0]
ultimo = partes[-1]
print(f"Primeiro nome = {primeiro}")
print(f"Último nome = {ultimo}")
          