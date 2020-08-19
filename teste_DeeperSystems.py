from collections import defaultdict
import json

def ler_arquivo():
    with open ('source_file_2.json', 'r') as f:
        return json.load(f)

data =  ler_arquivo()
managers = defaultdict(list)

for record in data:
    project_name = record['name']
    for manager in record['managers']:
        managers[manager].append(project_name)

with open('managers.json', 'w') as json_file:
    json.dump(managers, json_file, indent=4)

watchers = defaultdict(list)

for record in data:
    project_name = record['name']
    for watcher in record['watchers']:
        watchers[watcher].append(project_name)

with open('watchers.json', 'w') as json_file:
    json.dump(watchers, json_file, indent=4)