import requests

base_url = 'https://petstore.swagger.io/v2/pet'

# Метод GET
# Получение списка питомцев по статусу
res_0 = requests.get(base_url + '/findByStatus', params={'status': 'available'}, headers={'accept': 'application/json'})
print(res_0.status_code)
print(res_0.json())