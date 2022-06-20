def beautiful_matrix(matrix):
    posicao_linha = -1
    i = 0
    while i < 5:
        linha = []
        linha = matrix[i]
        print(linha)
        print(linha.index(0))
        if linha.index(1) != 0:
            posicao_linha += 0
        i += 1
    print("Achei: ", posicao_linha)

line = []
i=0
while i < 5 :
    line.append( list(map(int,input().split())) )
    i += 1
beautiful_matrix(line)