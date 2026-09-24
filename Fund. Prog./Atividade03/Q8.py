'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 8

Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números negativos.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números pares.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção___

'''

# Entrada
print("Escolha a opção:")
print("1- Soma de 2 números negativos.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números pares.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")
opcao = input("Opção: ")

# Processamento
erro = False
resultado = None

if opcao in ['1', '2', '3', '4']:
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    
    if opcao == '1':
        if n1 < 0 and n2 < 0:
            resultado = n1 + n2
        else:
            erro = True
    elif opcao == '2':
        if n1 > n2:
            resultado = n1 - n2
        else:
            resultado = n2 - n1
    elif opcao == '3':
        if n1 % 2 == 0 and n2 % 2 == 0:
            resultado = n1 * n2
        else:
            erro = True
    elif opcao == '4':
        if n2 != 0:
            resultado = n1 / n2
        else:
            erro = True
else:
    erro = True

# Saída
if erro:
    print("Erro: Opção inválida ou números não cumprem as regras da opção escolhida.")
else:
    print(f"Resultado: {resultado}")