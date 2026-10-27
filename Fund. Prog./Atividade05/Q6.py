'''
Aluno: Thiago Maia

Atividade 5 - Questão 6

Faça a um programa que receba do usuário um nome e imprima este mesmo nome sem
as suas vogais.
'''

# Entrada
nome = input("Digite um nome: ")

# Processamento
vogais = "aeiouAEIOU"
nome_sem_vogais = ""
for letra in nome:
    if letra not in vogais:
        nome_sem_vogais += letra

# Saída
print(f"Sem vogais: {nome_sem_vogais}")