# 7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
# um número até acertar. (Declare um valor e receba outro)
numsecreto = "9"
tentativa = input("Adivinhe o numero de 1 a 10: ")
while tentativa != numsecreto: #Enquanto a tentativa for diferente do numero secreto (Repetir codigo)
    print("Numero errado!")
    tentativa = input("Adivinhe o numero de 1 a 10: ") # Pedindo senha novamente
print("----------PARABENS----------")
print("       numero Correto!")
