class Conteudo:
    def __init__(self, nome):
        self.nome = nome
        self.status = "Não iniciado"
        self.anotacoes = []

    def atualizar_status(self, novo_status):
        self.status = novo_status   

    def adicionar_anotacao(self, anotacao):
        self.anotacoes.append(anotacao)

    def to_dict(self):
        return {
            "nome": self.nome,
            "status": self.status,
            "anotacoes": self.anotacoes
        }

    @classmethod
    def from_dict(cls, data):
        conteudo = cls(data["nome"])
        conteudo.status = data["status"]
        conteudo.anotacoes = data["anotacoes"]
        return conteudo