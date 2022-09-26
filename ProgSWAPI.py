import requests
import re


for i in range (1,15): 
    web_url = requests.get('https://swapi.dev/api/people/' + str(i))
    f=open('my_file.txt','a')
    f.write(web_url.json()["name"])
    f.write("\n")
    f.close()

print("Привет")