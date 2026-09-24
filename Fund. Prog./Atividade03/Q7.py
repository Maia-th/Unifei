'''
Aluno: Thiago Oliveira Maia

Atividade 03 - Questão 7

Ler uma temperatura em graus Celsus e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F= c* 9 / 5 - 32 sendo F a temperatura em Fahrenheit e C a
temperatura em Celsus. Caso a temperatura em Fahrenheit seja maior do que 90 imprima
a mensagem "Estamos no inverno" e, caso contrário imprima
a mensagem "Estamos no verão".

'''

# Entrada
c = float(input("Temperatura em Celsius: "))

# Processamento
f = c * 9 / 5 - 32
if f > 90:
    mensagem = "Estamos no inverno"
else:
    mensagem = "Estamos no verão"

# Saída
print(f"Temperatura convertida: {f:.2f} F")
print(mensagem)