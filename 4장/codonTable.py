from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_rna_by_name["Standard"]
print(codon_table)