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
# exercicio 4
def posiciona_frota(frota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]       
    for coordenadas in frota.values():
        for coordenada in coordenadas:
            i = 0
            while i < len(coordenada):
                tabuleiro[coordenada[i][0]][coordenada[i][1]] = 1
                i +=1
    return (tabuleiro)
#exercicio5
def afundados(frota,tabuleiro):
    navios_afundados = 0 
    for posicoes_navio in frota.values():
        for posicao in posicoes_navio:
            certos = 0 
            i = 0
            while i < len(posicao):
                if tabuleiro[posicao[i][0]][posicao[i][1]] == 'X':
                    certos +=1 
                i += 1 
            if certos == len(posicao):
                navios_afundados += 1 
    return (navios_afundados)
#exercicio6
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    if orientacao == 'horizontal':
        if coluna + tamanho > 10:
            return False
    elif orientacao == 'vertical':
        if linha + tamanho > 10:
            return False 
    nome = define_posicoes(linha,coluna,orientacao,tamanho)
    for posicoes in frota.values():
        for coordenadas in posicoes:
                for i in range(len(coordenadas)):
                    for k in range(len(nome)):  
                        if coordenadas[i] == nome[k]:
                            return False 
    return True

               
               
        
                    









