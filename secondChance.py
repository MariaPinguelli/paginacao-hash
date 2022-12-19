import utils
from random import seed, randint

class Pagina:
    def __init__(self, idPagina):
        self.idPagina = idPagina
        self.isAloc
        self.bitAcesso = 1
    
    def updateAcesso(self):
        self.bitAcesso = 0
    
    def updateMrIndex(self, mrIndex):
        self.mrIndex = mrIndex

def runPaginacaoSC():
    aux = 0
    paginasMemFisica = 0
    listaDeAcesso = utils.listaDeAcessoAleatoriaAleat()
    tamListaDeAcesso = len(listaDeAcesso)
    memoriaVirtual = utils.memoriaVirtualInit2()
    memoriaFisica = utils.memoriaFisicaInitSC()
    tamMemFisica = len(memoriaFisica)
    
    while aux < tamListaDeAcesso:
        posVirtual = utils.hashEnderecoV2(listaDeAcesso[aux].id)
        alocaMemoriaVirtual(memoriaVirtual, posVirtual, listaDeAcesso[aux])

        if (paginasMemFisica >= len(memoriaFisica)):
            if(memoriaFisica[0].bitAcesso == 0):
                pos = freePos(memoriaFisica, memoriaVirtual)
                # memoriaFisica[0].bitAcesso = 1
                alocaMemoriaFisica(memoriaFisica, listaDeAcesso[aux], pos)
            else:
                algoritmoSC(memoriaFisica, tamMemFisica)
                # alocaMemoriaFisica(memoriaFisica, listaDeAcesso[aux], pos)
                
        else:
            alocaMemoriaFisica(memoriaFisica, listaDeAcesso[aux], aux)
            paginasMemFisica += 1
        aux += 1

        print("\nMemória Física\n")
        for j in range(len(memoriaFisica)):
            print("Pos "+str(j)+" Página: "+str(memoriaFisica[j].idPagina))
        print('\n')


def alocaMemoriaVirtual(memoriaVirtual, pos, pagina):
    if (pagina.isAloc == False):
        memoriaVirtual[pos].paginas.append(pagina.id)
        pagina.isAloc = True
        pagina.posVirtual = pos

def alocaMemoriaFisica(memoriaFisica, pagina, posFisica):

    memoriaFisica[posFisica].idPagina = pagina.id
    pagina.posFisica = posFisica

def algoritmoSC(memoriaFisica, tamMemFisica):
    memoriaFisica[0].bitAcesso = 0
    aux = memoriaFisica[0]
    for i in range(tamMemFisica-1):
        memoriaFisica[i] = memoriaFisica[i+1]
    memoriaFisica[tamMemFisica-1] = aux

def freePos(memoriaFisica, memoriaVirtual):
    print('free pos')
    tamMemFisica = len(memoriaFisica)
    pos = randint(0, tamMemFisica-1)
    print('pos'+str(pos))
    print("Elemento na memória física:: "+str(memoriaFisica[pos].idPagina))
    
    pagina = memoriaFisica[pos]
    print("Pagina pra remover: "+str(pagina.idPagina))
    
    posVirtual = utils.hashEnderecoV2(pagina.idPagina)
    paginas = memoriaVirtual[posVirtual].paginas

    for j in range(len(paginas)):
        print('Páginas no array de páginas na memória virtual antes de remover: '+str(paginas[j]))

    for i in range(len(paginas)):
        if (pagina.idPagina == paginas[i]):
            pagina.isAloc = False
            paginas.remove(pagina.idPagina)
            break

    if(len(paginas) == 0): 
        print("Não há páginas na estrutura de páginas na posição "+str(pos)+" da memória virtual")
    else:
        for i in range(len(paginas)):
            print('Páginas no array de páginas na memória virtual: '+str(paginas[i]))
    print('\n')
    return pos
