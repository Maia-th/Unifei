'''
Aluno: Thiago Maia

Atividade 5 - Questão 4

Faça um programa que leia um nome, calcule e imprima a quantidade letras que tem esse
nome.
'''

# Entrada
nome = input("Digite um nome: ")

# Processamento
quantidade_letras = len(nome.replace(" ", ""))

# Saída
print(f"O nome tem {quantidade_letras} letras.")