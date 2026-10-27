'''
Aluno: Thiago Maia

Atividade 5 - Questão 3

Faça um programa que leia um nome e imprima somente as 4 primeiras letras do nome.
Em seguida, imprima as 4 últimas letras do nome.
'''

# Entrada
nome = input("Digite um nome: ")

# Processamento
primeiras_quatro = nome[:4]
ultimas_quatro = nome[-4:]

# Saída
print(f"4 primeiras: {primeiras_quatro}")
print(f"4 últimas: {ultimas_quatro}")