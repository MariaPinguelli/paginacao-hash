# Imports
from random import seed, randint, choice
import utils

class Pagina:
    def __init__(self, id):
        seed()
        self.id = id
        self.mrIndex = None
        self.isAloc = False
        
    def updateAloc(self, isAloc, mrIndex):
        self.isAloc = isAloc
        self.mrIndex = mrIndex
        self.bitAcesso = 1
    
    def updateBit(self, bit):
        self.bitAcesso = bit

def verificaIsAloc(idPag, memoriaVirtual):
    for i in range(utils.tamMemoriaVirtual):
        if len(memoriaVirtual[i]) > 0:
            for j in range(len(memoriaVirtual[i])):
                if memoriaVirtual[i][j].isAloc == idPag & memoriaVirtual[i][j].isAloc:
                    return True
    return False

def memoriaVirtualPagAloc(listaDeAcesso, memoriaVirtual):
    tam = utils.tamMemoriaVirtual
    x = 0
    for i in range(tam):
        for j in range(listaDeAcesso[i].qtdPag):
            idPag = choice(listaDeAcesso)
            x = utils.hashEnderecoV2(idPag)
            memoriaVirtual[x] = Pagina(listaDeAcesso[j].id)
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
        print("Index lista de acessos: "+str(index)+" - Id da pagina: "+ str(memoriaFisica[0].id)+" - Bit de Acesso: "+str(memoriaFisica[0].bitAcesso))
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