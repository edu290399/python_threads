from time import sleep
from definitions import *
from threads import *
from service import *

## Serviços diversos com tempo médio de atendimento,
## com tempo mínimo e máximo estimados
## cliente chega -> mecânico atende -> orçamento do serviço escolhido
## fase de orçamento dura no máximo 5 horas
## Serviço -> orçamento -> execução (conserto)

## SISTEMA IMPRIME
## .cliente e o serviço selecionado
## .o nome do mecânico que realizará as ações
## .tempo de duração do orçamento
## .tempo de duração do conserto
## .quantos clientes cada mecânico atendeu

def main():
        while (len(waiting_clients) != 0):
                while(len(available_workers) == 0):
                        print(str(len(waiting_clients)) + "Clientes aguardando mecanico disponivel...")
                        sleep(0.1)
                else:
                        print("Cliente " + waiting_clients[0] + " sendo atendido" )
                        worker = available_workers[0]
                        new_thread = Th(worker)
                        new_thread.start()
                        print('trabalhadores disponiveis: '+ str(len(available_workers)))
                
        for x in threads:
                x.join()
        print(str(available_workers))
        print("Clientes aguardando:" + str(len(waiting_clients)))




main()
# for thread_number in range (5):
#         thread = Th(thread_number)
#         thread.start()