__author__ = 'samycici'
import time
from gtmetrix import *
import settings_sites

gt = GTmetrixInterface('equipe-qualidade@infoglobo.com.br', '7207b7afe6497706233d1bcd71f8d891')
my_test = gt.start_test(settings_sites.EXTRA)
time.sleep(60)
results = gt.poll_state_request(my_test.test_id)


