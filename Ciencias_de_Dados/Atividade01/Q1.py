# 1º) Programa de Desconto

conta = float(input("Informe o valor da conta: "))
desconto = float(input("Informe o percentual de desconto: "))
valor_final = conta - (conta * desconto / 100)
print(f"Valor final da conta com desconto: R$ {valor_final:.2f}")