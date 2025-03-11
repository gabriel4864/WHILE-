# 2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha
# correta definida previamente.
senha = "1234"
tentativa = input("Digite a senha: ")
while True:
    print("Senha incorreta")
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        break
print("Senha correta!")    
