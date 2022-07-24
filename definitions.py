from service import *
from workers import *

service1 = Service()
service1.nome = 'Reparo de parabrisa'
service1.t_max = 4000
service1.t_med = 3000
service1.t_min = 2000

service2 = Service()
service2.nome = 'Troca de pneu'
service2.t_max = 600
service2.t_med = 300
service2.t_min = 200

service3 = Service()
service3.nome = 'Troca de oleo'
service3.t_max = 30
service3.t_med = 20
service3.t_min = 10

service4 = Service()
service4.nome = 'Vulcanizacao'
service4.t_max = 1600
service4.t_med = 1400
service4.t_min = 1200

service5 = Service()
service5.nome = 'Pintura'
service5.t_max = 300
service5.t_med = 250
service5.t_min = 200

service6 = Service()
service6.nome = 'Lavagem'
service6.t_max = 100
service6.t_med = 60
service6.t_min = 40


services_list = []
workers_list = [Worker('Adelino'),Worker('Brizola'),Worker('Cleiton')]
client_list = ['Dirson','Eusebio','Farid','Gustavo', 'Heitor','Igor','Joao','Kelly','Ludmilla','Mona','Nadia','Olavo','Pedro',]

services_list.append(service1)
services_list.append(service2)
services_list.append(service3)
services_list.append(service4)
services_list.append(service5)
services_list.append(service6)

available_workers = workers_list
waiting_clients = client_list