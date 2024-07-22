import json

peoples = [
    {'title':'ola', 'content':'como vai?'},
    {'title':'tchau', 'content':'ate mais'},
    {'title':'blz', 'content':'tudo otimo'},
]

peoples_json = []

with open('data_tasks.json', 'w') as jsonfile:
    json.dump(peoples, jsonfile)

print(peoples_json)

with open('data_tasks.json', 'r') as jsonfile:
    peoples_json = json.load(jsonfile)
    
print(peoples_json)

print(peoples_json[1]['title'])