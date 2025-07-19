def adicionar_contatos(agendas, nome, telefone, email):
    agenda = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    agendas.append(agenda)
    print(f"O contato {nome} foi adicionado com sucesso!")


def ver_contato(agendas):
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


agendas = []

while True:
    print("\nMenu do Gerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Atualizar Contato")
    print("4. Favoritar Contato")
    print("5. Deletar Contato")
    print("6. Sair")

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

    elif escolha == "6":
        break

print("Programa finalizado!")
