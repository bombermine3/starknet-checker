import json

eligibles = {}
for i in range(0, 7):
    with open(f"data/starknet-{i}.json") as f:
        entities = json.load(f)['eligibles']
        for e in entities:
            eligibles[e['identity']] = e['amount']

print("Total addresses: ", len(eligibles))

with open('wallets.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line in eligibles:
            print(f"{line} {eligibles[line]}")
