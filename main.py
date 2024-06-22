# from bio import sequencia
# sequencia = Sequencia("ATCG")
# print(sequencia)


## ler um arquivo fasta

from bio.ler_fasta import ler_fasta

organismos = ler_fasta("./arquivos/Flaviviridae-genomes.fasta")
print(organismos)