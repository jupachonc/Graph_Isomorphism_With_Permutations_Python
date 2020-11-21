import copy

#Permutación a través del algoritmo de Heap
def permute(n, lista):
    if n == 1:
        yield lista
    else:
        for i in range(0,n):
            for p in permute(n-1, lista):
                yield p
            if n % 2 == 0:
                lista[i], lista[n-1] = lista[n-1], lista[i]
            else:
                lista[0], lista[n-1] = lista[n-1], lista[0]


#Impresión de la tabla de Cayley
def printCayleyTable(n):

    #Cálculo de las permutaciones
    array = []
    for p in permute(n, list(range(1, n+1))):
        array.append(copy.deepcopy(p))

    #Impresión del alineador
    print([0] * len(array[0]), end="\t")

    #Impresión del encabezado
    for a in array:
        print(a, end="\t")
    print()

    #Generación de la tabla
    for x in array:
        print(x, end="\t")
        for y in array:
            op = []
            for i in y:
                op.append(x[i-1])
            print(op, end="\t") 
        print()

#Permutación de una matriz(filas y columnas)
def permutemtx(mtx, per):
    mtaux= []
    for x in per:
        mtaux.append(mtx[x-1])
    mtaux = [list(y) for y in zip(*mtaux)]
    mtout =[]
    for x in per:
        mtout.append(mtaux[x-1])
    return [list(y) for y in zip(*mtout)]

#Paso de notación de permutación a notación de ciclo disyunto
def to_cycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi))
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break
        if len(cycle) > 1:
            cycles.append(cycle)

    return cycles

#Búsqueda de los automorfismos de un grafo a partir de su matriz de adyacencia.
def findAutomorphism(gf):
    perms = []
    for per in permute(len(gf), list(range(1, len(gf) + 1))):
        if gf == permutemtx(gf, per):
            perms.append(copy.deepcopy(per))
    return perms

#Determina si dos grafos son isomorfos a partir de sus matrices de adyacencia.
def isIsomorph(g1, g2):
    if(g1 == g2):
        return True
    if len(g1) != len(g2):
        return False
    cg1 = 0
    cg2 = 0
    for x in g1:
        cg1 += sum(x)
    for y in g2:
        cg2 += sum(y)
    if cg1 != cg2:
        return False
    for per in permute(len(g1), list(range(1, len(g1) + 1))):
        if g1 == permutemtx(g2, per):
            return True
    return False