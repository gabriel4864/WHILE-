# 8. Encontrando o maior número inserido pelo usuário. Peça números ao
# usuário e, ao digitar 0, exiba o maior número inserido.
num = int(input("Digite um numero"))
maior = max(num,num) #Pegando maior valor entre os digitados
while num != 0: #Enquanto o numero for diferente de 0 (Repetir codigo)
    if num > maior: #Se o numero digitado for maior que o maior valor anterior
        maior = num # O novo numero sera o maior
    num = int(input("Digite um numero: "))
print(maior)