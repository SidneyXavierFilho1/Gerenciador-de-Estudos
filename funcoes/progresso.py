from funcoes.persistencia import salvar_materias

def registrar_progresso(gerenciador):
    while True:
        if not gerenciador.listar_materias():
            print("\nNenhuma matéria cadastrada. Adicione uma matéria primeiro.")
            break
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
        salvar_materias(gerenciador)
        print(f"\n{horas} hora(s) registradas para a matéria '{materia.nome}'.")

def ver_progresso(gerenciador):
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