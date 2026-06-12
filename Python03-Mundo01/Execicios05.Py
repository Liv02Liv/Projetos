numero = str(input("Digite um numero de 0 á 9999: "))
numero = numero.zfill(4)
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print(f"\n Unidade: {unidade}\n Dezena: {dezena}\n Centena: {centena}\n Milhar: {milhar}")
