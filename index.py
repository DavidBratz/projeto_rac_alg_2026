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
# Registrar as partidass

def registrar_partidas():
    if len(times) < 2:
        print("É necessário ter pleo menos dois times cadastrados.")
        return
    
    print("\nTimes disponíveis:")
    for time in times:
        print("-", times)

        time1 = input("Digite o nome do primeiro time")
        time2 = input("Digite o nome do segundo time")

        if time1 not in times or time2 not in times:
            print("Um ou ambos os times não estão cadastrados.")
            return
        if time1 == time2:
            print("Não é possível registrar partidas do mesmo time.")
            return
        
        gols1 = int(input(f"Quantos gols o {time1} marcou?"))
        gols2 = int(input(f"Quantos gols o {time2} marcou?"))
        print(f"\nResultado: {time1} {gols1} x {gols2} {time2}")

        if gols1>gols2:
            print(f"Vencedor: {time1}")

        elif gols1<gols2:
            print(f"Vencedor: {time2}")

        else:
            print("A partida terminou empatada")

# teste parte1 parte2
while True:
    print("\n=== CAMPEONATO ===")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Registrar partida")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_time()
    elif opcao == "2":
        listar_times()
    elif opcao == "3":
        registrar_partidas()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")

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


