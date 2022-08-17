# import time

# ini = time.time()
def permutations(l):
    if len(l) == 1:
        return [l]

    listaAuxiliar = []

    for indice in range(len(l)):
        k = l[indice]

        listaSemK = l[:indice] + l[indice + 1:]

        for p in permutations(listaSemK):
            listaAuxiliar.append([k] + p)
    return listaAuxiliar


file = open('matriz6.txt', 'r')
i, j = file.readline().split()
linhas = file.read().splitlines()
coordenadas = {}
listaDePontos = []

for c in range(int(i)):
    cadaLinha = linhas[c].split()
    for ponto in cadaLinha:
        if ponto != '0':
            coordenadas[ponto] = (c, cadaLinha.index(ponto))
            listaDePontos.append(ponto)

listaDePontos.remove('R')
menorCusto = float('inf')
permut = list(permutations(listaDePontos))

for caminho in permut:
    custoTotal = 0
    indiceDeSoma = 0

    caminho = list(caminho)
    caminho.append('R')
    caminho.insert(0, 'R')

    while indiceDeSoma < len(caminho)-1:
        custoX = abs(coordenadas[caminho[indiceDeSoma]][0] - coordenadas[caminho[indiceDeSoma + 1]][0])
        custoY = abs(coordenadas[caminho[indiceDeSoma]][1] - coordenadas[caminho[indiceDeSoma + 1]][1])
        custoTotal += custoX + custoY
        indiceDeSoma += 1

    if custoTotal < menorCusto:
        menorCusto = custoTotal
        menorCaminho = caminho
resultado = ' '.join(menorCaminho[1:-1])
print(resultado)


# fim = time.time()
# tempo = fim-ini
# print(tempo)
