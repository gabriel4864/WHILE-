# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário
# digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.
ultimo_numero = 1
contador = 0
while True:
    numero = float(input("Digite um número: "))
    if numero == ultimo_numero:
        break
    ultimo_numero = numero
    contador += 1

print(f"foram digitados {contador} números e o ultimo numero foi {ultimo_numero}")