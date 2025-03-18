## como detectar ORFs (open reading frames) no genoma
## passo 1 -> procurar pelo códon de início (ATG)
## passo 2 -> verificar se há um código de parada válido (TAA, TAG, TGA)
## passo 3 -> extrair e traduzir a ORF

from Bio import SeqIO
from Bio.Seq import Seq
import re

file_path = "C:/Bioinformatics/BioPython/ailuropoda_melanoleuca.fa"
seq_record = next(SeqIO.parse(file_path, "fasta"))
sequence = str(seq_record.seq)

orf_pattern = re.compile(r'ATG(?:[ATGC]{3}){30,}?(?:TAA|TAG|TGA)')
orfs = orf_pattern.findall(sequence) ## procurar padrão(ões) de ORFs no genoma

if orfs:
    longest_orf = max(orfs, key=len)  
    orf_seq = Seq(longest_orf)  ## transformar ORF mais longa em SEQ (sequência)

    print("ORF Encontrada:", orf_seq[:60] + "...")  ## mostrar apenas os 60 primeiros nucleotídeos

    protein = orf_seq.translate(table=1)  ## tradução do DNA por tabela padrão (table=1) -> maioria dos organismos, sem especificidade de indivíduo
    print("Sequência Proteica:", protein[:60] + "...")  ## mostrar apenas os 60 primeiros aminoácidos

    with open("proteina_panda.fasta", "w") as f:
        f.write(f">Proteina_Panda\n{protein}") ## salva proteína encontrada/separada em um novo arquivo .FASTA

    print("Arquivo proteina_panda.fasta salvo com sucesso!")
else:
    print("Nenhuma ORF longa encontrada.")

## ------------ RESULTADOS ------------------

## >Proteina_Panda
## MLHRLEPEKGPHPPTSLAPLEIVPFETASPQAQVDQEGPGNLSPLLPPAAPPPAPLEEAPRVQLSKGSPEREDSARNSRTNPYIDQLKSKGSPGTPRLCQEEEASLGQSEKQNSKNAAPEGKGSGFQSPTREVEVSPQGEGDVAHSVQEPSDCDEDETVTDIAQHGLEMVEPWEEPQWVTSPLHSPTLKDMQEAQVQGHRLEKRLPHRPSLRQSHSLDSKTTTVKSQWTLEAPSSSSCANLEAERNSDPLQPLAPRREIIGWEEKTPRSFREFSGPKGTEAVPSQKGPGGLQPKPAEISPVILAEGKELGTHQGHSSPQIEQGSVPGPDNSKESSPSLQDSASRGEHPPKLQLKSTECGPPKGKNRPSSLNLDSAIPITDLFRFDNVASFGSPGMQLSEPGDTKVTWMTSSHCKVDPWSICSQDPQDLDIVAHALTGRRNSAPVSVSAVRTSFMVKMCQARAVPVIPPKIQYTQIPQPLPSQSSGDSGVQPLERSQEEPSSTGEPSQKSAREDSLSLESPKEEKPKQDTGAIDSLPMDTTTSHMCEGPTLSPEPVLANLLSTQDATVQCRKRTSETEPSGDNLLSSKIERPSGGSKPFHRSRPGRPQSLILFSPPFPIMDHPPPSSTVTDSKVLLSPIRSPTQTVSPGLLCGDLAENTWVTPEGVTLRNKMTIPKNGQRLETSTSCFYQPQRRSVILDGRSGRQIE*
## * = códon de parada

## comparar a sequência via BLASTp (NCBI BLASTp) para verificar se a proteína é conhecida e qual sua função.