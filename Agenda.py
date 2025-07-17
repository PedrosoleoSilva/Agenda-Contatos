
def adicionar_contatos (agendas, nome, telefone, email):
    agenda = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    agendas.append(agenda)
    print(f"O contato {nome}, foi adicionado com sucesso!")
    return

def ver_contato(agendas):
    for indice, agenda in enumerate(agendas, start = 1):
        status = "✰" if agenda["favorito"] else ""
        print(f"Favorito: {indice}. [{status}] \n Nome:  {agenda['contato']} \n Numero:  {agenda['telefone']} \n Email: {agenda['email']}")
    return

agendas = [];

while True:
    print("\n Menu Do Gerenciador de Lista de tarefas");
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Atualizar Contato")
    print("4. Favoritar Contato")
    print("5. Deletar  Contato")
    print("6. Sair")

    escolha = input("Digite a opção desejada: \n")
    if escolha == "1":
        contato_adicionar =input("Digite o nome do contato \n")
        telefone_contato = input("Digite o número do contato \n")
        email_contato = input("Digite o email do contato \n")
        adicionar_contatos(agendas, contato_adicionar, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contato(agendas)
    elif escolha == "6":
        break
print("programa finalizado!")