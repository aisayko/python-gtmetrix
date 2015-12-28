__author__ = 'samycici'
import time
from gtmetrix import *
import json

with open('sites.json') as data_file:
    list_sites = json.load(data_file)

    for key, value in list_sites.items():
        print ("Site analisado: %s - Url: %s" % (key, value))
        gt = GTmetrixInterface('equipe-qualidade@infoglobo.com.br', '7207b7afe6497706233d1bcd71f8d891')
        print ("Iniciando Analise")
        my_test = gt.start_test(value)
        time.sleep(60)
        print ("Gravando resultados")
        results = gt.poll_state_request(key, my_test.test_id)


