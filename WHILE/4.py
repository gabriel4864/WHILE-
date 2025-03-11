senha = "1234"
tentativa = input("Digite a senha: ")
while tentativa != senha:
    print("Senha errada. Tente novamente!")
    tentativa = input("Digite a senha: ")
print("Acesso autorizado!")