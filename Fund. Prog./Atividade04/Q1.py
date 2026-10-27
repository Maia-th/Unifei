'''
Aluno: Thiago Maia

Atividade 04 - Questão 1

Escreva um programa para encontrar a soma S=3+6+9+....+333.
'''

# Entrada
soma = 0
limite_final = 333
passo = 3

# Processamento
for i in range(3, limite_final + 1, passo):
    soma += i

# Saída
print(f"A soma S é: {soma}")