'''
Aluno: Thiago Maia

Atividade 5 - Questão 10

Faça um programa em Python que solicite ao usuário que informe os dados de nome,
data de nascimento e CPF. Seu programa deverá validar e somente aceitar um nome
válido (não deve conter números e nem caracteres especiais e, somente a primeira letra
do nome deverá estar em maiúsculo), uma data de nascimento válida e um CPF válido
(deverá realizar o cálculo do dígito verificador). Após as validações imprimir os dados
informados com suas respectivas máscaras.
'''

# Processamento e Entrada
def validar_nome(n):
    if not n.replace(" ", "").isalpha(): return False
    partes = n.split()
    for p in partes:
        if p != p.capitalize(): return False
    return True

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11: return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]): return False
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]): return False
    return True

def validar_data(d):
    partes = d.split('/')
    if len(partes) != 3: return False
    if not all(p.isdigit() for p in partes): return False
    dia, mes, ano = map(int, partes)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1900): return False
    return True

# Loops de validação
while True:
    nome = input("Digite o nome: ")
    if validar_nome(nome): break
    print("Nome inválido.")

while True:
    data = input("Digite a data (DD/MM/AAAA): ")
    if validar_data(data): break
    print("Data inválida.")

while True:
    cpf = input("Digite o CPF (apenas números ou com pontuação): ")
    if validar_cpf(cpf): 
        cpf = ''.join(filter(str.isdigit, cpf))
        break
    print("CPF inválido.")

# Saída
print(f"\nNOME: {nome}")
print(f"Data Nascimento: {data}")
print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")