import json

def read_file(x):
    with open(f'{x}','r') as item_istance:
        return json.loads(item_istance.read())

def write_file(path,x):
    j_obj = json.dumps(x,ensure_ascii=False)
    with open(f'{path}','w') as item_file:
        item_file.write(j_obj)
        return j_obj
