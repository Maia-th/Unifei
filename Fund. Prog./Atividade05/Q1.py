'''
Aluno: Thiago Maia

Atividade 5 - Questão 1

Considere a string A = "Um elefante incomoda muita gente" Que fatia da variável A
em python corresponde a "elefante incomoda"?
'''

# Entrada
A = "Um elefante incomoda muita gente"

# Processamento
# "Um " tem 3 caracteres (índice 0 a 2). "elefante incomoda" começa no índice 3 e vai até o 20 (exclusivo).
fatia = A[3:20]

# Saída
print(fatia)