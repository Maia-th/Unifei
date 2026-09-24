'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 3

Faça um programa Python que receba o valor de um salário e um percentual de aumento
a ser aplicado. Calcular o novo salário e imprimir o resultado obtido. Caso o novo salário
seja maior do R$ 2.000,00 imprima a mensagem "Novo salário é Acima da média
nacional brasileira". Caso contrário imprima "Novo salário é Abaixo da média
nacional brasileira ". 

'''

# Entrada
salario = float(input("Valor do salário: "))
percentual = float(input("Percentual de aumento: "))

# Processamento
novo_salario = salario + (salario * percentual / 100)
if novo_salario > 2000.00:
    mensagem = "Novo salário é Acima da média nacional brasileira"
else:
    mensagem = "Novo salário é Abaixo da média nacional brasileira"

# Saída
print(f"Novo Salário: {novo_salario:.2f}")
print(mensagem)