from random import seed, randint
import numpy as np
import utils

memoriaVirtual = []
listaAcessos = []


class Pagina:
    def __init__(self, idProc, nroPag):
        seed()
        self.id = randint(1000, 9999)
        self.idProc = idProc
        self.isAloc = False

    def updateAloc(self, isAloc, pos):
        self.isAloc = isAloc
        self.posFisica = pos

def memoriaVirtualPagAloc(listaProc, memoriaVirtual):
    x = 0
    for i in range(len(listaProc)):
        for j in range(listaProc[i].qtdPag):
            memoriaVirtual[x] = Pagina(listaProc[i].id, x)
            x = x+1
    return memoriaVirtual


def paginacaoAleatoria(listaProc):
    listaDeAcesso = utils.listaDeAcessoAleatoriaV2()
    memoriaVirtual = utils.memoriaVirtualInit2()
    memoriaFisica = utils.memoriaFisicaInitV2()


    # index = 0
    # tam = int(abs(contPag(listaProc)/4))
    # print('\n')
    # for i in range(tam):
    #     print("Index lista de acessos: "+str(index) +
    #           " - Id da pagina: " + str(listaDeAcesso[i].id) +
    #           " - Posição memória física: "+str(i))
    #     listaDeAcesso[i].updateAloc(True, i)
    #     memoriaFisica[i] = listaDeAcesso[i]
    #     index += 1

    # while (index < len(listaDeAcesso)):
    #     pos = randint(0, len(memoriaFisica))
    #     if (listaDeAcesso[index].isAloc == False):
    #         listaDeAcesso[pos].updateAloc(True, listaDeAcesso[pos])
    #         memoriaVirtual[pos] = listaDeAcesso[index]

    #     print("Index lista de acessos: "+str(index) +
    #           " - Id da pagina: " + str(listaDeAcesso[index].id)+
    #           " - Posição memória física: "+str(pos))

    #     index += 1
