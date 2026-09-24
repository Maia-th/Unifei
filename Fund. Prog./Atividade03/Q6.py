'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 6

Faça um programa em Python que leia duas notas N1 e N2 de um aluno, e
informe se ele foi aprovado ou não numa disciplina.
Considere que a média final é dada pela equação:
média = 0.4 * N1 + 0.6 * N2
E que o aluno está se a média for maior ou igual a 5.0 e, reprovado caso contrário.

'''

# Entrada
n1 = float(input("Nota N1: "))
n2 = float(input("Nota N2: "))

# Processamento
media = (0.4 * n1) + (0.6 * n2)
if media >= 5.0:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# Saída
print(resultado)