class Worker:
    def __init__(self,nome):
        self.nome = nome
        self.n_clients = 0
    
    def __repr__(self):
        return self.nome + " atendeu " + str(self.n_clients) + " clientes"


