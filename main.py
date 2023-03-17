import requests

URL = 'https://httpbin.org/get'

response = requests.get(URL) #devuelve objeto del tipo response GET

print(response, type(response))     
print(response.status_code, type(response.status_code)) #int
print(response.url)
print(response.text, type(response.text)) #str
print(response.json()) #convierte la respuesta de .text a un objeto json dict (serializa)

payload = response.json() #payload es un dict
print(payload.get('origin'))

'''
QUERY - enviando informacion al servidor
'''
# query - para enviar informacion al servidor, despues del signo ? 
# https://httpbin.org/get?name=eduardo&password=123&email=fabenitez.dev@hotmail.com

URL = 'https://httpbin.org/get?name=fabenitez&password=123456&email=fabenitez.dev@hotmail.com'

response = requests.get(URL)

if response.status_code == 200:
    payload = response.json()
    params = payload['args']

    print('*********** HTTPBIN devuelve los datos enviados en el query como espejo *************')
    print('Nombre: ' + params['name'])
    print('Password: ' + params['password'])
    print('EMail: ' + params['email'])


