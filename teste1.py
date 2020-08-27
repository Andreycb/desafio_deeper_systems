import pandas as pd
import json
from collections import defaultdict

watchers = defaultdict(list)
managers = defaultdict(list)

def salvar_arquivo(data, nome):
    nome += '.json'
    with open(nome, 'w') as f:
        json.dump(data, f, indent=4)

data = pd.read_json('source_file_2.json')
data = data.sort_values(by='priority', ascending=False)
data = data.values.tolist()

for i in data: #0-name 1-managers 2-whachers 3-priority
    name_proj = i[0]
    for watcher in i[2]:
        watchers[watcher].append(name_proj)
    for manager in i[1]:
        managers[manager].append(name_proj)

salvar_arquivo(watchers, 'watchers')
salvar_arquivo(managers, 'managers')
