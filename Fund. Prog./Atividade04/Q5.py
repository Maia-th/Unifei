'''
Aluno: Thiago Maia

Atividade 04 - Questão 5

Escreva um programa para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido.
'''

# Entrada
valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))

# Processamento
while valor2 == 0:
    print("O segundo valor não pode ser zero.")
    valor2 = float(input("Insira um novo segundo valor: "))

resultado_divisao = valor1 / valor2

# Saída
print(f"O resultado da divisão é: {resultado_divisao:.2f}")