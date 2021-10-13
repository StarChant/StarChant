import json
import pprint
import json
import random

pp = pprint.PrettyPrinter(indent=4)

master = json.load(open("./metadata-prerandomized.json"))

start = 1
end = 466

masterValues = list(master)[start:end]

random.seed("87314876641541055251095431619250856243264627284949971051498783260561907368646")

random.shuffle(masterValues)

with open(f'metadata-{start}-{end-1}.json', 'w', encoding='utf-8') as f:
    json.dump(masterValues, f, ensure_ascii=False, indent=4)