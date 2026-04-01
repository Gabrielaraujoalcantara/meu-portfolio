contatos = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }

    contatos.append(contato)
    print("Contato adicionado!\n")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
        return
    
    for i, contato in enumerate(contatos):
        fav = "⭐" if contato["favorito"] else ""
        print(f"{i} - {contato['nome']} / {contato['telefone']} / {fav}")
    print()

def editar_contato():
    listar_contatos()
    indice = int(input("Digite o numero do contato para editar: "))

    if 0 <= indice < len(contatos):
        contatos[indice]["nome"] = input("novo nome: ")
        contatos[indice]["telefone"] = input("Novo telefone: ")
        contatos[indice]["email"] = input("Novo email: ")
        print("contato atualizado\n")
    else:
        print("Indice invalido!\n")

def deletar_contato():
    listar_contatos()
    indice = int(input("Digite o numero do contato para deletar: "))

    if 0 <= indice < len(contatos):
        contatos.pop(indice)
        print("Contato removido!\n")
    else: 
        print("indice invalido.\n")

def favoritar_contato():
    listar_contatos()
    indice = int(input("Digite o numero do contato para favoritar"))

    if 0 <= indice < len(contatos):
        contatos[indice]["favorito"] = True
        print("Contato marcado como favorito!\n")
    else:
        print("indice invalido.\n")

def menu():
    while True:
        print("----- AGENDA -----")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Editar contato")
        print("4 - Deletar contato")
        print("5 - Favoritar contato")
        print("0 - Sair")
       
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            editar_contato()
        elif opcao == "4":
            deletar_contato()
        elif opcao == "5":
            favoritar_contato()
        elif opcao == "0":
            print("Saindo")
            break
        else:
            print("Opcao invalida!\n")

menu()
