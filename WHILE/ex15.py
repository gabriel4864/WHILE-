# 9. Contar quantos números pares o usuário digitar. O programa deve
# contar quantos números pares o usuário inseriu. O usuário para digitando -1.
soma = 0
numero = int(input("Digite um numero: "))
if numero %2 == 0: # Se o numero digitado for par, adicionar um ja no primeiro valor proposto
    soma += 1
while numero != -1: # Enquanto o numero for diferente de -1 (Repetir codigo)
    numero = int(input("Digite um numero: "))  
    if numero %2 == 0:
        soma += 1 # Adicionar um a contagem semrpre que o numero for par
print("---------------------------")
print("Foram digitados: ", soma, "numeros pares")