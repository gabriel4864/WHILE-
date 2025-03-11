# 4. O usuário deve digitar a senha correta (1234). Enquanto errar, o
# programa deve pedir novamente.
senha = "1234"
tentativa = input("Digite a senha: ")

while tentativa != senha: # Enquanto a tentativa for diferente da senha (Repetir codigo)
    print("Senha incorreta!") # Mostrando que a senha esta incorreta
    tentativa = input("Digite a senha: ") # Pedindo senha novamente
print("Senha correta!")