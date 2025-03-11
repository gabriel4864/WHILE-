# 1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.
numero = int(input("Digite um numero: "))
n1 = 2
while n1 <= numero: 
    n1 += numero 
    n1 += 2
print(n1)
