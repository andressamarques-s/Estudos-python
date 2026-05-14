chamados = []

def adicionar_chamado():
    nome = input("Digite seu nome: ")
    problema = input("Digite um problema: ")
    chamado = {"nome": nome, "problema": problema}
    chamados.append(chamado)

def listar_chamados(chamados):
    for numero, chamado in enumerate(chamados):
        print(f"Chamado {numero + 1} - Usuário: {chamado['nome']} | Problema: {chamado['problema']}")

adicionar_chamado()
adicionar_chamado()
adicionar_chamado()
listar_chamados(chamados)
