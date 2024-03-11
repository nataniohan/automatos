#vamos usar a classe abstrata base
from automato import Automato

#Classe que represent um automato que reconhece a linguagem L= aba*|ba*ba
class M1(Automato):
    #construtor dessa classe
    def __init__(self):
        #construtor de superclasse, passando o conjunto de estado de aceitacao
        super().__init__([2, 5])
    
    #implementar a funcao f
    def f(self, estado, simbolo):
        if estado == 0 and simbolo == 'a':
            return 1
        elif estado == 0 and simbolo == 'b':
            return 3
        elif estado == 1 and simbolo == 'b':
            return 2
        elif estado == 2and simbolo == 'a':
            return 2
        elif estado == 3 and simbolo == 'a':
            return 3
        elif estado == 3 and simbolo == 'b':
            return 4
        elif estado == 4 and simbolo == 'a':
            return 5
        return 6
                
class M2(Automato):
    #construtor dessa classe
    def __init__(self):
        #construtor de superclasse, passando o conjunto de estado de aceitacao
        super().__init__([3])
        
    #implementar a funcao f
    def f(self, estado, simbolo):
        if estado == 0 and simbolo == "a":
            return 1
        elif estado == 1 and simbolo == "b":
            return 1
        elif estado == 1 and simbolo == "a":
            return 3
        return 4