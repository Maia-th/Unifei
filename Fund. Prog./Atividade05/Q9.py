'''
Aluno: Thiago Maia

Atividade 5 - Questão 9

Faça um programa em Python que calcule a média de 4 (quatro) números informados
pelo usuário. Caso o resultado da média seja maior ou igual ao valor 60, imprima a
mensagem "AlunoAprovado". Caso contrário, imprima "Aluno Reprovado". Você deverá
validar a informação dos 4 números informados e, deverá aceitar somente informações
do tipo int e ou float. Ou seja, você precisará criar uma lógica para verificar os
informados e, caso o usuário não informe um valor do tipo float e ou int, o seu programa
não pode cancelar (apresentar erro) e deverá exibir a seguinte mensagem: "Favor
informar um número válido para cada uma das 4 (quatro) notas".
'''

# Entrada e Processamento
notas = []
while len(notas) < 4:
    entrada = input(f"Informe a nota {len(notas) + 1}: ")
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("Favor informar um número válido para cada uma das 4 (quatro) notas")

media = sum(notas) / 4

if media >= 60:
    resultado = "Aluno Aprovado"
else:
    resultado = "Aluno Reprovado"

# Saída
print(f"Média: {media:.2f} - {resultado}")