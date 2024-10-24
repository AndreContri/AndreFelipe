# exercicio 1 
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao = []
    if orientacao == 'vertical':
        while tamanho != 0:
            posicao.append([0,coluna]) 
            tamanho -= 1
        i = 0
        while i < len(posicao):
            posicao[i][0] = linha
            linha += 1
            i += 1 
    else:  
        while tamanho != 0:
            posicao.append([linha,0]) 
            tamanho -= 1
        i = 0
        while i < len(posicao):
            posicao[i][1] = coluna
            coluna += 1
            i += 1 
    return (posicao)
#exercicio 2
def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    posicao_navio = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota.keys():
        frota[nome_navio].append(posicao_navio)
    else: 
        frota[nome_navio] = [posicao_navio]
    return frota    
# exercicio 3
def faz_jogada(tabuleiro,linha,coluna):
    chute = tabuleiro[linha][coluna]
    if chute == 1:
       tabuleiro[linha][coluna] = 'X'
    if chute == 0:
         tabuleiro[linha][coluna] = '-'
    return tabuleiro




