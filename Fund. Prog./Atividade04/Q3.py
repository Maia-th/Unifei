'''
Aluno: Thiago Maia

Atividade 04 - Questão 3

Escreva um programa de MENU contendo as opções de (1=Inclusão, 2=Exclusão, 3=Consulta, 4=Relatório e 9=Sair). O programa só deve ser finalizado quando o usuário digitar a opção 9=Sair
'''

# Entrada
opcao = 0

# Processamento
while opcao != 9:
    opcao = int(input("MENU:\n1=Inclusão\n2=Exclusão\n3=Consulta\n4=Relatório\n9=Sair\nEscolha uma opção: "))
    
    if opcao == 1:
        resultado = "Você escolheu: Inclusão"
    elif opcao == 2:
        resultado = "Você escolheu: Exclusão"
    elif opcao == 3:
        resultado = "Você escolheu: Consulta"
    elif opcao == 4:
        resultado = "Você escolheu: Relatório"
    elif opcao == 9:
        resultado = "Saindo do programa..."
    else:
        resultado = "Opção inválida. Tente novamente."
        
    # Saída
    print(resultado)