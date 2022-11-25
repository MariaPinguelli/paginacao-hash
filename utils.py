def hashEndereco(indice, memoriaFisicaPag):
    enderecoHash = indice%memoriaFisicaPag
    return enderecoHash

def criaListaNula(tam):
    listaNula = []
    for i in range(tam):
        listaNula.append(None)
    return listaNula