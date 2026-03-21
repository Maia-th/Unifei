# 5º) Menu de Usuários

usuarios = {}

while True:
    print("\nMENU:")
    print("1=Incluir usuário")
    print("2=Excluir usuário")
    print("3=Consultar usuário")
    print("4=Alterar usuário")
    print("5=Listar todos os usuários")
    print("9=Sair")
    
    opcao = input("Escolha a opção: ")

    if opcao == '9':
        print("Programa finalizado.")
        break
    
    elif opcao == '1':
        nome = input("Nome do usuário: ")
        id_usuario = len(usuarios) + 1
        usuarios[id_usuario] = nome
        print(f"Usuário {nome} incluído com ID {id_usuario}.")
    
    elif opcao == '2':
        try:
            id_usuario = int(input("ID do usuário a excluir: "))
            if id_usuario in usuarios:
                del usuarios[id_usuario]
                print(f"Usuário {id_usuario} excluído.")
            else:
                print("Usuário não encontrado.")
        except ValueError:
            print("ID inválido.")
    
    elif opcao == '3':
        try:
            id_usuario = int(input("ID do usuário a consultar: "))
            if id_usuario in usuarios:
                print(f"ID {id_usuario}: {usuarios[id_usuario]}")
            else:
                print("Usuário não encontrado.")
        except ValueError:
            print("ID inválido.")
    
    elif opcao == '4':
        try:
            id_usuario = int(input("ID do usuário a alterar: "))
            if id_usuario in usuarios:
                novo_nome = input("Novo nome: ")
                usuarios[id_usuario] = novo_nome
                print(f"Usuário {id_usuario} alterado.")
            else:
                print("Usuário não encontrado.")
        except ValueError:
            print("ID inválido.")
    
    elif opcao == '5':
        if usuarios:
            print("Usuários cadastrados:")
            for id_usuario, nome in usuarios.items():
                print(f"{id_usuario} - {nome}")
        else:
            print("Nenhum usuário cadastrado.")
    
    else:
        print("Opção inválida. Programa finalizado.")
        break