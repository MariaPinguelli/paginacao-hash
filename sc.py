# Imports
from random import seed, randint
from utils import contPag, memoriaFisicaInit, memoriaVirtualInit, listaDeAcessoAleatoria

class Pagina:
    def __init__(self, idProc, pos):
        seed()
        self.id = randint(1000, 9999)
        self.idProc = idProc
        self.isAloc = False
        self.bitAcesso = 1
        self.endV = pos
        
    def updateAloc(self, isAloc, pos):
        self.isAloc = isAloc
        self.posFisica = pos
    
    def updateBit(self, bit):
        self.bitAcesso = bit

def memoriaVirtualPagAloc(listaProc, memoriaVirtual):
    tamMem = len(memoriaVirtual)
    
    x = 0
    for i in range(len(listaProc)):
        for j in range(listaProc[i].qtdPag):
            memoriaVirtual[x] = Pagina(listaProc[i].id, x)
            x = x+1
    return memoriaVirtual

def paginacaoSC(listaProc):
    
    memoriaFisica = memoriaFisicaInit(listaProc)
    memoriaVirtual = memoriaVirtualInit(listaProc)
    memoriaVirtual = memoriaVirtualPagAloc(listaProc, memoriaVirtual)
    listaDeAcesso = listaDeAcessoAleatoria(memoriaVirtual)
    
    # global index
    index = 0
    tam = int(abs(contPag(listaProc)/4))
    for i in range(tam):
        memoriaVirtual[listaDeAcesso[i]].updateAloc(True, i)
        memoriaVirtual[listaDeAcesso[i]].updateBit(1)
        memoriaFisica[i] = memoriaVirtual[listaDeAcesso[i]]
        index += 1
        
    while(index < len(listaDeAcesso)):
        # print("Memoria Fisica")
        # print(memoriaFisica)
        print("Index: "+str(index)+" - Id da pagina: "+ str(memoriaFisica[0].id)+" - Bit de Acesso: "+str(memoriaFisica[0].bitAcesso))
        if memoriaFisica[0].bitAcesso == 1:
            memoriaFisica[0].updateBit(0)
            listCopy = memoriaFisica
            memoriaFisica[len(memoriaFisica)-1] = listCopy[0]
            for i in range(len(memoriaFisica)-1):
                memoriaFisica[i] = listCopy[i+1]
                
        elif memoriaFisica[0].bitAcesso == 0:
            memoriaVirtual[memoriaFisica[0].endV].updateAloc(False, None)
            
            listCopy = memoriaFisica
            memoriaFisica[len(memoriaFisica)-1] = listCopy[0]
            for i in range(len(memoriaFisica)-1):
                memoriaFisica[i] = listCopy[i]
            
            memoriaVirtual[listaDeAcesso[index]].updateAloc(True, index)
            memoriaVirtual[listaDeAcesso[index]].updateBit(1)
            memoriaFisica[len(memoriaFisica)-1] = memoriaVirtual[listaDeAcesso[index]]
            
        index += 1
        