from classes.conteudo import Conteudo
from classes.materia import Materia
from classes.gerenciador_estudo import GerenciadorEstudos

gerenciador = GerenciadorEstudos()

while True:
    print("\nMenu:")
    print("1. Adicionar matéria")
    print("2. Ver matérias e conteúdos")
    print("3. Registrar progresso de estudo")
    print("4. Ver progresso de estudo")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")
    if escolha not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida. Tente novamente.")
        continue

    if escolha == "1":
        nome_materia = input("Digite o nome da matéria: ").strip()
        if not nome_materia:
            print("O nome da matéria não pode ser vazio.")
            continue
        while True:
            try:
                metas_horas = int(input("Digite a meta de horas de estudo para a semana: "))

                if metas_horas <= 0:
                    print("A meta de horas deve ser um número positivo.")
                    continue
                break

            except ValueError:
                print("A meta de horas deve ser um número inteiro.")
                continue

        materia = Materia(nome_materia, metas_horas)
        gerenciador.adicionar_materia(materia)
        print(f"Matéria '{nome_materia}' adicionada com sucesso!")

    elif escolha == "2":

        while True:
            print("\n=== Matérias ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                print(f"{indice} - {materia.nome}")

            print("0 - Voltar")

            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                print("Opção inválida. Tente novamente.")
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
                print("5 - Voltar")

                submenu = input("Escolha: ")
                if submenu not in ["1", "2", "3", "4", "5"]:
                    print("Opção inválida. Tente novamente.")
                    continue

                if submenu == "1":
                    print(f"\n=== Conteúdos de {materia.nome} ===")
                    if not materia.conteudos:
                        print(f"A matéria '{materia.nome}' não possui conteúdos cadastrados.")
                    for conteudo in materia.conteudos:
                        print(f"- {conteudo.nome} (Status: {conteudo.status})")
                        if conteudo.anotacoes:
                            for anotacao in conteudo.anotacoes:
                                print(f"  - Anotação: {anotacao}")

                elif submenu == "2":
                    nome = input("Digite o nome do conteúdo: ").strip()
                    if not nome:
                        print("O nome do conteúdo não pode ser vazio.")
                        continue
                    conteudo = Conteudo(nome)
                    materia.adicionar_conteudo(conteudo)
                    print(f"Conteúdo '{nome}' adicionado à matéria '{materia.nome}'.")

                elif submenu == "3":
                    nome_conteudo = input("Digite o nome do conteúdo que deseja atualizar: ").strip()
                    if not nome_conteudo:
                        print("O nome do conteúdo não pode ser vazio.")
                        continue
                    conteudo = materia.obter_conteudo(nome_conteudo)
                    if conteudo:
                        print("Escolha o novo status:")
                        print("1 - Não iniciado")
                        print("2 - Em andamento")
                        print("3 - Concluído")
                        status_opcao = input("Escolha: ")
                        if status_opcao not in ["1", "2", "3"]:
                            print("Opção inválida. Tente novamente.")
                            continue
                        if status_opcao == "1":
                            conteudo.atualizar_status("Não iniciado")
                        elif status_opcao == "2":
                            conteudo.atualizar_status("Em andamento")
                        elif status_opcao == "3":
                            conteudo.atualizar_status("Concluído")
                        else:
                            print("Opção inválida.")
                    else:
                        print(f"Conteúdo '{nome_conteudo}' não encontrado.")

                elif submenu == "4":
                    nome_conteudo = input("Digite o nome do conteúdo que deseja adicionar anotação: ").strip()
                    if not materia.conteudos:
                        print(f"A matéria '{materia.nome}' não possui conteúdos cadastrados.")
                        continue
                    else:
                        print(f"\n=== Conteúdos de {materia.nome} ===")
                        for conteudo in materia.conteudos:
                            print(f"- {conteudo.nome} (Status: {conteudo.status})")
                    if not nome_conteudo:
                        print("O nome do conteúdo não pode ser vazio.")
                        continue
                    conteudo = materia.obter_conteudo(nome_conteudo)
                    if conteudo:
                        anotacao = input("Digite a anotação: ").strip()
                        if not anotacao:
                            print("A anotação não pode ser vazia.")
                            continue
                        conteudo.adicionar_anotacao(anotacao)
                    else:
                        print(f"Conteúdo '{nome_conteudo}' não encontrado.")

                elif submenu == "5":
                    break

    elif escolha == "3":
        while True:
            print("\n=== Registrar Progresso de Estudo ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                            print(f"{indice} - {materia.nome}")
            
            print("0 - Voltar")
            
            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                            print("Opção inválida. Tente novamente.")
                            continue
            if opcao == "0":
                            break
            
            indice = int(opcao) - 1
            materia = gerenciador.listar_materias()[indice]

        try:
            horas = int(input("Digite o número de horas estudadas: "))
            
            if horas <= 0:
                print("O número de horas deve ser um valor positivo.")
                continue

        except ValueError:
            print("O número de horas deve ser um valor inteiro.")
            continue

        materia.registrar_estudo(horas)
        print(f"{horas} hora(s) registradas para a matéria '{materia.nome}'.")

    elif escolha == "4":
        while True:
            print("\n=== Ver Progresso de Estudo ===")

            for indice, materia in enumerate(gerenciador.listar_materias(), start=1):
                print(f"{indice} - {materia.nome}")

            print("0 - Voltar")

            opcao = input("Escolha: ")
            if opcao not in [str(i) for i in range(len(gerenciador.listar_materias()) + 1)]:
                print("Opção inválida. Tente novamente.")
                continue

            if opcao == "0":
                break

            indice = int(opcao) - 1
            materia = gerenciador.listar_materias()[indice]

            progresso_semanal = materia.calcular_progresso_semanal()
            progresso_geral = materia.calcular_progresso_geral()

            print(f"\nProgresso da matéria '{materia.nome}':")
            print(f"Progresso semanal: {progresso_semanal:.2f}%")
            print(f"Progresso geral: {progresso_geral:.2f}%")

    elif escolha == "5":
        print("Saindo do programa...")
        break
