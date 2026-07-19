#%%
#Importação das bibliotecas.
import pandas as pd 

df = pd.read_csv("Copa-do-Mundo-da-FIFA-2026.csv", index_col= False, sep= ";")
df

#%%

print("📊Desempenho das equipes")

#%%

print("Qual seleção fez mais pontos?")
df.nlargest(1, "Pts")[["Equipes", "Pts"]].style.hide(axis="index")

#%%

print("Quais seleções terminaram invictas?")
df[df["DER"] == 0][["Equipes", "PJ", "VIT", "E", "DER"]].style.hide(axis="index")

#%%

print("Quais tiveram o pior desempenho?")
df.nsmallest(10, "Pts")[["Equipes", "Pts"]].style.hide(axis="index")

#%%

print("Quem venceu mais partidas?")
df.nlargest(10, "VIT")[["Equipes", "VIT"]].style.hide(axis="index")

#%%

print("Quem perdeu mais partidas?")
df.nlargest(10, "DER")[["Equipes", "DER"]].style.hide(axis="index")

#%%

print("⚽ Ataque e 🛡️ Defesa")

#%%

print("Melhor ataque")
df.nlargest(10, "GM")[["Equipes", "GM"]].style.hide(axis="index")

#%%

print("Melhor defesa")
df.nsmallest(10, "GC")[["Equipes", "GC"]].style.hide(axis="index")

#%%

print("Existe relação entre gols marcados e pontos?")
df[["GM", "Pts"]].corr().style.hide(axis="index")
#Se o valor estiver próximo de 1, existe uma forte relação positiva.

#%%

print("Melhor saldo de gols")
df.nlargest(10, "SG")[["Equipes", "SG"]].style.hide(axis="index")