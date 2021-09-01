import requests
import time

oneMin = 60
start_time = time.time()
seconds = 10
pload = {'username':'al','password':'123'}

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        requests.post("http://localhost:18000/post",data = pload)
        seconds += 10

