import numpy

class MatrizA(Matriz):

    def __init__(self, argv):
        if len(argv) >= 2:
            self.M = numpy.zeros((argv[0],argv[0]))
            if argv[1] == "uniforme":
                self.uniforme()
            if argv[1] == "array" and len(argv) >= 3:
                self.array(argv[2])
        else:
            print "Quantidade incorreta de argumentos" 
            
    def uniforme(self):
        for index, value in numpy.ndenumerate(self.M):
            self.M[index] = numpy.random.uniform(0, 1)

    def array(self, entrada):
        for index, value in numpy.ndenumerate(self.M):
            self.M[index] = entrada[index]
            
    def getM(self):
        return self.M
    
    def getTam(self):
        return len(self.M[0])
