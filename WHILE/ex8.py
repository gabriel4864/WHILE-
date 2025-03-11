# 3. Somar números até o usuário digitar 0. Peça números ao usuário e
# some-os até que ele digite 0.
num = int(input("Digite um numero: ")) 
soma = 0

while num != 0: #Enquanto o usuario nao digita 0 (Repetir codigo)
    soma += num # Soma o ultimo numero apresentado com o valor atual
    num = int(input("Digite um numero (ou 0 para sair): ")) 
print(soma)