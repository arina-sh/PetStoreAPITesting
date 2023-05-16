import requests
import json

base_url = 'https://petstore.swagger.io/v2/pet'
headers={'accept': 'application/json', 'Content-Type': 'application/json'}

# Метод POST
# Добавление питомца в магазин
data = {
  "id": 9223372036854775701,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Captain Pumpkin_2",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_1 = requests.post(base_url, headers=headers, data=json.dumps(data))
print(res_1.status_code)
print(res_1.json())
dict_data = json.loads(res_1.content)

petID = dict_data['id']

# Метод GET
# Получение питомца по id
res_2 = requests.get(base_url + f'/{petID}', headers={'accept': 'application/json'})
print(res_2.status_code)
print(res_2.json())

# Метод PUT
# Изменение питомца
data = {
  "id": 9223372036854775701,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Captain Pumpkin",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "sold"
}
res_3 = requests.put(base_url, headers=headers, data=json.dumps(data))
print(res_3.status_code)
print(res_3.json())

# Метод DELETE
# Изменение питомца
res_4 = requests.delete(base_url + f'/{petID}', headers={'accept': 'application/json'})
print(res_4.status_code)
print(res_4.json())