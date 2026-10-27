'''
Aluno: Thiago Maia

Atividade 04 - Questão 6

Escreva um programa para ler as notas da 1ª e 2ª avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.
'''

# Entrada e Processamento (Validação)
nota1 = float(input("Insira a nota da 1ª avaliação (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida. Insira a nota da 1ª avaliação (0 a 10): "))

nota2 = float(input("Insira a nota da 2ª avaliação (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida. Insira a nota da 2ª avaliação (0 a 10): "))

# Processamento (Cálculo)
media = (nota1 + nota2) / 2

# Saída
print(f"A média do aluno é: {media:.2f}")