![ORF analysis github](https://github.com/user-attachments/assets/c2203cef-ac61-4a5b-a663-92a7aec176c7)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


# Análise de ORF: Similaridade e potencial de codificação de proteínas no DNA via Biopython
<h2> [EN] ORF (Open Reading Frame) Analyis: Similarity and potentially codification of proteins in DNA data analysis via Biopython</h2>

<p align="left">
  <a href="#english-translation">English Translation</a> •
  <a href="#sobre-o-projeto-de-pesquisa">Sobre o Projeto de Pesquisa</a> •
  <a href="#scripts-e-gráficos">Scripts e Gráficos</a> •
  <a href="#resultados">Resultados</a> •
  <a href="#apresentação-em-congresso">Apresentação em Congresso</a> •
  <a href="#socials">Socials</a> •
  <a href="#credits">Credits</a> 
</p>

## Sobre o Projeto de Pesquisa

A bioinformática permite a identificação de sequências codificantes e a anotação funcional de genomas. Neste estudo, uma ORF foi identificada no genoma do Ailuropoda melanoleuca e analisada através de ferramentas como o BLASTp para avaliar sua similaridade com proteínas conhecidas. O estudo revelou que a ORF codifica uma sequência proteica de 707 aminoácidos, com 99,86% de identidade a uma proteína hipotética do panda-gigante.

O genoma de A. melanoleuca, obtido pela database internacional pública NCBI, foi processado utilizando a biblioteca Biopython para identificação de ORFs. A maior sequência identificada foi traduzida em uma proteína e submetida a uma busca por similaridade no banco de dados nr (non-redundant) do NCBI, utilizando BLASTp. Foram analisados a identidade da sequência, a cobertura do alinhamento e a presença de domínios conservados. 

## Scripts e Gráficos

Dentro do projeto, além do script para análise de ORFs, scripts com outras funcionalidades biológicas também foram feitos, visando a visualização dos dados obtidos e comparação com também já existentes em databases internacionais. São esses:

- Script de Análise ORF: O protagonista do estudo. Foi utilizado para identificar, dentro do genoma ".fasta", possíveis sequências proteicas codificantes para proteínas conhecidas. Completamente estruturado em Biopython, a biblioteca foi essencial para os resultados por conter funções eficientes para as identificações desejadas (orf_pattern, longest_orf e orf_seq).
    Confira [aqui](https://github.com/chiarxw/ORF_Analysis/blob/main/scripts/ORF_Genome_Analysis/orf_genoma_panda.py)!

- Script de Contagem de Sequências: Feito com o objetivo de contar quantas vezes uma sequência X de bases nitrogenadas aparece no genoma (sejam essas códons ou sequências aleatórias - e sem número específico de caracteres (bases)). Utilizou principalmente Biopython, junto de pandas e matplotlib para posterior geração de gráficos. Junto dele, foi feito um script de gráficos para contagem de bases nitrogenadas ACTG em toda integridade do genoma.
    Confira ambos [aqui](https://github.com/chiarxw/ORF_Analysis/tree/main/scripts/Frequency_of_Nitrogenous_Bases)!

- Script de Contagem de Conteúdo GC: Utilizando o mesmo script de contagem de sequências anterior, foi gerado um gráfico para análise exclusiva da frequência de bases Guanina e Citosina (GC) no genoma. Feito em Biopython, pandas e matplotlib.
    Confra [aqui](https://github.com/chiarxw/ORF_Analysis/blob/main/scripts/Counting_GC_Content/gr%C3%A1fico_varia%C3%A7%C3%A3o_gc_panda.py)!

- Gráficos: Todos os scripts anteriormente apresentados geraram gráficos visuais para interpretação e visualização dos dados. Confira o resultado deles [aqui](https://github.com/chiarxw/ORF_Analysis/tree/main/graphics)!

## Resultados

- ORF identificada com 707 aminoácidos.

- 99,86% de identidade com proteína hipotética de Ailuropoda melanoleuca.

- E-value = 0, indicando alinhamento altamente significativo.

- Nenhum domínio conservado detectável, sugerindo uma função ainda pouco caracterizada. Futuros estudos podem caracterizar as funções da proteína encontrada.

## Apresentação em Congresso

Os resultados deste estudo serão apresentados em dois congressos brasileiros: [Congresso Brasileiro de Biotecnologia Aplicada (CONBIOTEC)](https://ime.events/v-conbiotec) e [Congresso Brasileiro de Ciências Biológicas (CONBRACIB)](https://ime.events/vi-conbracib). Confira o E-Banner apresentado em um destes:

![E-banner IDENTIFICAÇÃO DE UMA ORF E ANÁLISE DE SIMILARIDADE PROTEICA EM Ailuropoda melanoleuca por Chiara Brancalion2 - VI CONBRACIB](https://github.com/user-attachments/assets/01d7f63a-551a-4662-ac3e-c8d994375905)

## English Translation

<h2> About the Research Project </h2>
Bioinformatics enables the identification of coding sequences and the functional annotation of genomes. In this study, an ORF was identified in the genome of Ailuropoda melanoleuca and analyzed using tools such as BLASTp to evaluate its similarity to known proteins. The study revealed that the ORF encodes a protein sequence of 707 amino acids, with 99.86% identity to a hypothetical protein of the giant panda.

The genome of A. melanoleuca, obtained from the publicly available international NCBI database, was processed using the Biopython library to identify ORFs. The largest identified sequence was translated into a protein and subjected to a similarity search against the NCBI nr (non-redundant) database using BLASTp. Sequence identity, alignment coverage, and the presence of conserved domains were analyzed.

<h2> Scripts and Graphs </h2>
Within the project, in addition to the ORF analysis script, other scripts were developed to facilitate biological data visualization and comparison with existing sequences from international databases. These include:

- ORF Analysis Script: The core script of the study. It was used to identify potential protein-coding sequences in the ".fasta" genome file. Fully structured in Biopython, this library was essential for the results due to its efficient functions for ORF identification (orf_pattern, longest_orf, and orf_seq). [Check it out here!](https://github.com/chiarxw/ORF_Analysis/blob/main/scripts/ORF_Genome_Analysis/orf_genoma_panda.py)

- Sequence Count Script: Developed to count how many times a given sequence of nitrogenous bases (either codons or random sequences with no fixed length) appears in the genome. This script primarily used Biopython, along with pandas and matplotlib for subsequent graphical representation. Additionally, a separate script was created to generate graphs of nitrogenous base (A, C, T, G) counts across the entire genome. [Check them out here!](https://github.com/chiarxw/ORF_Analysis/tree/main/scripts/Frequency_of_Nitrogenous_Bases)

- GC Content Count Script: Using the same sequence count script mentioned earlier, a specific graph was generated to analyze the frequency of Guanine and Cytosine (GC) bases in the genome. Implemented using Biopython, pandas, and matplotlib. [Check it out here!](https://github.com/chiarxw/ORF_Analysis/blob/main/scripts/Counting_GC_Content/gr%C3%A1fico_varia%C3%A7%C3%A3o_gc_panda.py)

- Graphs: All the previously mentioned scripts generated visual graphs to aid in data interpretation and visualization. [See the results here!](https://github.com/chiarxw/ORF_Analysis/tree/main/graphics)

<h2> Results </h2>
- Identified ORF with 707 amino acids.
- 99.86% identity with a hypothetical Ailuropoda melanoleuca protein.
- E-value = 0, indicating a highly significant alignment.
- No detectable conserved domains, suggesting a poorly characterized function. Future studies may help characterize the function of the identified protein.

<h2> Conference Presentation </h2>
The results of this study will be presented at two Brazilian conferences:

- Brazilian Congress of Applied Biotechnology (CONBIOTEC)
- Brazilian Congress of Biological Sciences (CONBRACIB)

## Socials
> LinkedIn [Chiara Brancalion](https://www.linkedin.com/in/chiara-brancalion-5263412a0) &nbsp;&middot;&nbsp;
> GitHub [@chiarxw](https://github.com/chiarxw)

---

## Credits

This repository uses the following open source information and packages:

- [NCBI Database](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_002007445.2/)
- [NCBI BLASTp](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
- [Python](https://www.python.org/)
- [Biopython](https://biopython.org/)
- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/index.html)
- [R](https://www.r-project.org/)
- [Ileriayo Markdown Badges](https://github.com/Ileriayo/markdown-badges)
- [README Template](https://github.com/amitmerchant1990)
