#%%
import pandas as pd

print("=" * 60)
print("SUPERMERCADO - CAIXA 01".center(50))
print("=" * 60)
print("Digite o codigo do produto e pressione a tecla Entre.")
print("Digite 'F' para finalizar a compra.")

print("-" * 60)

dados = {
    "Código": ["001", "002", "003", "004", "005", "006", "007", "008"],
    "Produto": [
        "Arroz 5kg",
        "Feijão 1kg",
        "Macarrão 500g",
        "Óleo de Soja 500ml",
        "Açúcar 1kg",
        "Café 500g",
        "Leite 1l",
        "Sabonete"],
    "Preço": [24.90, 8.50, 4.30, 7.28, 5.10, 15.98, 4.80, 2.50]
}

df = pd.DataFrame(dados).set_index("Código")

print(df)

print("-" * 60)
print("Digite o código do produto (F para finalizar):\n")

carrinho = []

while True:
    codigo = input("Digite o código do produto (F para finalizar): ")
    
    if codigo.upper() == "F":
        print("\nFim Da Compra!\n")
        break
    if codigo in df.index:
        carrinho.append(codigo)
        print(f"Adicionado: {df.loc[codigo, 'Produto']} - R$ {df.loc[codigo, 'Preço']:.2f}")
    else:
        print("Produto não encontrado.")

total = 0

for codigo in carrinho:
    total += df.loc[codigo, "Preço"]

print(f"SubTotal: R$ {total:.2f}\n")