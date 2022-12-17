from random import seed, randint
import math

tamMemoriaVirtual = 16
tamMemoriaReal = math.floor(tamMemoriaVirtual/2)

def hashEndereco(idPag, memoriaListaPag):
    enderecoHash = idPag % memoriaListaPag
    return enderecoHash

def hashEnderecoV2(idPag):
    enderecoHash = math.floor(idPag % tamMemoriaVirtual)
    return enderecoHash

def memoriaFisicaInit(listaProc):
    listaNula = []
    tam = int(contPag(listaProc)/4)
    for i in range(tam):
        listaNula.append(0)
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

    tamListaAcessos = math.floor(len(memoriaVirtual)/2)
    for i in range(tamListaAcessos):
        # tamListaAcessos = len(memoriaVirtual)-1
        id = randint(0, tamListaAcessos)
        # listaDeAcesso.append(randint(0, len(memoriaVirtual)-1))
        listaDeAcesso.append(memoriaVirtual[id])
    print("Tamanho da memória virtual: " + str(len(memoriaVirtual)))
    print("Tamanho da lista de acessos: " + str(len(listaDeAcesso)))
    print("Lista de acessos: ", end=" ")
    for j in range(len(listaDeAcesso)):
        print(listaDeAcesso[j].id, end=" ")
    return listaDeAcesso

def listaDeAcessoAleatoriaV2():
    seed()
    listaDeAcesso = []

    tamListaAcessos = randint(4, 60)
    for i in range(tamListaAcessos):
        id = randint(1000, 9999)
        listaDeAcesso.append(id)
    print("Tamanho da lista de acessos: " + str(len(listaDeAcesso)))
    print("Lista de acessos: ", end=" ")
    for j in range(len(listaDeAcesso)):
        print(listaDeAcesso[j].id, end=" ")
    return listaDeAcesso