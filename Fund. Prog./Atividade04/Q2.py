'''
Aluno: Thiago Maia

Atividade 04 - Questão 2

Escreva um programa que leia 10 notas e informe a média dos alunos.
'''

# Entrada
soma_notas = 0
quantidade_alunos = 10

# Processamento
for i in range(quantidade_alunos):
    nota = float(input(f"Insira a nota {i+1}: "))
    soma_notas += nota

media = soma_notas / quantidade_alunos

# Saída
print(f"A média das notas é: {media:.2f}")