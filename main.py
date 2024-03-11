#carrega o automato
from M1 import M1

# usar o automato
afd = M1()
fitas = ["ab","bba","abaaa"]
for fita in fitas:
    print(fita,":",afd.aceita(fita))