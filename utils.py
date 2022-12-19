from random import seed, randint
import math

# Estrutura dos elementos da memória virtual
class MemoriaVirtual:
     def __init__(self, idPagina):
        seed()
        # self.idPagina = idPagina
        self.paginas = []

class MemoriaFisica:
    def __init__(self, idPagina):
        seed()
        self.idPagina = idPagina

tamMemoriaVirtual = 6
tamMemoriaReal = math.floor(tamMemoriaVirtual/2)

class Pagina:
    def __init__(self):
        seed()
        self.id = randint(1000, 9999)
        self.isAloc = False

    def updateAloc(self, isAloc, pos):
        self.isAloc = isAloc
        self.posFisica = pos


# def hashEndereco(idPag, memoriaListaPag):
#     enderecoHash = idPag % memoriaListaPag
#     return enderecoHash

def hashEndereco(idPag):
    enderecoHash = math.floor(idPag % tamMemoriaVirtual)
    return enderecoHash

def memoriaFisicaInit(listaProc):
    listaNula = []
    tam = int(contPag(listaProc)/4)
    for i in range(tam):
        listaNula.append(0)
    return listaNula

def memoriaFisicaInitV2():
    memoriaFisica = []
    for i in range(tamMemoriaReal):
        memoriaFisica.append(MemoriaFisica(0))
    # print("\nMemoria Física: "+str(memoriaFisica))
    return memoriaFisica

def memoriaVirtualInit(listaProc):
    listaNula = []
    tam = contPag(listaProc)
    for i in range(tam):
        listaNula.append(None)
    return listaNula

def memoriaVirtualInit2():
    memoriaVirtual = []
    for i in range(tamMemoriaVirtual):
        memoriaVirtual.append(MemoriaVirtual(0))
    # print("\n\nMemória Virtual: "+str(memoriaVirtual)) 
    return memoriaVirtual


def contPag(listaProc):
    soma = 0
    for proc in listaProc:
        soma += proc.qtdPag
    return soma


# def listaDeAcessoAleatoria(memoriaVirtual):
#     seed()
#     listaDeAcesso = []

#     tamListaAcessos = math.floor(len(memoriaVirtual)/2)
#     for i in range(tamListaAcessos):
#         # tamListaAcessos = len(memoriaVirtual)-1
#         id = randint(0, tamListaAcessos)
#         # listaDeAcesso.append(randint(0, len(memoriaVirtual)-1))
#         listaDeAcesso.append(memoriaVirtual[id])
#     print("Tamanho da memória virtual: " + str(len(memoriaVirtual)))
#     print("Tamanho da lista de acessos: " + str(len(listaDeAcesso)))
#     print("Lista de acessos: ", end=" ")
#     for j in range(len(listaDeAcesso)):
#         print(listaDeAcesso[j].id, end=" ")
#     return listaDeAcesso

def listaDeAcessoAleatoria():
    seed()
    listaDeAcesso = []

    # tamListaAcessos = randint(4, 60)
    tamListaAcessos = randint(1, 10)
    for i in range(tamListaAcessos):
        id = randint(1000, 9999)
        listaDeAcesso.append(id)
    print("Tamanho da lista de acessos: " + str(len(listaDeAcesso)))
    print("Lista de acessos "+str(listaDeAcesso))
    print("\n")
    return listaDeAcesso

def listaDeAcessoAleatoriaAleat():
    seed()
    listaDeAcesso = []

    # tamListaAcessos = randint(4, 60)
    tamListaAcessos = randint(10, 60)
    for i in range(tamListaAcessos):
        pag = Pagina()
        listaDeAcesso.append(pag)
    print("Tamanho da lista de acessos: " + str(len(listaDeAcesso)))
    print("Lista de acessos: ")
    for i in range(len(listaDeAcesso)):
        print(str(listaDeAcesso[i].id), end=" ")
    print("\n")
    return listaDeAcesso