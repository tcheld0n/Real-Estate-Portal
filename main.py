# Simulação de banco de dados em dicionários
clientes = {}
propriedades = {}
agentes = {}
visitas = {}

# 1. Autenticação e Perfis de Usuários
def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    tipo_usuario = input("Tipo de usuário (comprador/locatario/agente/admin): ")

    if email in clientes:
        print("Usuário já cadastrado!")
        return

    clientes[email] = {"nome": nome, "senha": senha, "tipo": tipo_usuario}
    print(f"Usuário {nome} cadastrado com sucesso!")

def login():
    email = input("Email: ")
    senha = input("Senha: ")

    if email in clientes and clientes[email]["senha"] == senha:
        print("Login bem-sucedido!")
        return email
    else:
        print("Credenciais inválidas.")
        return None

# 2. Listagem e Gerenciamento de Propriedades
def cadastrar_propriedade(dono_email):
    global id_propriedade
    area = input("Tamanho em m^2: ")
    preco = input("Preço: ")
    localizacao = input("Localização: ")
    
    propriedades[id_propriedade] = {
        "dono": dono_email,
        "area": area,
        "preco": preco,
        "localizacao": localizacao,
        "status": "disponível"
    }
    print(f"Propriedade cadastrada com sucesso! ID: {id_propriedade}")
    id_propriedade += 1

# 4. Perfis de Agentes Imobiliários
def cadastrar_agente():
    global id_agente
    nome = input("Nome do agente: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    agentes[id_agente] = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
    }
    print(f"Agente {nome} cadastrado com sucesso! ID: {id_agente}")
    id_agente += 1

def buscar_propriedades():
    return 0

def agendar_visita():
    return 0

# Menu principal
def menu():
    usuario_logado = None

    while True:
        print("\n===== Portal de Imóveis =====")
        print("1 - Cadastrar Usuário")
        print("2 - Login")
        print("3 - Cadastrar Propriedade")
        print("4 - Buscar Propriedades")
        print("5 - Cadastrar Agente")
        print("6 - Agendar Visita")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario_logado = login()
        elif opcao == "3":
            if usuario_logado:
                cadastrar_propriedade(usuario_logado)
            else:
                print("Faça login primeiro!")
        # elif opcao == "4":
        #     buscar_propriedades()
        # elif opcao == "5":
        #     cadastrar_agente()
        # elif opcao == "6":
        #     agendar_visita()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()