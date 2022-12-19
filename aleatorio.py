from random import seed, randint
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
        self.posFisica = None

def paginacaoAleatoria():
    paginasMemFisica = 0
    listaDeAcesso = utils.listaDeAcessoAleatoriaAleat()
    memoriaVirtual = utils.memoriaVirtualInit2()
    memoriaFisica = utils.memoriaFisicaInitV2()

    for i in range(len(listaDeAcesso)):
        pos = utils.hashEnderecoV2(listaDeAcesso[i].id)
        alocaMemoriaVirtual(memoriaVirtual, pos, listaDeAcesso[i])
        if (paginasMemFisica >= len(memoriaFisica)):
            pos = freePos(memoriaFisica, memoriaVirtual)
            alocaMemoriaFisica(memoriaFisica, listaDeAcesso[i], pos)
        else:
            alocaMemoriaFisica(memoriaFisica, listaDeAcesso[i], i)
            paginasMemFisica += 1

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

def freePos(memoriaFisica, memoriaVirtual):
    tamMemFisica = len(memoriaFisica)
    pos = randint(0, tamMemFisica-1)
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
