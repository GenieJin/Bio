from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

tatabox_seq =  Seq("tataaaggcAATATGCAGTAG", IUPAC.unambiguous_dna) #IUPAC를 사용해 DNA 서열임을 알려줌
print(tatabox_seq)
print(type(tatabox_seq))