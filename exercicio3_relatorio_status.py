chamados = [
    {"usuario": "Ana", "problema": "Sem acesso", "status": "aberto"},
    {"usuario": "João", "problema": "Impressora", "status": "fechado"},
    {"usuario": "Carlos", "problema": "Email", "status": "aberto"},
    {"usuario": "Maria", "problema": "VPN", "status": "fechado"},
    {"usuario": "Pedro", "problema": "Senha", "status": "aberto"},
]

def relatorio(chamados):
    print("--- ABERTOS ---")
    for chamado in chamados:
        if chamado["status"] == "aberto":
            print(f"{chamado['usuario']} | {chamado['problema']}")

    print("\n--- FECHADOS ---")
    for chamado in chamados:
        if chamado["status"] == "fechado":
            print(f"{chamado['usuario']} | {chamado['problema']}")

relatorio(chamados)
