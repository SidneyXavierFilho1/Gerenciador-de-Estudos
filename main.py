import json

from classes.conteudo import Conteudo
from classes.materia import Materia
from classes.gerenciador_estudo import GerenciadorEstudos

gerenciador = GerenciadorEstudos()

def salvar_materias():
    with open("materias.json", "w", encoding="utf-8") as arquivo:
        json.dump([materia.to_dict() for materia in gerenciador.listar_materias()], arquivo, indent=4, ensure_ascii=False)

with open("materias.json", "r", encoding="utf-8") as arquivo:
    materias_data = json.load(arquivo)
    for materia_data in materias_data:
        materia = Materia.from_dict(materia_data)
        gerenciador.adicionar_materia(materia)

while True:
    print("\nMenu:")
    print("1. Adicionar matéria")
    print("2. Ver matérias e conteúdos")
    print("3. Registrar progresso de estudo")
    print("4. Ver progresso de estudo")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")
    if escolha not in ["1", "2", "3", "4", "5"]:
        print("\nOpção inválida. Tente novamente.")
        continue

    if escolha == "1":
        nome_materia = input("Digite o nome da matéria: ").strip()
        if not nome_materia:
            print("\nO nome da matéria não pode ser vazio.")
            continue
        while True:
            try:
                meta_horas = int(input("Digite a meta de horas de estudo para a semana: "))

                if meta_horas <= 0:
                    print("\nA meta de horas deve ser um número positivo.")
                    continue
                break

            except ValueError:
                print("\nA meta de horas deve ser um número inteiro.")
                continue

        materia = Materia(nome_materia, meta_horas)
        gerenciador.adicionar_materia(materia)
        salvar_materias()
        print(f"\nMatéria '{nome_materia}' adicionada com sucesso!")

    elif escolha == "2":

        while True:
            print("\n=== Matérias ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                print(f"{indice} - {materia.nome}")

            print("0 - Voltar")

            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                print("\nOpção inválida. Tente novamente.")
                continue

            if opcao == "0":
                break

            indice = int(opcao) - 1
            materia = gerenciador.listar_materias()[indice]

            while True:
                print(f"\n=== {materia.nome} ===")

                print("1 - Ver conteúdos")
                print("2 - Adicionar conteúdo")
                print("3 - Atualizar status")
                print("4 - Adicionar anotação")
                print("5 - Remover conteúdo")
                print("6 - Voltar")

                submenu = input("Escolha: ")
                if submenu not in ["1", "2", "3", "4", "5", "6"]:
                    print("\nOpção inválida. Tente novamente.")
                    continue

                if submenu == "1":
                    print(f"\n=== Conteúdos de {materia.nome} ===")
                    if not materia.conteudos:
                        print(f"\nA matéria '{materia.nome}' não possui conteúdos cadastrados.")
                    for conteudo in materia.conteudos:
                        print(f"- {conteudo.nome} (Status: {conteudo.status})")
                        if conteudo.anotacoes:
                            for anotacao in conteudo.anotacoes:
                                print(f"  - Anotação: {anotacao}")

                elif submenu == "2":
                    nome = input("Digite o nome do conteúdo: ").strip()
                    if not nome:
                        print("\nO nome do conteúdo não pode ser vazio.")
                        continue
                    conteudo = Conteudo(nome)
                    materia.adicionar_conteudo(conteudo)
                    salvar_materias()
                    print(f"\nConteúdo '{nome}' adicionado à matéria '{materia.nome}'.")

                elif submenu == "3":
                    if not materia.conteudos:
                        print(f"\nA matéria '{materia.nome}' não possui conteúdos cadastrados.")
                        continue

                    print(f"\n=== {materia.nome} ===")

                    for i, conteudo in enumerate(materia.conteudos, start=1):
                        print(f"{i} - {conteudo.nome}")
                    print("0 - Voltar")

                    escolha_conteudo = input("Escolha o conteúdo que deseja atualizar o status: ")
                    if escolha_conteudo == "0":
                        continue
                    try:
                        indice_conteudo = int(escolha_conteudo) - 1
                        if indice_conteudo < 0 or indice_conteudo >= len(materia.conteudos):
                            print("\nOpção inválida. Tente novamente.")
                            continue

                    except ValueError:
                        print("\nOpção inválida. Tente novamente.")
                        continue
                    conteudo = materia.conteudos[indice_conteudo]

                    print("\nEscolha o novo status:")
                    print("1 - Em andamento ")
                    print("2 - Concluído")

                    status_opcao = input("\nEscolha: ")
                    if status_opcao not in ["1", "2"]:
                        print("\nOpção inválida. Tente novamente.")
                        continue
                    if status_opcao == "1":
                        conteudo.atualizar_status("Em andamento")
                    elif status_opcao == "2":
                        conteudo.atualizar_status("Concluído")
                    salvar_materias()
                    print(f"\nStatus do conteúdo '{conteudo.nome}' atualizado para '{conteudo.status}'.")

                elif submenu == "4":
                    if not materia.conteudos:
                        print(f"\nA matéria '{materia.nome}' não possui conteúdos cadastrados.")
                        continue
                    print(f"\n=== {materia.nome} ===")
                    for i, conteudo in enumerate(materia.conteudos, start=1):
                        print(f"{i} - {conteudo.nome}")
                    print("\n0 - Voltar")
                    escolha_anotacao = input("Escolha o conteúdo que deseja adicionar uma anotação: ")
                    if escolha_anotacao == "0":
                        continue
                    try:
                        indice_conteudo = int(escolha_anotacao) - 1
                        if indice_conteudo < 0 or indice_conteudo >= len(materia.conteudos):
                            print("\nOpção inválida. Tente novamente.")
                            continue    
                    except ValueError:
                        print("\nOpção inválida. Tente novamente.")
                        continue
                        
                    conteudo = materia.conteudos[indice_conteudo]
                    anotacao = input("\nDigite a anotação: ").strip()
                    if not anotacao:
                            print("\nA anotação não pode ser vazia.")
                            continue
                    conteudo.adicionar_anotacao(anotacao)
                    salvar_materias()
                    print(f"\nAnotação adicionada ao conteúdo '{conteudo.nome}' da matéria '{materia.nome}'.")

                elif submenu == "5":
                    if not materia.conteudos:
                        print(f"\nA matéria '{materia.nome}' não possui conteúdos cadastrados.")
                        continue
                    print(f"\n=== {materia.nome} ===")
                    for i, conteudo in enumerate(materia.conteudos, start=1):
                        print(f"{i} - {conteudo.nome}")
                    print("0 - Voltar")
                    escolha_remover = input("Escolha o conteúdo que deseja remover: ")
                    if escolha_remover == "0":
                        continue
                    try:
                        indice_conteudo = int(escolha_remover) - 1
                        if indice_conteudo < 0 or indice_conteudo >= len(materia.conteudos):
                            print("\nOpção inválida. Tente novamente.")
                            continue    
                    except ValueError:
                        print("\nOpção inválida. Tente novamente.")
                        continue
                        
                    conteudo = materia.conteudos[indice_conteudo]
                    materia.remover_conteudo(conteudo)
                    salvar_materias()
                    print(f"\nConteúdo '{conteudo.nome}' removido da matéria '{materia.nome}'.")

                elif submenu == "6":
                    break

    elif escolha == "3":
        while True:
            print("\n=== Registrar Progresso de Estudo ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                            print(f"{indice} - {materia.nome}")
            
            print("0 - Voltar")
            
            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                            print("\nOpção inválida. Tente novamente.")
                            continue
            if opcao == "0":
                            break
            
            indice = int(opcao) - 1
            materia = gerenciador.listar_materias()[indice]

            try:
                horas = int(input("Digite o número de horas estudadas: "))
                
                if horas <= 0:
                    print("\nO número de horas deve ser um valor positivo.")
                    continue

            except ValueError:
                print("\nO número de horas deve ser um valor inteiro.")
                continue

            materia.registrar_estudo(horas)
            salvar_materias()
            print(f"\n{horas} hora(s) registradas para a matéria '{materia.nome}'.")

    elif escolha == "4":
        while True:
            print("\n=== Ver Progresso de Estudo ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                print(f"\n{indice} - {materia.nome}")

            print("0 - Voltar")

            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                print("\nOpção inválida. Tente novamente.")
                continue

            if opcao == "0":
                break

            indice = int(opcao) - 1
            materia = gerenciador.listar_materias()[indice]

            progresso_horas = materia.calcular_progresso_horas()
            progresso_conteudos = materia.calcular_progresso_conteudos()
            progresso_total = materia.calcular_progresso_total()

            print(f"\nProgresso da matéria '{materia.nome}':")
            print(f"Progresso por horas: {progresso_horas:.2f}%")
            print(f"Progresso por conteúdos: {progresso_conteudos:.2f}%")
            print(f"Progresso total: {progresso_total:.2f}%")

    elif escolha == "5":
        print("Saindo do programa...")
        break