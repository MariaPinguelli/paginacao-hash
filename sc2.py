import utils

class Pagina:
    def __init__(self, idPagina, mrIndex):
        self.idPagina = idPagina
        self.mrIndex = mrIndex
        self.bitAcesso = 1
    
    def updateAcesso(self):
        self.bitAcesso = 0
    
    def updateMrIndex(self, mrIndex):
        self.mrIndex = mrIndex

def verificaIsAloc(idPag, memoriaReal):
    return False

def printAloc(idPag, index, i):
    print("\n")
    print("Pagina ------------------------ " + str(idPag))
    print("Endereco na Memoria Virtual --- " + str(index))
    print("Endereco na Memoria Real ------ " + str(i))

def findVirtualIndex(idPag, lista):
    return [0, 0]

def runPaginacaoSC2():
    listaDeAcesso = utils.listaDeAcessoAleatoria()