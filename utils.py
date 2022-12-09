from random import seed, randint

def hashEndereco(idPag, memoriaListaPag):
    enderecoHash = idPag%memoriaListaPag
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

def listaDeAcessoAleatoria(memoriaVirtual):
    seed()
    listaDeAcesso = []
    
    for i in range(len(memoriaVirtual)):
        listaDeAcesso.append(randint(0, len(memoriaVirtual)))
    
    return listaDeAcesso