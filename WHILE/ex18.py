# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o
# usuário digite -1. Em seguida, exiba a média das notas.
numero = int(input("Digite um numero: "))
soma = 0 
contador = 1
while True: 
    numero = int(input("Digite um numero: "))
    soma += numero
    contador += 1
    if numero == -1:
        break 
soma // contador
print(soma)