'''
Aluno: Thiago Maia

Atividade 5 - Questão 8

Faça um programa que leia um endereço de e-mail informado pelo usuário. Caso o e-
mail informado esteja no padrão correto, ou seja, tenha no mínimo @.com o seu
programa deverá imprimir a mensagem "e-mail informado está correto" e finalizar o
programa, caso contrário deverá imprimir "e-mail inválido" e solicitar que o usuário
informe um novo e-mail válido.
'''

# Entrada e Processamento
while True:
    email = input("Digite um e-mail: ")
    if "@" in email and ".com" in email:
        resultado = "e-mail informado está correto"
        break
    else:
        print("e-mail inválido")

# Saída
print(resultado)