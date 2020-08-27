from collections import defaultdict
import json

def ler_arquivo():
    with open ('source_file_2.json', 'r') as f:
        return json.load(f)

data =  ler_arquivo()
managers = defaultdict(list)

for i in data:
    name_proj = i['name']
    for manager in i['managers']:
        managers[manager].append(name_proj)

with open('managers.json', 'w') as json_file:
    json.dump(managers, json_file, indent=4)

watchers = defaultdict(list)

for i in data:
    name_proj = i['name']
    for watcher in i['watchers']:
        watchers[watcher].append(name_proj)

with open('watchers.json', 'w') as json_file:
    json.dump(watchers, json_file, indent=4)
