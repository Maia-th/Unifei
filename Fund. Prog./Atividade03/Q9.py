'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 9

Faça um programa para a Polícia Civil de Minas Gerais com a finalidade de ajudar
aclassificar o envolvimento de uma pessoa em um crime. Para isso, o seu programa
deveráfazer 5 perguntas para uma pessoa sobre um crime, sendo elas:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa
nocrime. Se a pessoa responder positivamente a 2 questões ela deve ser classificadacomo
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Casocontrário, ele será
classificado como "Inocente".

'''

# Entrada
p1 = input("Telefonou para a vítima? (S/N): ").strip().upper()
p2 = input("Esteve no local do crime? (S/N): ").strip().upper()
p3 = input("Mora perto da vítima? (S/N): ").strip().upper()
p4 = input("Devia para a vítima? (S/N): ").strip().upper()
p5 = input("Já trabalhou com a vítima? (S/N): ").strip().upper()

# Processamento
respostas_positivas = 0
if p1 == 'S': respostas_positivas += 1
if p2 == 'S': respostas_positivas += 1
if p3 == 'S': respostas_positivas += 1
if p4 == 'S': respostas_positivas += 1
if p5 == 'S': respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Saída
print(classificacao)