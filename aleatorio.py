from random import seed, randint
import numpy as np
import utils

memoriaVirtual = []
listaAcessos = []
paginasMapeadasFisica = 0

class Pagina:
    def __init__(self, idProc, nroPag):
        seed()
        self.id = randint(1000, 9999)
        self.isAloc = False
        self.posVirtual = None

# def memoriaVirtualPagAloc(listaProc, memoriaVirtual):
#     x = 0
#     for i in range(len(listaProc)):
#         for j in range(listaProc[i].qtdPag):
#             memoriaVirtual[x] = Pagina(listaProc[i].id, x)
#             x = x+1
#     return memoriaVirtual


def paginacaoAleatoria(listaProc):
    paginasMemFisica = 0
    listaDeAcesso = utils.listaDeAcessoAleatoriaAleat()
    memoriaVirtual = utils.memoriaVirtualInit2()
    memoriaFisica = utils.memoriaFisicaInitV2()

    for i in range(len(listaDeAcesso)):
        pos = utils.hashEnderecoV2(listaDeAcesso[i].id)
        alocaMemoriaVirtual(memoriaVirtual, pos, listaDeAcesso[i])
        alocaMemoriaFisica(memoriaFisica, listaDeAcesso[i], i)

    print("\n\nMemória Virtual\n")
    for i in range(len(memoriaVirtual)):
        print("Posição "+str(i)+"\n")
        for j in range(len(memoriaVirtual[i].paginas)):
            print("Página "+str(memoriaVirtual[i].paginas[j].id))
        print("\n")

def alocaMemoriaVirtual(memoriaVirtual, pos, pagina):
    if (pagina.isAloc == False):
        memoriaVirtual[pos].primeiro = pagina
        memoriaVirtual[pos].paginas.append(pagina)
        pagina.isAloc = True
        pagina.posVirtual = pos


def alocaMemoriaFisica(memoriaFisica, pagina, posFisica):
    # print("mem fis: "+str(len(memoriaFisica))+"\npaginas mem fisica: "+str(posFisica))
    tamMemoriaFisica = len(memoriaFisica)

    if (posFisica < tamMemoriaFisica):
        memoriaFisica[posFisica].idPagina = pagina.id
    # else:
    #     pos = randint(0, len(memoriaFisica))
    #     if(pagina.id != memoriaFisica[pos].idPagina):
    #         buscaFisica(memoriaFisica, pagina)
            
        # buscaVirtual(memoriaVirtual, pagina)
        

# def buscaFisica(memoriaFisica, pagina):
    # pos = utils.hashEnderecoV2(pagina.id)
    # pos = pagina.posVirtual
    # print
    # for i in range(len(memoriaVirtual[pos].paginas)):
    #     if(memoriaVirtual[pos].paginas.id == pagina.id):
    #         print('wee')
    #         memoriaVirtual[pos].paginas.id.pop()
