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
            dados = times[time]
            print(f"- {time} ({dados['pontos']}pts, {dados['vitorias']}V, {dados['empates']}E, {dados['derrotas']}D)")

#Registrar as partidas
def registrar_partidas():
    if len(times) < 2:
        print("É necessário ter pelo menos dois times cadastrados.")
        return
   
    print("\nTimes disponíveis:")
    for time in times:
        print("-", time)

    time1 = input("\nDigite o nome do primeiro time: ")
    time2 = input("Digite o nome do segundo time: ")

    if time1 not in times or time2 not in times:
        print("Um ou ambos os times não estão cadastrados.")
        return
    if time1 == time2:
        print("Não é possível registrar partidas do mesmo time.")
        return
   
    gols1 = int(input(f"Quantos gols o {time1} marcou? "))
    gols2 = int(input(f"Quantos gols o {time2} marcou? "))
    print(f"\nResultado: {time1} {gols1} x {gols2} {time2}")

    # Atualizar gols pró
    times[time1]["gols_pro"] += gols1
    times[time2]["gols_pro"] += gols2

    # Atualizar gols contra
    times[time1]["gols_contra"] += gols2
    times[time2]["gols_contra"] += gols1

    # Atualizar saldo de gols
    times[time1]["saldo_gols"] = (
        times[time1]["gols_pro"] -
        times[time1]["gols_contra"]
    )

    times[time2]["saldo_gols"] = (
        times[time2]["gols_pro"] -
        times[time2]["gols_contra"]
    )


    if gols1 > gols2:
        print(f"Vencedor: {time1}")
        times[time1]["pontos"] += 3
        times[time1]["vitorias"] += 1
        times[time2]["derrotas"] += 1

    elif gols1 < gols2:
        print(f"Vencedor: {time2}")
        times[time2]["pontos"] += 3
        times[time2]["vitorias"] += 1
        times[time1]["derrotas"] += 1
       
    else:
        print("A partida terminou empatada!")
        times[time1]["pontos"] += 1
        times[time1]["empates"] += 1
        times[time2]["pontos"] += 1
        times[time2]["empates"] += 1

    print("Estatísticas e pontuações atualizadas com sucesso!")

def mostrar_classificacao():

    if len(times) == 0:
        print("Nenhum time cadastrado.")
        return

    print("\n=== CLASSIFICAÇÃO ===")

    for nome in times:
        print(
            f"{nome} - "
            f"{times[nome]['pontos']} pts | "
            f"V: {times[nome]['vitorias']} | "
            f"E: {times[nome]['empates']} | "
            f"D: {times[nome]['derrotas']} | "
            f"SG: {times[nome]['saldo_gols']}"
        )


def mostrar_campeao():

    if len(times) == 0:
        print("Nenhum time cadastrado.")
        return

    campeao = ""
    maior_pontuacao = -1

    for nome in times:
        if times[nome]["pontos"] > maior_pontuacao:
            maior_pontuacao = times[nome]["pontos"]
            campeao = nome

    print("\n=== CAMPEÃO ===")
    print(f"O campeão é: {campeao}")
    print(f"Pontuação: {maior_pontuacao} pontos")


# Menu Principal Único
while True:
    print("\n=== CAMPEONATO ===")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Registrar partida")
    print("4 - Mostrar classificação")
    print("5 - Mostrar campeão")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")
   
    if opcao == "1":
        cadastrar_time()
    elif opcao == "2":
        listar_times()
    elif opcao == "3":
        registrar_partidas()
    elif opcao == "4":
        mostrar_classificacao()
    elif opcao == "5":
        mostrar_campeao()
    elif opcao == "6":
         print("Encerrando...")
         break


    else:
        print("Opção inválida!")
