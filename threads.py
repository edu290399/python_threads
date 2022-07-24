from threading import Thread
import threading
from service import *
import time
from definitions import *
threads = []

class Th(Thread):

    def __init__ (self,worker):
        self.worker = worker
        Thread.__init__(self)
        self.budget_time = budget_time()

    def run(self):
        t = self
        threads.append(t)
        del(available_workers[0])
        del(waiting_clients[0])
        print(self.worker.nome+" iniciando o orçamento")
        time.sleep(self.budget_time/1000)
        print("Orçamento realizado em "+ str(self.budget_time) +" minutos, por " + self.worker.nome)
        service_choice = random.choice(services_list)
        print(self.worker.nome + " iniciando o serviço: " +service_choice.nome)
        sleep_time = service_choice.service_time()/1000
        time.sleep(sleep_time)
        print("Serviço concluido: " + service_choice.nome + " em " + str(sleep_time*1000) + "por: " + self.worker.nome)
        self.worker.n_clients += 1
        available_workers.append(self.worker)
