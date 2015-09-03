import numpy
#from MyLimiar import Limiar
#from MatrizA import MatrizA

class Limiarizador(object):

    def __init__(self):
        pass
    
    def execute(self, matriz, limiar):
        #verificar tipos
        m = matriz.getM()
        n = matriz.getTam()
        l = numpy.zeros((n,n))
        lim = limiar.next() 
        for index, value in numpy.ndenumerate(m):
            if m[index] >= lim:
                l[index] = 1
            else:
                l[index] = 0
        return MatrizA([n, "array", l])
