from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Bioinformatics\BioPython\ailuropoda_melanoleuca.fa"
seq_record = next(SeqIO.parse(file_path, "fasta"))
sequence = str(seq_record.seq)

base_counts = {base: sequence.count(base) for base in "ATCG"}

df = pd.DataFrame(list(base_counts.items()), columns=["Base", "Frequência"])

plt.bar(df["Base"], df["Frequência"], color=["blue", "green", "red", "orange"])
plt.xlabel("Bases Nitrogenadas") ## frequência de todas as bases nitrogenadas (A, C, T, G) sem especificidade a uma base X
plt.ylabel("Frequência")
plt.title("Frequência das Bases Nitrogenadas no Genoma do Panda")
plt.show() ## visualização dos resultados via gráfico de barras