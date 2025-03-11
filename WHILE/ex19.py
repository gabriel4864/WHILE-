# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número
# negativo seja inserido. No final, exiba o maior número informado.
num = 0 
maior = 0
while num >= 0:
    num = int(input("Digite um numero (ou <0 para parar): "))
    if num > maior:
        maior = num
    print(maior)