num = int(input("Digite um numero: "))
soma = 0

while num != 0:
    soma += num
    num = int(input("Digite um numero (ou 0 para sair): "))
    
print(soma)