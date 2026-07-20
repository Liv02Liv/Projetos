#%%
#Importação das bibliotecas.
import pandas as pd 

df = pd.read_csv("Copa-do-Mundo-da-FIFA-2026.csv", index_col= False, sep= ";")
df

#%%

print("1. Desempenho das equipes")

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

print("2. Ataque e defesa")

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

#%%

print("3. Eficiência")

#%%

df["Aproveitamento (%)"] = (df["Pts"] / (df["PJ"] * 3)) * 100

df["GM/Jogo"] = df["GM"] / df["PJ"]

df["GC/Jogo"] = df["GC"] / df["PJ"]

df["Pts/Jogo"] = df["Pts"] / df["PJ"]

df["SG/Jogo"] = df["SG"] / df["PJ"]

df 

#%%

print("4. Comparações")

#%%

print("Quem venceu mais também marcou mais gols?")
df.sort_values(["VIT", "GM"], ascending=False)[["Equipes", "VIT", "GM"]].style.hide(axis="index")

#%%

print("Correlação entre saldo de gols e pontos")
df[["SG", "Pts"]].corr().style.hide(axis="index")

#%%

print("Média de gols das 10 melhores equipes")
top10 = df.nlargest(10, "Pts")
top10["GM"].mean()