seq = "TATAAAGGCAATATGCAGTAG"
comp_dic = { 'A':'T', 'C':'G', 'G':'C', 'T':'A'}
comp_seq = ""
for s in seq : #서열에서 하나씩 읽어
    comp_seq += comp_dic[s] #상보적 염기 추가
revcomp_seq = comp_seq[::-1] #문자열을 뒤집어준다
print(comp_seq)
print(revcomp_seq)