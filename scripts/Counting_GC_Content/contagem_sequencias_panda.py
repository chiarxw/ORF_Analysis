from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt ## bibliotecas necessárias (main: SeqIO = contagem de sequências nucleotídicas)

file_path = r"C:\Bioinformatics\BioPython\Genomas\ailuropoda_melanoleuca.fa"
seq_record = next(SeqIO.parse(file_path, "fasta"))
sequence = str(seq_record.seq) ## identificação do genoma na base de dados

base_counts = {base: sequence.count(base) for base in "ATCG"} ## contagem de bases

df = pd.DataFrame(list(base_counts.items()), columns=["Base", "Frequência"]) ## criar dataframe

window_size = 1000
gc_content = []

for i in range(0, len(sequence) - window_size, window_size):
    window_seq = sequence[i : i + window_size]
    gc_count = window_seq.count("G") + window_seq.count("C")
    gc_content.append(gc_count / window_size) ## genoma em janelas

import re

motivo = "TATAAA" ## sequência X de bases
posicoes = [m.start() for m in re.finditer(motivo, sequence)]

print(f"O motivo '{motivo}' foi encontrado {len(posicoes)} vezes.")
print(f"Posições: {posicoes[:10]} ...")  # exibir apenas algumas posições

## ------------ RESULTADOS ------------------

## O motivo 'TATAAA' foi encontrado 94383 vezes.
## Posições: [6882, 7358, 8812, 10630, 11709, 11781, 12308, 17319, 18936, 44049] ...
## obs.: sequência 'TATAAA' não foi baseada em nenhum critério e o script pode ser utilizado para qualquer sequência X de bases.