# 2º) Calculadora Básica com Validação

while True:
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("F - Finalizar")
    opcao = input("Informe a opção: ").upper()

    if opcao == 'F':
        break

    try:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))
    except ValueError:
        print("Erro: Os valores devem ser números.")
        continue

    if opcao == '1':
        print(f"Resultado: {n1 + n2}")
    elif opcao == '2':
        print(f"Resultado: {n1 - n2}")
    elif opcao == '3':
        print(f"Resultado: {n1 * n2}")
    elif opcao == '4':
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Opção inválida.")