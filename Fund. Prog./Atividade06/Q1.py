'''
Aluno: Thiago Maia

Atividade 6 - Manipulação de Listas

Escreva um programa de MENU contendo as opções:
1= Incluir usuário
2= Excluir usuário
3= Consultar usuário
4= Alterar usuário
5= Listar todos os usuários que estão cadastrados
9= Sair.
O programa deve validar os campos (Nome Completo, CPF, Telefone, E-mail, Data de Nascimento).
'''

# Inicialização (Processamento Global)
usuarios = []

def valida_email(email):
    return "@" in email and "." in email

def exibir_menu():
    print("\n--- MENU ---")
    print("1 = Incluir usuário")
    print("2 = Excluir usuário")
    print("3 = Consultar usuário")
    print("4 = Alterar usuário")
    print("5 = Listar todos os usuários")
    print("9 = Sair")
    return input("Escolha uma opção: ")

# Entrada, Processamento e Saída interativos
opcao = ""
while opcao != "9":
    opcao = exibir_menu()
    
    if opcao == "1":
        # Incluir
        nome = input("Nome Completo: ")
        while not nome.replace(" ", "").isalpha():
            print("Nome inválido. Use apenas letras.")
            nome = input("Nome Completo: ")
            
        cpf = input("CPF (apenas números): ")
        while not (cpf.isdigit() and len(cpf) == 11):
            print("CPF inválido. Informe 11 dígitos numéricos.")
            cpf = input("CPF (apenas números): ")
            
        telefone = input("Telefone: ")
        while not telefone.isdigit():
            print("Telefone inválido. Informe apenas números.")
            telefone = input("Telefone: ")
            
        email = input("E-mail: ")
        while not valida_email(email):
            print("E-mail inválido.")
            email = input("E-mail: ")
            
        data_nasc = input("Data de Nascimento (DD/MM/AAAA): ")
        while len(data_nasc.split('/')) != 3:
            print("Formato de data inválido.")
            data_nasc = input("Data de Nascimento (DD/MM/AAAA): ")
            
        usuarios.append({"nome": nome, "cpf": cpf, "telefone": telefone, "email": email, "data_nasc": data_nasc})
        print("Usuário incluído com sucesso!")
        
    elif opcao == "2":
        # Excluir
        cpf_busca = input("Informe o CPF do usuário a ser excluído: ")
        encontrado = False
        for u in usuarios:
            if u["cpf"] == cpf_busca:
                usuarios.remove(u)
                print("Usuário excluído!")
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.")
            
    elif opcao == "3":
        # Consultar
        cpf_busca = input("Informe o CPF do usuário para consulta: ")
        encontrado = False
        for u in usuarios:
            if u["cpf"] == cpf_busca:
                print(f"Nome: {u['nome']} | Telefone: {u['telefone']} | E-mail: {u['email']} | Nasc: {u['data_nasc']}")
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.")
            
    elif opcao == "4":
        # Alterar
        cpf_busca = input("Informe o CPF do usuário que deseja alterar: ")
        for u in usuarios:
            if u["cpf"] == cpf_busca:
                novo_nome = input(f"Novo Nome ({u['nome']}): ") or u['nome']
                novo_tel = input(f"Novo Telefone ({u['telefone']}): ") or u['telefone']
                u['nome'] = novo_nome
                u['telefone'] = novo_tel
                print("Dados alterados com sucesso!")
                break
        else:
            print("Usuário não encontrado.")
            
    elif opcao == "5":
        # Listar
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de Usuários:")
            for u in usuarios:
                print(f"CPF: {u['cpf']} - Nome: {u['nome']}")
                
    elif opcao == "9":
        print("Saindo do sistema...")
        
    else:
        print("Opção inválida.")