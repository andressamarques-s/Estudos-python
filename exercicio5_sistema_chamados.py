chamados = [
    {"usuario": "Ana", "problema": "Sem acesso", "status": "aberto"},
    {"usuario": "João", "problema": "Impressora", "status": "fechado"},
    {"usuario": "Carlos", "problema": "Email", "status": "aberto"},
    {"usuario": "Maria", "problema": "VPN", "status": "fechado"},
    {"usuario": "Pedro", "problema": "Senha", "status": "aberto"},
]

def carregar_chamados():
    with open("chamados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        print("Chamados carregados!")

def adicionar_chamado():
    chamado = {}
    novo = input("Deseja adicionar um novo chamado? (s/n): ")
    if novo == "s":
        chamado["usuario"] = input("Digite o nome do usuário: ")
        chamado["problema"] = input("Digite o problema: ")
        chamado["status"] = input("Digite o status: ")
        chamados.append(chamado)
        print("Chamado adicionado com sucesso!")
    else:
        return "Obrigado por usar o sistema!"

def salvar_chamados():
    with open("chamados.txt", "w") as arquivo:
        for chamado in chamados:
            arquivo.write(f"{chamado['usuario']} | {chamado['problema']} | {chamado['status']}\n")

def listar_chamados():
    with open("chamados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())

carregar_chamados()
adicionar_chamado()
salvar_chamados()
listar_chamados()
