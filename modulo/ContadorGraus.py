import numpy
#from MyLimiar import Limiar
#from MatrizA import MatrizA

class ContadorGraus(object):

    def __init__(self):
        pass
    
    def execute(self, matriz):
        #verificar tipos
        if isinstance(matriz, Matriz):
            n = matriz.getTam()
            m = matriz.getM()
            l = numpy.zeros(n)
            for x in range(n):
                valor = 0
                for y in range(n):
                    valor += m[x][y]
                for y in range(n):
                    valor += m[y][x]
                valor -= m[x][x]
                l[x] = valor / (2 * n - 1) #tratar 0 depois
            return l
            
