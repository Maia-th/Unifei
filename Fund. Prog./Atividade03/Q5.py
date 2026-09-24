'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 5

Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

'''

# Entrada
idade = int(input("Idade do trabalhador: "))
tempo_servico = int(input("Tempo de serviço (anos): "))

# Processamento
if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    resultado = "Pode reformar-se (aposentar-se)."
else:
    resultado = "Não pode reformar-se (aposentar-se)."

# Saída
print(resultado)