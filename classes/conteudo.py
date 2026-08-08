class Conteudo:
    def __init__(self, nome):
        self.nome = nome
        self.status = "Não iniciado"
        self.anotacoes = []

    def atualizar_status(self, novo_status):
        self.status = novo_status   

    def adicionar_anotacao(self, anotacao):
        self.anotacoes.append(anotacao)
