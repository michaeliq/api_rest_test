from flask import Flask, request, jsonify
from jsonData import read_file, write_file
from os import path

app = Flask(__name__)

if path.exists('items.json') != True:
    with open('items.json','w') as file_istance:
        items = {}
        write_file('items.json',items)

def key_(object_json):
    return 'item'+str(len(object_json))

@app.route('/')
def test_w():
    key_ = key_(items)
    items[key_] = []
    items[key_].append({'marco argente':'apellido','carmen magnolia':'nombre'})
    json_ = write_file('items.json',items)
    return json_

@app.route('/write_and_read/')
def test_rw():
    items = read_file('items.json')
    key = key_(items)
    items[key] = []
    items[key].append({'apellido':'cortez','nombre':'josué'})
    write_file('items.json',items)
    return items

@app.route('/items/',methods=['GET'])
def getItems():
    items = read_file('items.json')
    return jsonify({'message':'items in stock',
                    'items': items})

@app.route('/items/<string:name_item>/',methods=['GET'])
def getItem(name_item):
    items = read_file('items.json')
    item_founded = items.keys()
    item_founded = filter(lambda x: items.get(x)[0]['name']==name_item, item_founded)
    item_founded = list(item_founded)
    if len(item_founded) > 0:
        return jsonify({'message':'item founded!',
                        'item': items[item_founded[0]]})
    return jsonify({'message':'item not founded'})

@app.route('/items/',methods=['POST'])
def addItem():
    items = read_file('items.json')
    key = key_(items)
    items[key] = []

    item = {
        'name':request.json['name'],
        'description':request.json['description'],
        'group':request.json['group']}
    items[key].append(item)
    write_file('items.json',items)
    return jsonify({'message':'Item added'})

@app.route('/items/<string:name_item>/',methods=['PUT'])
def editItem(name_item):
    items = read_file('items.json')

    for item_key, item_value in items.items():
        if item_value[0]['name'] == name_item:
            item_value[0]['name']=request.json['name']
            item_value[0]['description']=request.json['description']
            item_value[0]['group']=request.json['group']

            items[item_key] = item_value
            write_file('items.json',items)
            return jsonify({'message':'item edited!',
                            'items': items})
    return jsonify({'message':'item not founded'})

@app.route('/items/<string:name_item>/',methods=['DELETE'])
def deleteItem(name_item):
    items = read_file('items.json')
    item_keys = items.keys()

    item_founded = filter(lambda x: items.get(x)[0]['name'] == name_item, item_keys)
    item_founded = list(item_founded)
    if len(item_founded) > 0:
        items.pop(item_founded[0], 'object not found')
        write_file('items.json',items)
        return jsonify({'message':'item deleted',
                        'items': items})
    return jsonify({'message':'item not founded'})


if __name__=="__main__":
    app.run(debug=True)
