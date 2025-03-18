from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Bioinformatics\BioPython\ailuropoda_melanoleuca.fa"
seq_record = next(SeqIO.parse(file_path, "fasta"))
sequence = str(seq_record.seq)

base_counts = {base: sequence.count(base) for base in "ATCG"} ## contagem das bases nucleotídicas

df = pd.DataFrame(list(base_counts.items()), columns=["Base", "Frequência"]) ## definir dataframe do gráfico (base X frequência)

window_size = 1000
gc_content = []

for i in range(0, len(sequence) - window_size, window_size):
    window_seq = sequence[i : i + window_size]
    gc_count = window_seq.count("G") + window_seq.count("C")
    gc_content.append(gc_count / window_size) ## contagem apenas da frequência das Guaninas e Citosinas no genoma

plt.plot(gc_content, color="green")
plt.xlabel("Janela no Genoma")
plt.ylabel("Conteúdo GC (%)")
plt.title("Variação do Conteúdo GC ao Longo do Genoma do Panda")
plt.show() ## resultado do gráfico em barras