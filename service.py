import random

def budget_time():
    time = random.randint(15,300)
    return time

class Service:
    def __init__(self):
        self.nome = ''
        self.t_max = 0
        self.t_min = 0
        self.t_med = 0
    
    def service_time(self):
        service_time = random.randint(self.t_min,self.t_max)
        return service_time


    def __repr__(self):
        return self.nome + ", " + str(self.t_max) + ", " + str(self.t_min) + ", " + str(self.t_med)


