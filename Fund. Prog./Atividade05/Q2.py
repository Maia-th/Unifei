'''
Aluno: Thiago Maia

Atividade 5 - Questão 2

Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em
maiúscula e sem espaços em branco.
'''

# Entrada
frase = input("Digite uma frase: ")

# Processamento
frase_processada = frase.upper().replace(" ", "")

# Saída
print(frase_processada)