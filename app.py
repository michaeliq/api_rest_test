from flask import Flask, request, jsonify
from jsonData import read_file, write_file

app = Flask(__name__)

items = []

@app.route('/')
def test_w():
    test_ = [{'marco argente':'apellido','carmen magnolia':'nombre'}]
    json_ = write_file('items.json',test_)
    return json_

@app.route('/write_and_read/')
def test_rw():
    json_ = read_file('items.json')
    test_ = {'apellido':'cortez','nombre':'josué'}
    json_.append(test_)
    return write_file('items.json',json_)

@app.route('/items/',methods=['GET'])
def getItems():

    return jsonify({'message':'items in stock',
                    'items': items})

@app.route('/item/<int:name_item>/',methods=['GET'])
def getItem(name_item):
    
    item_founded = [item for item in items if item['name'] == name_item]
    if len(item_founded) > 0:
        return jsonify({'message':'item founded!',
                        'item': item_founded})
    return jsonify({'message':'item not founded'})

@app.route('/items/',methods=['POST'])
def addItem():
    
    item = {
        'name':request.json['name'],
        'description':request.json['description'],
        'group':request.json['group']}
    items.append(item)
    print(items)
     
    return jsonify({'message':'Item added'})

@app.route('/items/<string:name_item>/',methods=['PUT'])
def editItem(name_item):
    
    if item['name'] in items:
        item['name']=request.json['name']
        item['description']=request.json['description']
        item['group']=request.json['group']
        
        return ({'message':'item edited!',
                 'items': items})
    return jsonify({'message':'item not founded'})

@app.route('/items/<string:name_item>/',methods=['DELETE'])
def deleteItem(name_item):
    
    item_founded = [item for item in items if item['name'] == name_item]
    if len(item_founded) > 0:
        items.remove(item_founded)
        
        return jsonify({'message':'item deleted',
                        'items': items})
    return jsonify({'message':'item not founded'})


if __name__=="__main__":
    app.run(debug=True)
