# 10. Apenas aceitar números positivos. O programa deve continuar pedindo
# um número até o usuário digitar um número positivo.
num = 0

tentativa = int(input("Digite um numero:"))
while tentativa < num: #Enquanto a tentatiava for maior que zero (Repetir codigo)
    print("Numero invalido!") 
    tentativa = int(input("Digite um numero:")) #Digitar o numero novamente
print("Numero aceito")

