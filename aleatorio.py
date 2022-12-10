from random import seed, randint
import numpy as np
from utils import contPag, memoriaFisicaInit, memoriaVirtualInit

memoriaVirtual = []
listaAcessos = []

class Pagina: 
    def __init__(self, proc, nroPag):
        seed()
        self.idProc = proc.id
        self.id = nroPag


def paginacaoAleatoria(listaProc):
    memoriaFisica = memoriaFisicaInit(listaProc)
    memoriaVirtual = memoriaVirtualInit(listaProc)
    print("Mem fisica: " + str(memoriaFisica))
    print("Mem vir: " + str(memoriaVirtual))
    
# Cria as páginas referentes ao processo
def criaPaginas(listaProc):
    totalPaginas = 0
    for processo in listaProc:
        nroPagina = 1
        for pagina in range(processo.qtdPag):
            memoriaVirtual = Pagina(processo, nroPagina)
            nroPagina+1
            totalPaginas+1
    gerarListaAcessos(memoriaVirtual, totalPaginas)

# Cria a lista de acessos que a memória física deve fazer na memória virtual
def gerarListaAcessos(memoriaVirtual, totalPaginas):
    print("Mem vir: " + len(memoriaVirtual))
    # print("Qtde pgs: " + str(totalPaginas))
    # qtdAcessos = randint(10, totalPaginas)
    # print("Qtde acessos: " + str(qtdAcessos))
    # listaAcessos = np.random.choice(memoriaVirtual, qtdAcessos)
    # print(listaAcessos)