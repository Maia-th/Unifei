'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 4

Faça um programa em Python que recebe o NOME e o PREÇO de um produto. Casoo
PREÇO informado seja maior do que 100,00 calcule um desconto de 25% e imprima
oNOME e PREÇO-COM-DESCONTO e a frase "Desconto de 25%.". Caso
contrário,calcule um desconto de 15% e imprima o NOME, PREÇO-COM-DESCONTO
e a frase"Desconto de 15%." 

'''

# Entrada
nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))

# Processamento
if preco > 100.00:
    desconto = 0.25
    frase = "Desconto de 25%."
else:
    desconto = 0.15
    frase = "Desconto de 15%."

preco_com_desconto = preco - (preco * desconto)

# Saída
print(f"Nome: {nome}")
print(f"Preço com desconto: {preco_com_desconto:.2f}")
print(frase)