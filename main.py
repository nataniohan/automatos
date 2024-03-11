#carrega o automato
from M1 import M1
from M1 import M2
# usar o automato
afd = M1()
fitas = ["ab","bba","abaaa"]
for fita in fitas:
    print(fita,":",afd.aceita(fita))
    
print()
af = M2()
fitas2 = ["abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba","aba", "aa", "aaaaaaaaaaaaaa"]
for fita in fitas2:
    print(fita,":",af.aceita(fita))
    