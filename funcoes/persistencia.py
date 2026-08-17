import json
from classes.materia import Materia

def salvar_materias(gerenciador):
    with open("materias.json", "w", encoding="utf-8") as arquivo:
        json.dump([materia.to_dict() for materia in gerenciador.listar_materias()], arquivo, indent=4, ensure_ascii=False)

def carregar_materias(gerenciador):
    with open("materias.json", "r", encoding="utf-8") as arquivo:
        materias_data = json.load(arquivo)
        for materia_data in materias_data:
            materia = Materia.from_dict(materia_data)
            gerenciador.adicionar_materia(materia)