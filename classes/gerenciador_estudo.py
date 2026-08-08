class GerenciadorEstudos:
    def __init__(self):
        self.materias = []

    def adicionar_materia(self, materia):
        self.materias.append(materia)

    def remover_materia(self, materia):
        if materia in self.materias:
            self.materias.remove(materia)

    def listar_materias(self):
        return self.materias

    def buscar_materia(self, nome):
        for materia in self.materias:
            if materia.nome == nome:
                return materia
        return None