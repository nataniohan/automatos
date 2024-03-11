#para implementar uma classe abstract 
from abc import abstractmethod, ABC

#CRIAR UMA CLASSE ABSTRCT EM PYTHON
class Automato(ABC):
    #DEFINIR O CONSTRUTOR EM PYTHON
    def __init__(self, aceitacao):
        #definir os atributos
        self.estado = 0
        self.aceitacao = aceitacao
     
    #definicao de um metodo abstrato em Python    
    @abstractmethod
    def f(self, estado,simbolo):
        pass
    
    #recebe a fita e muda de estado ate o final da palavra
    def aceita(self, fita):
        #inicializa o estado inicial
        self.estado = 0
        #percorrendo a fita e mudando de estado
        for simbolo in fita:
            self.estado = self.f(self.estado, simbolo)
       #ao terminar de ler a fita 
        return self.estado in self.aceitacao