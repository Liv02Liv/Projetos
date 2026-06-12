nome = str(input("Digite seu nome completo: "))
maiuscula = nome.upper()
minuscula = nome.lower()
espaco = len(nome.replace(" ", ""))
primeiroNome = nome.split()[0]
contaPrimeiro = len(primeiroNome)
print(f"\n {maiuscula}. \n {minuscula}. \n O nome contem {espaco} Letras. \n O Primeiro nome contem {contaPrimeiro} Letras.")