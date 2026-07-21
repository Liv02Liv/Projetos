#%%

import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("Copa-do-Mundo-da-FIFA-2026.csv", index_col= False, sep= ";")
df

#%%

print("Pontos por equipe")
df.sort_values("Pts", ascending=False).plot(
    x="Equipes",
    y="Pts",
    kind="bar",
    figsize=(12,5)
)

plt.show()

#%%

print("Gols marcados")
df.sort_values("GM", ascending=False).plot(
    x="Equipes",
    y="GM",
    kind="bar",
    figsize=(12,5)
)

plt.show()

#%%

print("Gols sofridos")
df.sort_values("GC").plot(
    x="Equipes",
    y="GC",
    kind="bar",
    figsize=(12,5)
)

plt.show()

#%%

print("Dispersão: Pontos × Gols Marcados")
df.plot.scatter(
    x="GM",
    y="Pts",
    figsize=(7,5)
)

plt.show()

#%%

print("Dispersão: Pontos × Saldo de Gols")
df.plot.scatter(
    x="SG",
    y="Pts",
    figsize=(7,5)
)

plt.show()

#%%