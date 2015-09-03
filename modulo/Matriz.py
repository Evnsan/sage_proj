class Matriz(object):

    def __init__(self, argv):
        if len(argv) >= 1:
            self.M = numpy.zeros((argv[0],argv[0]))
        else:
            print "Quantidade incorreta de argumentos" 
            
    def getM(self):
        return self.M
    
    def getTam(self):
        return len(self.M[0])
