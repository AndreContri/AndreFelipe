# exercicio 1 
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_final = []
    if orientacao == 'vertical':
        while tamanho != 0:
            lista_final.append([0,coluna]) 
            tamanho -= 1
        i = 0
        while i < len(lista_final):
            lista_final[i][0] = linha
            linha += 1
            i += 1 
    else: 
        while tamanho != 0:
            lista_final.append([linha,0]) 
            tamanho -= 1
        i = 0
        while i < len(lista_final):
            lista_final[i][1] = coluna
            coluna += 1
            i += 1 
    return (lista_final)
