import json

with open('barcelona.json') as f:
    ds = json.load(f)
    with open("barcelona_inline.json", "a") as f:
        for d in ds:
            f.write(json.dumps(d) + "\n")