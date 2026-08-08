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

    def calcular_progresso_semanal(self):
        if self.meta_horas == 0:
            return 0
        return (self.horas_estudadas / self.meta_horas) * 100

    def calcular_progresso_geral(self):
        total_conteudos = len(self.conteudos)
        if total_conteudos == 0:
            return 0
        conteudos_concluidos = sum(1 for conteudo in self.conteudos if conteudo.status == "Concluído")
        return (conteudos_concluidos / total_conteudos) * 100

    def mostrar_conteudos(self):
        for conteudo in self.conteudos:
            print(f"Conteúdo: {conteudo.nome}, Status: {conteudo.status}, Anotações: {conteudo.anotacoes}")