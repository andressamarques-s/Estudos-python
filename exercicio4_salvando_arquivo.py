chamados = [
    {"usuario": "Ana", "problema": "Sem acesso", "status": "aberto"},
    {"usuario": "João", "problema": "Impressora", "status": "fechado"},
    {"usuario": "Carlos", "problema": "Email", "status": "aberto"},
    {"usuario": "Maria", "problema": "VPN", "status": "fechado"},
    {"usuario": "Pedro", "problema": "Senha", "status": "aberto"},
]

def salvar_chamados():
    with open("chamados.txt", "w") as arquivo:
        for chamado in chamados:
            arquivo.write(f"{chamado['usuario']} | {chamado['problema']} | {chamado['status']}\n")

def carregar_chamados():
    with open("chamados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())

salvar_chamados()
carregar_chamados()
