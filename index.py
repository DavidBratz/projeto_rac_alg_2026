# Dicionário onde serão armazenados os times
times = {}

def cadastrar_time():
    nome = input("Digite o nome do time: ")

    if nome in times:
        print("Esse time já está cadastrado!")
    else:
        times[nome] = {
            "pontos": 0,
            "vitorias": 0,
            "empates": 0,
            "derrotas": 0,
            "gols_pro": 0,
            "gols_contra": 0,
            "saldo_gols": 0
        }

        print("Time cadastrado com sucesso!")

def listar_times():
    if len(times) == 0:
        print("Nenhum time cadastrado.")
    else:
        print("\nTimes cadastrados:")
        for time in times:
            print("-", time)

# Teste da parte 1
while True:
    print("\n=== CADASTRO DE TIMES ===")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_time()

    elif opcao == "2":
        listar_times()

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
        