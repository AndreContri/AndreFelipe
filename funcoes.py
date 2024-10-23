texto = 'Design de Software\nInsper\nEngenharia'
texto_final = ''

for i in range(len(texto)):
    if texto[i] + texto[i+1] == '\n':
        print (texto[i+2])

        

# for palavra in lista_palavras:
#     if 
#     texto_final += (f"{palavra}({len(palavra)}) ")
# texto_final = texto_final.strip()
# print (lista_palavras )


# Design(6) de(2) Software(8) Insper(6) Engenharia(10)








# ','.join(['a', 'b', 'c'])  
# # Retorna 'a,b,c'


# 'Design de Software\nInsper\nEngenharia'
# 'Design\nde\nSoftware\nInsper\nEngenharia'
# 'Design de Software Insper Engenharia'
# ['Design', 'de', 'Software', 'Insper', 'Engenharia']
