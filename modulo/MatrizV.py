import numpy
import math
#from MatrizA import MatrizA

class MatrizV(Matriz):

    def __init__(self, argv):
    #recebera uma lista de vetores de mesmo tamanho argv (lista de listas)
        self.TESTE = True;
        entrada = numpy.array(argv)
        centralizada = self.centraliza(entrada)
        unitarizada = self.unitariza(centralizada)
        self.M = self.geraM(unitarizada)
            
    def unitariza(self, centralizada):
        retorno = numpy.empty(len(centralizada), dtype=list) 
        i = 0
        for vetor in centralizada:
            norma = 0.0
            for valor in vetor:
                norma += valor*valor
            norma = math.sqrt(norma)
            vetor /= norma
            if self.TESTE:
                print "unitarizada: vetor", i
                print vetor
                print ""
            retorno[i] = vetor
            i += 1
        return retorno 
    
    def geraM(self, unitarizada):
        """
            corr(vi, vj) = vi . vj
        """
        matriz = numpy.zeros((len(unitarizada), len(unitarizada)))
        i = 0;
        for v1 in unitarizada:
            j = 0
            for v2 in unitarizada:
                if (i != j):
                    matriz[i][j] = matriz[j][i] = numpy.dot(v1, v2)
                else:
                    matriz[i][j] = matriz[j][i] = 1
                j += 1
            i += 1
        return matriz
    
    def centraliza(self, entrada):
        retorno = numpy.empty(len(entrada), dtype=list) 
        i = 0
        for vetor in entrada:
            soma = sum(vetor)
            if(soma != 0):
                media = soma / len(vetor)
                vetor -= media
            else:
                pass
            retorno[i] = vetor
            i += 1
        if self.TESTE:
            print "centralizada:"
            print retorno
            print ""

        return retorno;

    def getM(self):
        return self.M
    
    def getTam(self):
        return len(self.M[0])
