import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np ## importação das bibliotecas necessárias (main: matplotlib)

especies = ["Ailuropoda melanoleuca", "Canis lupus", "Felis catus", "Ursus arctos"]
identidade = [99.86, 87, 80, 90]
cores = ["#2ca02c", "#1f77b4", "#d62728", "#9467bd"]  ## comparação das espécies (com base em dados do BLASTp) / divisãodo gráfico por cores

sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
bars = plt.bar(especies, identidade, color=cores, edgecolor="black") ## estilo e tamanho do gráfico

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5,
             f"{bar.get_height()}%", ha='center', fontsize=12, color="white", fontweight="bold") ## estilização das legendas

plt.ylim(0, 105)  ## altura do gráfico
plt.ylabel("Identidade (%)", fontsize=14)
plt.xlabel("Espécie", fontsize=14)
plt.title("Identidade Proteica com a ORF Predita", fontsize=16, fontweight="bold") ## legendas

plt.show() ## exibição do gráfico em barras