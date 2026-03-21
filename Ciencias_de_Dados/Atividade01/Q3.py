# 3º) Validador de CPF

while True:
    cpf = input("Informe o CPF (9 dígitos): ")
    
    if cpf.upper() == 'F':
        break
    
    if not cpf.isdigit() or len(cpf) != 9:
        print("CPF inválido. Informe um número válido.")
        continue

    # Calcula primeiro dígito
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = (soma1 * 10) % 11
    if d1 == 10:
        d1 = 0

    # Calcula segundo dígito
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(9)) + d1 * 2
    d2 = (soma2 * 10) % 11
    if d2 == 10:
        d2 = 0

    print(f"Dígitos verificadores: {d1}{d2}")