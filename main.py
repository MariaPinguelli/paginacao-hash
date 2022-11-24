# import strformat
#Variáveis globais
memoriaFisicaPag = 0

#Índice é o endereço virtual, e ao acessar o endereço virtual, conseguimos o índice para acessar a memoria física
#Variável com espaço de endereços virtuais
memoriaVirtual = []

#Variável com endereços fisicos
memoriaFisica = []

tabelaPaginas = []

def substituirPaginaAleatorio():
    print("Substituir pagina aleatorio")
    
def substituirPaginaSC():
    print("Substituir pagina SC")

def hashEndereco(indice):
    enderecoHash = indice%memoriaFisicaPag
    return enderecoHash

def processo(qtdPag, nomeProcesso):
    global memoriaFisicaPag
    
    memoriaFisicaPag += qtdPag/4
    
    print("Nome do Processo: " + nomeProcesso)
    print("Quantidade de paginas do processo: " + str(qtdPag))
    print("Quantidade de paginas da memoria fisica: " + str(memoriaFisicaPag))
    
    

def main():
    processo(12, "Processo aleatorio A")
    print("\n")
    processo(20, "Processo aleatorio B")
    

if __name__ == "__main__":
    main()