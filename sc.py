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
    if len(memoriaReal) == 0: return False
    for i in range(len(memoriaReal)):
        if memoriaReal[i].idPagina is idPag:
            return True
    return False

def printAloc(idPag, index, i):
    print("\n")
    print("Pagina ------------------------ " + str(idPag))
    print("Endereco na Memoria Virtual --- " + str(index))
    print("Endereco na Memoria Real ------ " + str(i))

def findVirtualIndex(idPag, lista):
    print("start ---------------------------------------------")
    print("Looking for: " + str(idPag))
    print("Lista len: "+ str(len(lista)))
    for i in range(len(lista)):
        print("Lista[ "+str(i)+" ] len: "+str(len(lista[i])))
        if len(lista[i]) > 0:
            for j in range(len(lista[i])):
                if lista[i][j].idPagina == idPag:
                    print("Found: " + str(lista[i][j].idPagina))
                    print("end ---------------------------------------------")
                    return [i, j]
    print("end ---------------------------------------------")
    return [0, 0]

def runPaginacaoSC():
    listaDeAcesso = utils.listaDeAcessoAleatoria()
    
    mrLen = utils.tamMemoriaReal
    memoriaVirtual = [[]] * utils.tamMemoriaVirtual
    memoriaReal = [] * mrLen
    
    print("TAM memoriaVirtual: "+str(len(memoriaVirtual)))
    for k in range(len(memoriaVirtual)):
        print("memoriaVirtual - pos "+str(k)+" tam "+str(len(memoriaVirtual[k])))  
    
    print("ALGORITMO SC - SECOND CHANCE")
    
    indice = 0
    while ((indice < mrLen) & (indice < len(listaDeAcesso))):
        idPag = listaDeAcesso[indice]
        if verificaIsAloc(idPag, memoriaReal) is False:
            index = utils.hashEnderecoV2(idPag)
            memoriaVirtual[index].append(Pagina(idPag, indice))
            print("LINHA 62: TAM memoriaVirtual: "+str(len(memoriaVirtual)))
            for k in range(len(memoriaVirtual)):
                print("memoriaVirtual - pos "+str(k)+" tam "+str(len(memoriaVirtual[k])))
            memoriaReal.append(Pagina(idPag, indice))
            printAloc(idPag, index, indice)
        indice+=1
        
    print("TAM memoriaVirtual: "+str(len(memoriaVirtual)))
    for k in range(len(memoriaVirtual)):
        print("memoriaVirtual - pos "+str(k)+" tam "+str(len(memoriaVirtual[k])))        
    
    i = mrLen
    while i < len(listaDeAcesso):
        idPag = listaDeAcesso[i]
        if verificaIsAloc(idPag, memoriaReal) is False:
            index = utils.hashEnderecoV2(idPag)
            memoriaVirtual[index].append(Pagina(idPag, i))
            
            if memoriaReal[0].bitAcesso == 0:
                deletePagIndex = findVirtualIndex(memoriaReal[0].idPagina, memoriaVirtual)
                memoriaVirtual[deletePagIndex[0]].remove(memoriaVirtual[deletePagIndex[0]][deletePagIndex[1]])
                
                # Atualizar index alocados
                for j in range(utils.tamMemoriaReal-1):
                    auxIndexes = findVirtualIndex(memoriaReal[j].idPagina, memoriaVirtual)
                    memoriaVirtual[auxIndexes[0]][auxIndexes[1]].updateMrIndex(j)
                    memoriaReal[j].updateMrIndex(j)
                
                memoriaReal.append(Pagina(idPag, len(memoriaReal)-1))
                printAloc(memoriaReal[len(memoriaReal)-1].idPagina, index, memoriaReal[len(memoriaReal)-1].mrIndex)
            else:
                print("SEGUNDA CHANCE PARA A PAGINA: " + str(memoriaReal[0].idPagina))
                aux = memoriaReal[0]
                aux.updateAcesso()
                aux.updateMrIndex(len(memoriaReal)-1)
                memoriaReal.pop(0)
                for j in range(utils.tamMemoriaReal-1):
                    memoriaReal[j].updateMrIndex(j)
                memoriaReal.append(aux)
                i-=1
        i+=1        