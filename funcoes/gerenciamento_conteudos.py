from classes.conteudo import Conteudo
from funcoes.persistencia import salvar_materias

def selecionar_conteudo(materia):
    if not materia.conteudos:
        print(f"\nA matéria '{materia.nome}' não possui conteúdos cadastrados.")
        return None

    print(f"\n=== {materia.nome} ===")
    for i, conteudo in enumerate(materia.conteudos, start=1):
        print(f"{i} - {conteudo.nome}")
    print("0 - Voltar")

    escolha = input("Escolha o conteúdo: ")
    if escolha == "0":
        return None
    try:
        indice_conteudo = int(escolha) - 1
        if indice_conteudo < 0 or indice_conteudo >= len(materia.conteudos):
            print("\nOpção inválida. Tente novamente.")
            return None
    except ValueError:
        print("\nOpção inválida. Tente novamente.")
        return None

    return materia.conteudos[indice_conteudo]

def menu_conteudos(materia, gerenciador):
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
            salvar_materias(gerenciador)
            print(f"\nConteúdo '{nome}' adicionado à matéria '{materia.nome}'.")
    
        elif submenu == "3":
            conteudo = selecionar_conteudo(materia)
            if conteudo is None:
                continue
    
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

            salvar_materias(gerenciador)
            print(f"\nStatus do conteúdo '{conteudo.nome}' atualizado para '{conteudo.status}'.")
    
        elif submenu == "4":
            conteudo = selecionar_conteudo(materia)
            if conteudo is None:
                continue

            anotacao = input("\nDigite a anotação: ").strip()
            if not anotacao:
                    print("\nA anotação não pode ser vazia.")
                    continue
            
            conteudo.adicionar_anotacao(anotacao)
            salvar_materias(gerenciador)
            print(f"\nAnotação adicionada ao conteúdo '{conteudo.nome}' da matéria '{materia.nome}'.")
    
        elif submenu == "5":
            conteudo = selecionar_conteudo(materia)
            if conteudo is None:
                continue

            materia.remover_conteudo(conteudo)
            salvar_materias(gerenciador)
            print(f"\nConteúdo '{conteudo.nome}' removido da matéria '{materia.nome}'.")
    
        elif submenu == "6":
            break