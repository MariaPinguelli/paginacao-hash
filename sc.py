# Imports
from random import seed, randint
from utils import contPag, memoriaFisicaInit, memoriaVirtualInit

class Pagina:
    def __init__(self, qtdPag):
        seed()
        self.id = randint(1000, 9999)
        self.qtdPag = qtdPag


# Lógica atual
# inicializar as memórias
# criar páginas
# alocar páginas
# e quando todos os espaços fisicos tiverem sido alocados
# começa lista de acesso, e cria ela cada elemento com 2 numeros aleatorios de acesso
def paginacaoSC(listaProc):
    print("Qtd de paginas: " + str(contPag(listaProc)))
    
    memoriaFisica = memoriaFisicaInit(listaProc)
    memoriaVirtual = memoriaVirtualInit(listaProc)

    
    