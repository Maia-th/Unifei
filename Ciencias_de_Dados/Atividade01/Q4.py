# 4º) Validador de CNPJ

while True:
    cnpj = input("Informe o CNPJ (12 dígitos): ")
    
    if cnpj.upper() == 'F':
        break
    
    if not cnpj.isdigit() or len(cnpj) != 12:
        print("CNPJ inválido. Informe um número válido.")
        continue

    # Primeiro dígito
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    d1 = 11 - (soma1 % 11)
    if d1 >= 10:
        d1 = 0

    # Segundo dígito
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(12))
    d2 = 11 - (soma2 % 11)
    if d2 >= 10:
        d2 = 0

    print(f"Dígitos verificadores: {d1}{d2}")