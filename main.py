from classes.gerenciador_estudo import GerenciadorEstudos
from funcoes.gerenciamento_materias import adicionar_materia, menu_materia, remover_materia
from funcoes.persistencia import carregar_materias
from funcoes.progresso import registrar_progresso, ver_progresso

gerenciador = GerenciadorEstudos()
carregar_materias(gerenciador)

while True:
    print("\nMenu:")
    print("1. Adicionar matéria")
    print("2. Ver matérias e conteúdos")
    print("3. Registrar progresso de estudo")
    print("4. Ver progresso de estudo")
    print("5. Remover matéria")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")
    if escolha not in ["1", "2", "3", "4", "5", "6"]:
        print("\nOpção inválida. Tente novamente.")
        continue

    if escolha == "1":
         adicionar_materia(gerenciador)

    elif escolha == "2":
          menu_materia(gerenciador)

    elif escolha == "3":
        registrar_progresso(gerenciador)

    elif escolha == "4":
        ver_progresso(gerenciador)

    elif escolha == "5":
          remover_materia(gerenciador)

    elif escolha == "6":
        print("Saindo do programa...")
        break