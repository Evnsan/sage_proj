import random

class Limiar(object):
    
    def __init__(self):
        self.dist = 1
        self.nextValue = 0.8
        
    def next(self):
        if self.dist == 1:
            return self.constante()
        elif self.dist == 2:
            return self.uniforme()
        else:
            pass

    def setDist(self , *argv):
        if argv[0] == 'constante':
            self.dist = 1
            self.setConstante(argv[1])
        elif argv[0] == 'uniforme':
            self.nextValue = random.uniform(0, 1)
            self.dist = 2
        else:
            pass
    
    def constante(self):
        return self.nextValue
        
    def setConstante(self, value):
        self.next = value

    def uniforme(self):
        retorno = self.nextValue
        self.nextValue = random.uniform(0, 1)
        return retorno
