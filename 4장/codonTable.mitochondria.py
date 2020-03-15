from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"] #미토콘드리아가 사용하는 코돈
print(codon_table)