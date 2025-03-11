# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo
# (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de
# votos nulos e brancos. A entrada 0 encerra a votação.
voto = int(input("Digite em qual candidato ira votar [1|2|3|4] ou [5] para nulo ou [6] para branco e [7] para encerrar a votacao:  "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
contagem = 0
while voto != 7:
    voto = int(input("Digite em qual candidato ira votar [1|2|3|4] ou [5] para nulo ou [6] para branco e [7] para encerrar a votacao:  "))
    if voto == 1:
        candidato1 += 1
        contagem +=1
    elif voto == 2:
        candidato2 +=1
        contagem +=1
    elif voto == 3:
        candidato3 += 1
        contagem += 1
    elif voto ==  4:
        candidato4 += 1
        contagem +=1
    elif voto == 5:
        nulo +=1
        contagem +=1
    else:
        branco += 1
        contagem +=1
pnulo = (nulo/contagem)* 100
pbranco = (branco/contagem)*100
print("     FIM DA VOTACAO")
print("------------------------")
print("Quantidade de votos do candidato 1: ", candidato1)
print("Quantidade de votos do candidato 2: ", candidato2)
print("Quantidade de votos do candidato 3: ", candidato3)
print("Quantidade de votos do candidato 4: ", candidato4)
print("Quantidade de votos nulos: ", nulo)
print("Quantidade de votos brancos: ", branco)
print("-------------------------------------")
print ("porcentagem de votos nulos: ", pnulo, "%")
print("Porcentagem de votos brancos: ", pbranco, "%")

    
