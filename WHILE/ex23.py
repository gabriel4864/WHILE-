# 8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba
# o troco. Após isso, o programa deve reiniciar para um novo cliente.
valor = float(input("Digite um valor: R$"))
total_compra = 0

while valor != 0:
    total_compra += valor #Colocar antes o incremento 
    valor = float(input("Digite um valor: R$"))
print("O valor total da compra foi de R$", total_compra)
valor_pago = float(input("Digite o total pago na compra: R$"))
troco = valor_pago - total_compra
print("O troco sera: R$", troco)

