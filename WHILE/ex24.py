# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos
# desejados. O programa deve calcular o valor total e permitir que o usuário finalize o
# pedido digitando 0.
codigo = float(input("Digite o codigo do pedido ou [0] para finalizar a compra: "))
quantidade = int(input("Digite a quantidade de pedidos: "))
while codigo != "0":
    codigo = float(input("Digite um valor ou [0] para finalizar a compra: "))
    quantidade = int(input("Digite a quantidade de pedidos: "))
print("Compra finalizada!")