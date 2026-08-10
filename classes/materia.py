from classes.conteudo import Conteudo


class Materia:
    def __init__(self, nome, meta_horas):
        self.nome = nome
        self.meta_horas = meta_horas
        self.horas_estudadas = 0
        self.conteudos = []

    def adicionar_conteudo(self, conteudo):
        self.conteudos.append(conteudo)

    def registrar_estudo(self, horas):
        self.horas_estudadas += horas

    def calcular_progresso_horas(self):
        if self.meta_horas == 0:
            return 0
        return (self.horas_estudadas / self.meta_horas) * 100

    def calcular_progresso_conteudos(self):
        total_conteudos = len(self.conteudos)
        if total_conteudos == 0:
            return 0
        conteudos_concluidos = sum(1 for conteudo in self.conteudos if conteudo.status == "Concluído")
        return (conteudos_concluidos / total_conteudos) * 100

    def calcular_progresso_total(self):
        progresso_horas = self.calcular_progresso_horas()
        progresso_conteudos = self.calcular_progresso_conteudos()
        return (progresso_horas + progresso_conteudos) / 2

    def mostrar_conteudos(self):
        for conteudo in self.conteudos:
            print(f"Conteúdo: {conteudo.nome}, Status: {conteudo.status}, Anotações: {conteudo.anotacoes}")

    def remover_conteudo(self, nome_conteudo):
        for conteudo in self.conteudos:
            if conteudo.nome == nome_conteudo:
                self.conteudos.remove(conteudo)
                return 

    def to_dict(self):
        return {
            "nome": self.nome,
            "meta_horas": self.meta_horas,
            "horas_estudadas": self.horas_estudadas,
            "conteudos": [conteudo.to_dict() for conteudo in self.conteudos]
        }

    @classmethod
    def from_dict(cls, data):
        materia = cls(data["nome"], data["meta_horas"])
        materia.horas_estudadas = data["horas_estudadas"]
        materia.conteudos = [Conteudo.from_dict(conteudo_data) for conteudo_data in data["conteudos"]]
        return materia