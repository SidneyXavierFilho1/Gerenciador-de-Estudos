from classes.materia import Materia
from funcoes.persistencia import salvar_materias
from funcoes.gerenciamento_conteudos import menu_conteudos

def adicionar_materia(gerenciador):
    nome_materia = input("\nDigite o nome da matéria: ").strip()
    if not nome_materia:
        print("\nO nome da matéria não pode ser vazio.")
        return
    
    while True:
        try:
            meta_horas = int(input("\nDigite a meta de horas de estudo para a semana: "))
    
            if meta_horas <= 0:
                print("\nA meta de horas deve ser um número positivo.")
                continue
            break
    
        except ValueError:
            print("\nA meta de horas deve ser um número inteiro.")
            continue
    
    materia = Materia(nome_materia, meta_horas)
    gerenciador.adicionar_materia(materia)
    salvar_materias(gerenciador)
    print(f"\nMatéria '{nome_materia}' adicionada com sucesso!")

def menu_materia(gerenciador):
    while True:
        if not gerenciador.listar_materias():
            print("\nNenhuma matéria cadastrada. Adicione uma matéria primeiro.")
            break

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
        menu_conteudos(materia, gerenciador)

def remover_materia(gerenciador):
    if not gerenciador.listar_materias():
        print("\nNão há matérias para remover.")
        return
    while True:
        print("\n=== Remover Matéria ===")
            
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
            
        confirmacao = input(f"Tem certeza que deseja remover a matéria '{materia.nome}'? (s/n): ").strip().lower()
        if confirmacao == 's':
            gerenciador.remover_materia(materia)
            salvar_materias(gerenciador)
            print(f"\nMatéria '{materia.nome}' removida com sucesso!")
        else:
            print("\nRemoção cancelada.")