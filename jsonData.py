import json

def read_file(x):
    with open(f'{x}','r') as item_istance:
        return json.load(item_istance)

def write_file(path,x):
    with open(f'{path}','w') as item_file:
        json_ = json.dump(x,item_file,indent=4,ensure_ascii=False)
        return json_
