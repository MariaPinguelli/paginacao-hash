# Imports
from random import seed, randint
from sc import paginacaoSC

#Variáveis globais
#Índice é o endereço virtual, e ao acessar o endereço virtual, conseguimos o índice para acessar a memoria física
#Variável com espaço de endereços virtuais
memoriaVirtual = []

#Variável com endereços fisicos
memoriaFisica = []

# listaProc = []

class Processo:
    def __init__(self, qtdPag):
        seed()
        self.id = randint(1000, 9999)
        self.qtdPag = qtdPag

def main():
    listaProc = []
    seed()
    qtdProc = randint(1, 10)
    
    for i in range(qtdProc):
        proc = Processo(randint(1, 20))
        listaProc.append(proc)
    
    paginacaoSC(listaProc)

if __name__ == "__main__":
    main()