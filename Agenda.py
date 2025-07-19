def adicionar_contatos(agendas, nome, telefone, email):
    agenda = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    agendas.append(agenda)
    print(f"O contato {nome} foi adicionado com sucesso!")


def ver_contato(agendas):
    if not agendas:
        print("Nenhum contato cadastrado.")
        return
    for indice, agenda in enumerate(agendas, start=1):
        status = "✰" if agenda["favorito"] else ""
        print(f"{indice}. [{status}]")
        print(f"  Nome: {agenda['contato']}")
        print(f"  Número: {agenda['telefone']}")
        print(f"  Email: {agenda['email']}\n")


def atualizar_contato(agendas, indice_contato, novo_nome, novo_numero, novo_email):
    indice = int(indice_contato) - 1
    if 0 <= indice < len(agendas):
        agendas[indice]["contato"] = novo_nome
        agendas[indice]["telefone"] = novo_numero
        agendas[indice]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print("Índice de contato inválido!")


def favoritar_contato(agendas, indice_contato):
    indice = int(indice_contato) - 1
    if 0 <= indice < len(agendas):
        agendas[indice]["favorito"] = not agendas[indice]["favorito"]
        estado = "favoritado" if agendas[indice]["favorito"] else "removido dos favoritos"
        print(f"Contato {indice_contato} foi {estado}.")
    else:
        print("Índice de contato inválido!")


def ver_favoritos(agendas):
    favoritos = [a for a in agendas if a["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    for indice, agenda in enumerate(favoritos, start=1):
        print(f"{indice}. [✰]")
        print(f"  Nome: {agenda['contato']}")
        print(f"  Número: {agenda['telefone']}")
        print(f"  Email: {agenda['email']}\n")


def deletar_contato(agendas, indice_contato):
    indice = int(indice_contato) - 1
    if 0 <= indice < len(agendas):
        removido = agendas.pop(indice)
        print(f"Contato '{removido['contato']}' removido com sucesso.")
    else:
        print("Índice de contato inválido!")


agendas = []

while True:
    print("\nMenu do Gerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Ver Todos os Contatos")
    print("3. Atualizar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contatos(agendas, nome, telefone, email)
    elif escolha == "2":
        ver_contato(agendas)
    elif escolha == "3":
        ver_contato(agendas)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo email: ")
        atualizar_contato(agendas, indice_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        ver_contato(agendas)
        indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        favoritar_contato(agendas, indice_contato)
    elif escolha == "5":
        ver_favoritos(agendas)
    elif escolha == "6":
        ver_contato(agendas)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(agendas, indice_contato)
    elif escolha == "7":
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
