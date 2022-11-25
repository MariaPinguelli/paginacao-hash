def hashEndereco(indice, memoriaFisicaPag):
    enderecoHash = indice%memoriaFisicaPag
    return enderecoHash

def memoriaFisicaInit(listaProc):
    listaNula = []
    tam = int(contPag(listaProc)/4)
    for i in range(tam):
        listaNula.append(None)
    return listaNula

def memoriaVirtualInit(listaProc):
    listaNula = []
    tam = contPag(listaProc)
    for i in range(tam):
        listaNula.append(None)
    return listaNula

def contPag(listaProc):
    soma = 0
    for proc in listaProc:
        soma += proc.qtdPag
    return soma