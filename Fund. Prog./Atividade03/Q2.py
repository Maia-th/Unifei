'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 2

Faça um programa em Python que calcule a média de 4 (quatro) números. Caso
oresultado da média seja maior ou igual ao valor 60, imprima a mensagem
"AlunoAprovado". Caso contrário, imprima "Aluno Reprovado". 

'''

# Entrada
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

# Processamento
media = (n1 + n2 + n3 + n4) / 4
if media >= 60:
    resultado = "Aluno Aprovado"
else:
    resultado = "Aluno Reprovado"

# Saída
print(resultado)