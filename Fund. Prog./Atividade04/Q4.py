'''
Aluno: Thiago Maia

Atividade 04 - Questão 4

Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número, somente a multiplicação.
'''

# Entrada
numero = int(input("Insira um número de 1 a 10: "))
tabuada = []

# Processamento
if 1 <= numero <= 10:
    for i in range(1, 11):
        tabuada.append(f"{numero} x {i} = {numero * i}")
else:
    tabuada.append("Número fora do intervalo permitido.")

# Saída
for linha in tabuada:
    print(linha)