'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 1

Faça um programa em Python que receba um número e caso ele seja par imprima “O
número informado é Par.”, caso contrário se este número for ímpar imprima “O número
informado é Ímpar.”. 

'''

# Entrada
numero = int(input("Insira um número: "))

# Processamento
if numero % 2 == 0:
    resultado = "O número informado é Par."
else:
    resultado = "O número informado é Ímpar."

# Saída
print(resultado)